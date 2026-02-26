#!/usr/bin/env python3
"""
validate-features.py

Validates features.json structure and content against expected schema.
Supports both v1 and v2 features.json formats.

Usage:
    python validate-features.py path/to/features.json
    python validate-features.py --schema path/to/features.schema.json path/to/features.json

Features:
- Schema validation (if schema provided)
- Required fields checking
- Data type validation
- Enum value validation
- Dependency checking (no circular deps, valid feature IDs)
- Progress consistency (0-100, matches status)
- Date format validation
- Subtask consistency
- v2: verification object validation
- v2: files array validation
"""

import json
import re
import sys
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Set, Tuple

# Color output for terminal
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    END = '\033[0m'

class FeatureValidator:
    """Validates features.json structure and content"""

    VALID_STATUSES = ['pending', 'in_progress', 'blocked', 'completed', 'descoped']
    VALID_PRIORITIES = ['critical', 'high', 'medium', 'low']
    VALID_EFFORTS = ['small', 'medium', 'large', 'xlarge']

    V2_STATUSES = ['planned', 'in-progress', 'blocked', 'complete', 'archived']
    V2_VERIFICATION_STATUSES = ['PENDING', 'IN_PROGRESS', 'VERIFIED', 'BLOCKED', 'NOT_APPLICABLE']

    def __init__(self, features_data: Dict[str, Any]):
        self.data = features_data
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.info: List[str] = []

        # Detect version
        raw_version = self.data.get('version')
        if raw_version == '2.0':
            self.version = 2
        elif raw_version == 2.0 or raw_version == 2:
            self.version = 2
            self.warnings.append(
                f"'version' should be the string \"2.0\", not numeric {raw_version!r}. "
                "Treating as v2 but please update to a string."
            )
        else:
            self.version = 1

    def validate(self) -> bool:
        """Run all validations. Returns True if valid, False otherwise."""
        version_label = f"v{self.version}"
        print(f"{Colors.BOLD}Validating features.json ({version_label})...{Colors.END}\n")

        # Basic structure
        self._check_required_top_level_fields()
        self._check_features_list()

        if 'features' in self.data:
            # Feature-level validations
            feature_ids = self._collect_feature_ids()

            for idx, feature in enumerate(self.data['features']):
                self._validate_feature(feature, idx, feature_ids)

        # Project-level validations
        self._check_project_consistency()
        self._check_dependencies()

        # Print results
        self._print_results()

        return len(self.errors) == 0

    def _check_required_top_level_fields(self):
        """Check required fields at project level"""
        if self.version == 2:
            required = ['version', 'project', 'features']
        else:
            required = ['project', 'features']

        for field in required:
            if field not in self.data:
                self.errors.append(f"Missing required top-level field: '{field}'")

        # v2: project must be an object
        if self.version == 2 and 'project' in self.data:
            if not isinstance(self.data['project'], dict):
                self.errors.append("'project' must be an object in v2 schema")

    def _check_features_list(self):
        """Verify features is a list"""
        if 'features' in self.data:
            if not isinstance(self.data['features'], list):
                self.errors.append("'features' must be an array")
            elif len(self.data['features']) == 0:
                self.warnings.append("'features' array is empty")

    def _collect_feature_ids(self) -> Set[str]:
        """Collect all feature IDs for dependency checking"""
        return {f.get('id') for f in self.data['features'] if 'id' in f}

    def _validate_feature(self, feature: Dict[str, Any], idx: int, all_ids: Set[str]):
        """Validate individual feature"""
        context = f"Feature {idx}"
        if 'id' in feature:
            context = f"Feature {feature['id']}"

        # Required fields
        if self.version == 2:
            required = ['id', 'title', 'status', 'verification']
        else:
            required = ['id', 'name', 'status']

        for field in required:
            if field not in feature:
                self.errors.append(f"{context}: Missing required field '{field}'")

        # ID format
        if 'id' in feature:
            fid = feature['id']
            if not isinstance(fid, str):
                self.errors.append(f"{context}: 'id' must be a string")
            elif self.version == 2:
                if not re.match(r'^[a-z0-9]+(-[a-z0-9]+)*$', fid):
                    self.errors.append(
                        f"{context}: ID must be kebab-case (lowercase alphanumeric segments separated by single hyphens, got: {fid})"
                    )
            else:
                if not fid.startswith('F'):
                    self.warnings.append(f"{context}: ID should start with 'F' (got: {fid})")
                elif not fid[1:].isdigit():
                    self.warnings.append(f"{context}: ID should be F followed by digits (got: {fid})")

        # Status
        if 'status' in feature:
            status = feature['status']
            valid = self.V2_STATUSES if self.version == 2 else self.VALID_STATUSES
            if status not in valid:
                self.errors.append(
                    f"{context}: Invalid status '{status}'. "
                    f"Must be one of: {', '.join(valid)}"
                )

        # Priority
        if 'priority' in feature:
            priority = feature['priority']
            if priority not in self.VALID_PRIORITIES:
                self.errors.append(
                    f"{context}: Invalid priority '{priority}'. "
                    f"Must be one of: {', '.join(self.VALID_PRIORITIES)}"
                )

        # Estimated effort (v1 only)
        if self.version == 1 and 'estimatedEffort' in feature:
            effort = feature['estimatedEffort']
            if effort not in self.VALID_EFFORTS:
                self.errors.append(
                    f"{context}: Invalid estimatedEffort '{effort}'. "
                    f"Must be one of: {', '.join(self.VALID_EFFORTS)}"
                )

        # Progress (v1 only)
        if self.version == 1 and 'progress' in feature:
            progress = feature['progress']
            if not isinstance(progress, (int, float)):
                self.errors.append(f"{context}: 'progress' must be a number")
            elif not 0 <= progress <= 100:
                self.errors.append(f"{context}: 'progress' must be between 0 and 100 (got: {progress})")

            # Progress should match status
            status = feature.get('status')
            if status == 'completed' and progress != 100:
                self.warnings.append(f"{context}: Status is 'completed' but progress is {progress}%")
            elif status == 'pending' and progress > 0:
                self.warnings.append(f"{context}: Status is 'pending' but progress is {progress}%")

        # Dependencies
        if 'dependencies' in feature:
            deps = feature['dependencies']
            if not isinstance(deps, list):
                self.errors.append(f"{context}: 'dependencies' must be an array")
            else:
                for dep in deps:
                    if dep not in all_ids:
                        self.errors.append(f"{context}: Unknown dependency '{dep}'")

        # Dates
        for date_field in ['startedDate', 'completedDate', 'dueDate']:
            if date_field in feature:
                self._validate_date(feature[date_field], context, date_field)

        # Subtasks
        if 'subtasks' in feature:
            self._validate_subtasks(feature['subtasks'], context)

        # Blockers
        if 'blockers' in feature:
            blockers = feature['blockers']
            if not isinstance(blockers, list):
                self.errors.append(f"{context}: 'blockers' must be an array")

        # v2-only validations
        if self.version == 2:
            if 'verification' in feature:
                self._validate_verification_object(feature['verification'], context)

            if 'files' in feature:
                self._validate_v2_files(feature['files'], context)

    def _validate_date(self, date_str: str, context: str, field: str):
        """Validate date format (YYYY-MM-DD)"""
        if date_str is None:
            return

        if not isinstance(date_str, str):
            self.errors.append(f"{context}: '{field}' must be a string")
            return

        try:
            datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError:
            self.errors.append(
                f"{context}: '{field}' has invalid date format. "
                f"Expected YYYY-MM-DD, got: {date_str}"
            )

    def _validate_subtasks(self, subtasks: List[Dict], context: str):
        """Validate subtasks structure"""
        if not isinstance(subtasks, list):
            self.errors.append(f"{context}: 'subtasks' must be an array")
            return

        for idx, subtask in enumerate(subtasks):
            sub_context = f"{context} > Subtask {idx+1}"

            # Required fields
            if 'id' not in subtask:
                self.errors.append(f"{sub_context}: Missing 'id'")
            if self.version == 1 and 'name' not in subtask:
                self.errors.append(f"{sub_context}: Missing 'name'")
            if 'status' not in subtask:
                self.errors.append(f"{sub_context}: Missing 'status'")

            # Status validation
            if 'status' in subtask:
                valid = self.V2_STATUSES if self.version == 2 else self.VALID_STATUSES
                if subtask['status'] not in valid:
                    self.errors.append(
                        f"{sub_context}: Invalid status '{subtask['status']}'"
                    )

    def _validate_verification_object(self, verification: Any, context: str):
        """Validate v2 verification object"""
        if not isinstance(verification, dict):
            self.errors.append(f"{context}: 'verification' must be an object")
            return

        # Required fields
        if 'file' not in verification:
            self.errors.append(f"{context}: verification missing required field 'file'")
        elif verification['file'] is not None and not isinstance(verification['file'], str):
            self.errors.append(f"{context}: verification 'file' must be a string or null")

        if 'status' not in verification:
            self.errors.append(f"{context}: verification missing required field 'status'")
        elif verification['status'] not in self.V2_VERIFICATION_STATUSES:
            self.errors.append(
                f"{context}: Invalid verification status '{verification['status']}'. "
                f"Must be one of: {', '.join(self.V2_VERIFICATION_STATUSES)}"
            )

        # Optional integer fields
        for int_field in ['files_verified', 'files_total', 'blocking_issues']:
            if int_field in verification:
                val = verification[int_field]
                if not isinstance(val, int):
                    self.errors.append(f"{context}: verification '{int_field}' must be an integer")
                elif val < 0:
                    self.errors.append(f"{context}: verification '{int_field}' must be >= 0 (got: {val})")

    def _validate_v2_files(self, files: Any, context: str):
        """Validate v2 files array"""
        if not isinstance(files, list):
            self.errors.append(f"{context}: 'files' must be an array")
            return

        valid_actions = ['create', 'modify', 'delete']

        for idx, entry in enumerate(files):
            file_context = f"{context} > File {idx+1}"

            if not isinstance(entry, dict):
                self.errors.append(f"{file_context}: file entry must be an object")
                continue

            # Required fields
            if 'path' not in entry:
                self.errors.append(f"{file_context}: Missing required field 'path'")
            elif not isinstance(entry['path'], str):
                self.errors.append(f"{file_context}: 'path' must be a string")

            if 'verification_status' not in entry:
                self.errors.append(f"{file_context}: Missing required field 'verification_status'")
            elif entry['verification_status'] not in self.V2_VERIFICATION_STATUSES:
                self.errors.append(
                    f"{file_context}: Invalid verification_status '{entry['verification_status']}'. "
                    f"Must be one of: {', '.join(self.V2_VERIFICATION_STATUSES)}"
                )

            # Optional fields
            if 'action' in entry:
                if entry['action'] not in valid_actions:
                    self.errors.append(
                        f"{file_context}: Invalid action '{entry['action']}'. "
                        f"Must be one of: {', '.join(valid_actions)}"
                    )

            if 'depends_on' in entry:
                if not isinstance(entry['depends_on'], list):
                    self.errors.append(f"{file_context}: 'depends_on' must be an array")
                else:
                    all_paths = {e.get('path') for e in files if isinstance(e, dict) and 'path' in e}
                    for dep in entry['depends_on']:
                        if not isinstance(dep, str):
                            self.errors.append(f"{file_context}: 'depends_on' entries must be strings")
                        elif dep not in all_paths:
                            self.errors.append(
                                f"{file_context}: depends_on references '{dep}' which is not in this feature's files list"
                            )

            if 'verified_at' in entry:
                val = entry['verified_at']
                if not isinstance(val, str):
                    self.errors.append(f"{file_context}: 'verified_at' must be a string")

        # Check for circular file-level dependencies
        file_graph: Dict[str, List[str]] = {}
        for entry in files:
            if isinstance(entry, dict) and 'path' in entry:
                file_graph[entry['path']] = [
                    d for d in entry.get('depends_on', []) if isinstance(d, str)
                ]

        def _file_has_cycle(node: str, visited: Set[str], rec_stack: Set[str]) -> bool:
            visited.add(node)
            rec_stack.add(node)
            for neighbor in file_graph.get(node, []):
                if neighbor not in visited:
                    if _file_has_cycle(neighbor, visited, rec_stack):
                        return True
                elif neighbor in rec_stack:
                    return True
            rec_stack.remove(node)
            return False

        visited: Set[str] = set()
        for node in file_graph:
            if node not in visited:
                if _file_has_cycle(node, visited, set()):
                    self.errors.append(f"{context}: Circular file dependency detected involving '{node}'")
                    break

    def _check_project_consistency(self):
        """Check project-wide consistency"""
        if 'features' not in self.data:
            return

        # Check for duplicate IDs
        ids = [f.get('id') for f in self.data['features'] if 'id' in f]
        duplicates = [fid for fid in ids if ids.count(fid) > 1]
        if duplicates:
            unique_dups = set(duplicates)
            self.errors.append(f"Duplicate feature IDs found: {', '.join(unique_dups)}")

        # Check progress stats
        total = len(self.data['features'])

        if self.version == 2:
            completed = sum(1 for f in self.data['features'] if f.get('status') == 'complete')
            in_progress = sum(1 for f in self.data['features'] if f.get('status') == 'in-progress')
        else:
            completed = sum(1 for f in self.data['features'] if f.get('status') == 'completed')
            in_progress = sum(1 for f in self.data['features'] if f.get('status') == 'in_progress')

        self.info.append(f"Total features: {total}")
        self.info.append(f"Completed: {completed} ({completed/total*100:.1f}%)")
        self.info.append(f"In progress: {in_progress}")

    def _check_dependencies(self):
        """Check for circular dependencies"""
        if 'features' not in self.data:
            return

        # Build dependency graph
        graph: Dict[str, List[str]] = {}
        for feature in self.data['features']:
            fid = feature.get('id')
            if fid:
                graph[fid] = feature.get('dependencies', [])

        # Check for cycles using DFS
        def has_cycle(node: str, visited: Set[str], rec_stack: Set[str]) -> bool:
            visited.add(node)
            rec_stack.add(node)

            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    if has_cycle(neighbor, visited, rec_stack):
                        return True
                elif neighbor in rec_stack:
                    return True

            rec_stack.remove(node)
            return False

        visited: Set[str] = set()
        for node in graph:
            if node not in visited:
                if has_cycle(node, visited, set()):
                    self.errors.append(f"Circular dependency detected involving {node}")
                    break

    def _print_results(self):
        """Print validation results with colors"""
        print()

        if self.info:
            print(f"{Colors.BLUE}{Colors.BOLD}Info:{Colors.END}")
            for msg in self.info:
                print(f"{Colors.BLUE}  ℹ {msg}{Colors.END}")
            print()

        if self.warnings:
            print(f"{Colors.YELLOW}{Colors.BOLD}Warnings:{Colors.END}")
            for msg in self.warnings:
                print(f"{Colors.YELLOW}  ⚠ {msg}{Colors.END}")
            print()

        if self.errors:
            print(f"{Colors.RED}{Colors.BOLD}Errors:{Colors.END}")
            for msg in self.errors:
                print(f"{Colors.RED}  ✗ {msg}{Colors.END}")
            print()
            print(f"{Colors.RED}{Colors.BOLD}Validation FAILED{Colors.END}")
        else:
            print(f"{Colors.GREEN}{Colors.BOLD}✓ Validation PASSED{Colors.END}")


def validate_with_schema(features_path: Path, schema_path: Path) -> bool:
    """Validate using JSON Schema (requires jsonschema library)"""
    try:
        import jsonschema
    except ImportError:
        print(f"{Colors.RED}Error: jsonschema library not found.{Colors.END}")
        print("Install with: pip install jsonschema")
        return False

    with open(schema_path) as f:
        schema = json.load(f)

    with open(features_path) as f:
        features = json.load(f)

    try:
        jsonschema.validate(features, schema)
        print(f"{Colors.GREEN}✓ Schema validation passed{Colors.END}\n")
        return True
    except jsonschema.exceptions.ValidationError as e:
        print(f"{Colors.RED}✗ Schema validation failed:{Colors.END}")
        print(f"{Colors.RED}  {e.message}{Colors.END}\n")
        return False


def main():
    parser = argparse.ArgumentParser(description='Validate features.json file')
    parser.add_argument('features_file', help='Path to features.json')
    parser.add_argument('--schema', help='Path to features.schema.json (optional)')

    args = parser.parse_args()

    features_path = Path(args.features_file)

    # Check file exists
    if not features_path.exists():
        print(f"{Colors.RED}Error: File not found: {features_path}{Colors.END}")
        sys.exit(1)

    # Load features.json
    try:
        with open(features_path) as f:
            features_data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"{Colors.RED}Error: Invalid JSON in {features_path}{Colors.END}")
        print(f"{Colors.RED}  {e}{Colors.END}")
        sys.exit(1)

    # Validate with schema if provided
    if args.schema:
        schema_path = Path(args.schema)
        if not schema_path.exists():
            print(f"{Colors.RED}Error: Schema file not found: {schema_path}{Colors.END}")
            sys.exit(1)

        schema_valid = validate_with_schema(features_path, schema_path)
        if not schema_valid:
            sys.exit(1)

    # Run custom validations
    validator = FeatureValidator(features_data)
    is_valid = validator.validate()

    sys.exit(0 if is_valid else 1)


if __name__ == '__main__':
    main()
