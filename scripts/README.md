# Scripts

Utility scripts for working with features.json and the feature definition workflow.

---

## validate-features.py

Python script for validating features.json structure and content.

### Features

✅ **Required field checking** - Ensures all required fields are present
✅ **Data type validation** - Verifies correct types (string, number, array, etc.)
✅ **Enum value validation** - Checks status, priority, effort against allowed values
✅ **Dependency checking** - Validates feature IDs exist, detects circular dependencies
✅ **Progress consistency** - Ensures progress matches status (completed = 100%, etc.)
✅ **Date format validation** - Validates YYYY-MM-DD format
✅ **Subtask validation** - Checks subtask structure and required fields
✅ **ID format checking** - Warns about non-standard ID formats
✅ **Duplicate detection** - Finds duplicate feature IDs
✅ **Schema validation** - Optional JSON Schema validation (requires jsonschema library)

### Usage

**Basic validation:**
```bash
python scripts/validate-features.py path/to/features.json
```

**With JSON Schema validation:**
```bash
python scripts/validate-features.py --schema templates/features.schema.json path/to/features.json
```

**Example output:**
```
Validating features.json...

Info:
  ℹ Total features: 8
  ℹ Completed: 2 (25.0%)
  ℹ In progress: 1

Warnings:
  ⚠ Feature F003: Status is 'pending' but progress is 10%

Errors:
  ✗ Feature F005: Missing required field 'status'
  ✗ Feature F007: Invalid priority 'urgent'. Must be one of: critical, high, medium, low

Validation FAILED
```

### What It Checks

**Required Fields:**
- Top-level: `project`, `features`
- Feature-level: `id`, `name`, `status`
- Subtask-level: `id`, `name`, `status`

**Valid Enums:**
- **Status**: `pending`, `in_progress`, `blocked`, `completed`, `descoped`
- **Priority**: `critical`, `high`, `medium`, `low`
- **Effort**: `small`, `medium`, `large`, `xlarge`

**Data Consistency:**
- Progress between 0-100
- Progress matches status (completed = 100%, pending = 0%)
- Dependencies reference existing feature IDs
- No circular dependencies
- Date format: YYYY-MM-DD
- No duplicate feature IDs

**ID Format Recommendations:**
- Should start with 'F'
- Followed by digits (F001, F002, etc.)
- Warnings only, not errors

### Exit Codes

- `0` - Validation passed
- `1` - Validation failed (errors found)

### Dependencies

**Required:**
- Python 3.6+
- No external dependencies for basic validation

**Optional:**
- `jsonschema` library for schema validation
  ```bash
  pip install jsonschema
  ```

### Integration Examples

**Pre-commit hook:**
```bash
#!/bin/bash
# .git/hooks/pre-commit
python scripts/validate-features.py features.json || exit 1
```

**Makefile target:**
```makefile
validate-features:
	@python scripts/validate-features.py features.json

validate-features-schema:
	@python scripts/validate-features.py --schema templates/features.schema.json features.json
```

**CI/CD pipeline:**
```yaml
# .github/workflows/validate.yml
- name: Validate features.json
  run: |
    pip install jsonschema
    python scripts/validate-features.py --schema templates/features.schema.json features.json
```

### Common Issues

**Issue**: "Missing required field 'status'"
**Fix**: Add `"status": "pending"` to the feature

**Issue**: "Invalid priority 'urgent'"
**Fix**: Use one of: `critical`, `high`, `medium`, `low`

**Issue**: "Unknown dependency 'F999'"
**Fix**: Ensure dependency ID exists in features array

**Issue**: "Circular dependency detected"
**Fix**: Check dependency chain - Feature A depends on B, B depends on C, C depends on A

**Issue**: "Duplicate feature IDs found: F005"
**Fix**: Each feature must have unique ID

---

## Future Scripts

Additional scripts planned for this directory:

**generate-feature-doc.py**
- Generate markdown feature document from template
- Interactive prompts for required fields
- Integrates with features.json

**sync-to-github.py**
- Sync features.json to GitHub Issues
- Bi-directional updates
- Status synchronization

**feature-stats.py**
- Generate project statistics
- Progress charts
- Burndown data
- Time estimates

**compact-session.py**
- Compact session files
- Preserve history
- Reduce context size

---

## Contributing

If you create useful scripts for the feature definition workflow, please share them with the community!

**Guidelines:**
- Clear usage documentation
- Example output
- Exit codes documented
- Error messages helpful
- Works cross-platform (or note limitations)

---

## License

MIT License - Part of feature-definition-workflow
