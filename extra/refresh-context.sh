#!/bin/bash
# refresh-context.sh
# Generate concise context summary for fresh Claude session
#
# This script extracts key information from session files and project state
# to provide AI agents with just enough context to resume work efficiently.
#
# Usage: ./refresh-context.sh [output-file]
# Default output: /tmp/context-refresh.md

set -e

OUTPUT_FILE="${1:-/tmp/context-refresh.md}"

cat > "$OUTPUT_FILE" << 'HEADER'
# Context Refresh Summary

HEADER

echo "Generated: $(date '+%Y-%m-%d %H:%M:%S')" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

# 1. Current work (from SESSION-CURRENT.md)
echo "## 🎯 CURRENT SESSION" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
if [ -f ~/workspace/SESSION-CURRENT.md ]; then
    # Extract just the "Active Work" section
    sed -n '/## Active Work/,/## Next Actions/p' ~/workspace/SESSION-CURRENT.md | head -n -1 >> "$OUTPUT_FILE"
else
    echo "No active session file found." >> "$OUTPUT_FILE"
fi

# 2. Recent commits (last 5, excluding merges)
echo "" >> "$OUTPUT_FILE"
echo "## 📝 RECENT COMMITS" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
cd ~/workspace
git log --oneline --no-merges -5 2>/dev/null >> "$OUTPUT_FILE" || echo "Not in git repository" >> "$OUTPUT_FILE"

# 3. Active projects quick status
echo "" >> "$OUTPUT_FILE"
echo "## 🚧 ACTIVE PROJECTS" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

# Scan for active projects (customize paths for your workspace)
for project_dir in ~/workspace/projects/*/; do
    if [ -d "$project_dir" ]; then
        project_name=$(basename "$project_dir")
        echo "**$project_name**: [Add status description]" >> "$OUTPUT_FILE"
        echo "  Location: $project_dir" >> "$OUTPUT_FILE"
    fi
done

# 4. Feature status (from features.json if exists)
echo "" >> "$OUTPUT_FILE"
echo "## 📊 FEATURE STATUS" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
features_found=false
for project_dir in ~/workspace/projects/*/; do
    if [ -f "$project_dir/features.json" ]; then
        project_name=$(basename "$project_dir")

        # Check if any features are in_progress
        in_progress=$(jq -r '.features[]? | select(.status=="in_progress") | "  - [\(.progress)%] \(.name)"' "$project_dir/features.json" 2>/dev/null)

        if [ -n "$in_progress" ]; then
            echo "**$project_name**:" >> "$OUTPUT_FILE"
            echo "$in_progress" >> "$OUTPUT_FILE"
            echo "" >> "$OUTPUT_FILE"
            features_found=true
        fi
    fi
done

if [ "$features_found" = false ]; then
    echo "No features currently in progress." >> "$OUTPUT_FILE"
fi

# 5. Test status (from tests.json if exists)
echo "" >> "$OUTPUT_FILE"
echo "## ✅ TEST STATUS" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
tests_found=false
for project_dir in ~/workspace/projects/*/; do
    if [ -f "$project_dir/tests.json" ]; then
        project_name=$(basename "$project_dir")
        echo "**$project_name**:" >> "$OUTPUT_FILE"
        jq -r '.summary | "  Total: \(.total) | Passing: \(.passing) | Failing: \(.failing) | Coverage: \(.coverage.lines // 0)%"' "$project_dir/tests.json" >> "$OUTPUT_FILE"
        tests_found=true
    fi
done

if [ "$tests_found" = false ]; then
    echo "No test manifests found. Tests tracked per project normally." >> "$OUTPUT_FILE"
fi

# 6. Blockers (from features.json)
echo "" >> "$OUTPUT_FILE"
echo "## 🚧 BLOCKERS" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
blockers_found=false
for project_dir in ~/workspace/projects/*/; do
    if [ -f "$project_dir/features.json" ]; then
        project_name=$(basename "$project_dir")
        blockers=$(jq -r '.blockers[]? | select(.status=="open") | "  - [\(.id)] \(.description)"' "$project_dir/features.json" 2>/dev/null)

        if [ -n "$blockers" ]; then
            echo "**$project_name**:" >> "$OUTPUT_FILE"
            echo "$blockers" >> "$OUTPUT_FILE"
            blockers_found=true
        fi
    fi
done

if [ "$blockers_found" = false ]; then
    echo "No blockers. 🎉" >> "$OUTPUT_FILE"
fi

# 7. Next actions (from SESSION-CURRENT.md)
echo "" >> "$OUTPUT_FILE"
echo "## ⏭️  NEXT ACTIONS" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
if [ -f ~/workspace/SESSION-CURRENT.md ]; then
    sed -n '/## Next Actions/,/---/p' ~/workspace/SESSION-CURRENT.md | grep -E '^[0-9]\.' | head -3 >> "$OUTPUT_FILE" || echo "See SESSION-CURRENT.md for next actions" >> "$OUTPUT_FILE"
fi

# 8. Quick links
cat >> "$OUTPUT_FILE" << 'FOOTER'

---

## 📚 QUICK LINKS

- [SESSION-CURRENT.md](~/workspace/SESSION-CURRENT.md) - Today's work
- [ACTIVE-PROJECTS.md](~/workspace/ACTIVE-PROJECTS.md) - All active projects
- [SESSION-RECENT.md](~/workspace/SESSION-RECENT.md) - Last 7 days
- [MCP Quick Reference](~/workspace/MCP-QUICK-REF.md)

**To update this summary**: `~/workspace/scripts/refresh-context.sh`
FOOTER

# Output to console
cat "$OUTPUT_FILE"
echo ""
echo "✅ Context summary saved to: $OUTPUT_FILE"
