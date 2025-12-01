# Issue Tracker Integration

How to connect feature definitions to tracking systems for implementation management.

---

## The Handoff

After defining features conversationally and creating feature documents, you need to track implementation progress.

**Feature Definition** → **Tracking System**

This document explains the integration between feature documents and various tracking approaches.

---

## Tracking System Options

### Option 1: features.json (Recommended for AI Workflows)

**Best For**:
- AI-assisted development
- Solo developers
- Programmatic queries
- Structured progress tracking

**Structure**:
```json
{
  "project": "project-name",
  "features": [
    {
      "id": "F001",
      "name": "Feature name",
      "status": "in_progress",
      "progress": 60
    }
  ]
}
```

See [templates/features.json.example](./templates/features.json.example) for complete structure.

### Option 2: GitHub Issues

**Best For**:
- Team collaboration
- External contributors
- Discussion threads
- Public visibility

**Integration**:
- Create issue per feature
- Link to feature document
- Sync status bidirectionally

### Option 3: Jira/Linear/Other

**Best For**:
- Enterprise workflows
- Existing team processes
- Complex project management

**Integration**:
- Similar to GitHub Issues
- Use API for automation
- Maintain feature document as source of truth

### Option 4: Hybrid Approach

**Best For**:
- AI development + team collaboration
- features.json as internal state
- Issues for stakeholder visibility

---

## features.json Structure

### Basic Feature Entry

```json
{
  "id": "F001",
  "name": "User Authentication System",
  "description": "Implement secure user login and session management",
  "status": "pending",
  "priority": "critical",
  "progress": 0,
  "estimatedEffort": "medium",
  "definitionDoc": "docs/features/01-user-authentication.md",
  "dependencies": [],
  "blockers": [],
  "files": [],
  "tests": [],
  "acceptanceCriteria": [
    "Users can register with email/password",
    "Users can login and logout",
    "Sessions persist across browser restarts",
    "Password reset flow works"
  ],
  "subtasks": [
    {
      "id": "F001.1",
      "name": "Database schema for users and sessions",
      "status": "pending",
      "estimatedTime": "2h"
    },
    {
      "id": "F001.2",
      "name": "Password hashing implementation",
      "status": "pending",
      "estimatedTime": "1h"
    }
  ],
  "startedDate": null,
  "completedDate": null
}
```

### With External Tracker Integration

```json
{
  "id": "F001",
  "name": "User Authentication System",
  "externalTracking": {
    "system": "github",
    "issueNumber": 15,
    "issueUrl": "https://github.com/user/repo/issues/15",
    "issueState": "open",
    "lastSyncedAt": "2025-11-30T14:30:00Z"
  }
}
```

---

## Creating features.json from Feature Documents

### Step 1: Extract Core Information

From your feature document, extract:
- Feature ID and name
- Description/purpose
- Acceptance criteria
- Implementation subtasks
- Dependencies
- Priority

### Step 2: Create JSON Entry

**Example Feature Document**:
```markdown
# Feature: User Authentication System

**Priority**: Critical

## Purpose
Secure user login and session management

## Acceptance Criteria
- [ ] Users can register with email/password
- [ ] Users can login and logout
- [ ] Sessions persist across browser restarts

## Implementation Notes
1. Create database schema
2. Implement password hashing
3. Build session management
```

**Resulting JSON**:
```json
{
  "id": "F001",
  "name": "User Authentication System",
  "description": "Secure user login and session management",
  "status": "pending",
  "priority": "critical",
  "definitionDoc": "docs/features/01-user-authentication.md",
  "acceptanceCriteria": [
    "Users can register with email/password",
    "Users can login and logout",
    "Sessions persist across browser restarts"
  ],
  "subtasks": [
    {"id": "F001.1", "name": "Create database schema", "status": "pending"},
    {"id": "F001.2", "name": "Implement password hashing", "status": "pending"},
    {"id": "F001.3", "name": "Build session management", "status": "pending"}
  ]
}
```

### Step 3: Add to Hierarchical Structure

For large projects, nest within phases and epics:

```json
{
  "project": "project-name",
  "phases": [
    {
      "id": "P1",
      "name": "Phase 1 - Foundation",
      "epics": [
        {
          "id": "E1.1",
          "name": "User Management",
          "features": [
            {
              "id": "F001",
              "name": "User Authentication System"
            }
          ]
        }
      ]
    }
  ]
}
```

---

## Status Values

### Feature Status

- **pending**: Not started
- **in_progress**: Actively being worked on
- **blocked**: Waiting on dependency or blocker
- **completed**: All subtasks done, acceptance criteria met
- **descoped**: Removed from current scope

### Subtask Status

- **pending**: Not started
- **in_progress**: Currently working on
- **completed**: Done

---

## Progress Tracking

### Calculating Progress

```
Feature Progress = (completed subtasks / total subtasks) × 100
```

**Example**:
```json
{
  "id": "F001",
  "subtasks": [
    {"id": "F001.1", "status": "completed"},
    {"id": "F001.2", "status": "completed"},
    {"id": "F001.3", "status": "in_progress"},
    {"id": "F001.4", "status": "pending"}
  ],
  "progress": 50
}
```

2 of 4 complete = 50% progress

### Hierarchical Rollup

```
Epic Progress = average(Feature Progress)
Phase Progress = average(Epic Progress)
Project Progress = average(Phase Progress)
```

---

## Integration Patterns

### Pattern 1: features.json Only

**Workflow**:
1. Define feature conversationally
2. Create feature document
3. Extract to features.json
4. Track progress in JSON
5. Update JSON as work progresses

**Pros**:
- Simple, no external dependencies
- Programmatic queries easy
- AI-friendly structure

**Cons**:
- No collaboration features
- No external visibility
- Manual progress updates

### Pattern 2: features.json + GitHub Issues

**Workflow**:
1. Define feature conversationally
2. Create feature document
3. Extract to features.json
4. Create GitHub issue from JSON
5. Link issue number in JSON
6. Sync status bidirectionally

**Pros**:
- Best of both worlds
- Collaboration + AI workflows
- Discussion threads available

**Cons**:
- More complexity
- Sync overhead
- Potential inconsistency

### Pattern 3: Feature Documents Only

**Workflow**:
1. Define feature conversationally
2. Create feature document
3. Update document status manually
4. No structured tracking

**Pros**:
- Simplest approach
- No additional tooling

**Cons**:
- Hard to query
- No programmatic progress
- Manual aggregation needed

---

## Automation Scripts

### Create Issue from Feature

**GitHub Example**:
```bash
#!/bin/bash
# Create GitHub issue from features.json entry

FEATURE_ID=$1

# Extract feature from JSON
FEATURE=$(jq -r ".features[] | select(.id == \"$FEATURE_ID\")" features.json)

NAME=$(echo "$FEATURE" | jq -r '.name')
DESC=$(echo "$FEATURE" | jq -r '.description')
PRIORITY=$(echo "$FEATURE" | jq -r '.priority')

# Create issue
gh issue create \
  --title "[$FEATURE_ID] $NAME" \
  --body "$DESC

## Acceptance Criteria
$(echo "$FEATURE" | jq -r '.acceptanceCriteria[]' | sed 's/^/- [ ] /')

## Feature Document
See: $(echo "$FEATURE" | jq -r '.definitionDoc')
" \
  --label "feature" \
  --label "priority:$PRIORITY"
```

### Update Progress

**Simple Update**:
```bash
#!/bin/bash
# Update feature progress in features.json

FEATURE_ID=$1
NEW_STATUS=$2

jq --arg fid "$FEATURE_ID" --arg status "$NEW_STATUS" \
  '(.features[] | select(.id == $fid) | .status) = $status' \
  features.json > features.json.tmp

mv features.json.tmp features.json
```

---

## Best Practices

### 1. Feature Document is Source of Truth

- Specification lives in feature document
- JSON tracks implementation status
- Issues provide collaboration layer

### 2. Link Everything

- JSON references feature document
- Issues reference feature document
- Feature document references JSON/issue

**Example Feature Document**:
```markdown
# Feature: User Authentication System

**Status**: In Progress
**Tracking**: F001 in features.json
**Issue**: #15
```

### 3. Sync Regularly

- Update JSON when subtasks complete
- Sync to issues daily/weekly
- Keep status current

### 4. Document Changes

Track scope changes in JSON:

```json
{
  "id": "F001",
  "scopeChanges": [
    {
      "date": "2025-12-01",
      "change": "Added OAuth support",
      "rationale": "User request for Google login"
    }
  ]
}
```

### 5. Handle Blockers Explicitly

```json
{
  "id": "F001",
  "status": "blocked",
  "blockers": [
    {
      "id": "B001",
      "description": "Waiting on API keys from provider",
      "createdDate": "2025-11-30",
      "resolution": null
    }
  ]
}
```

---

## Example: Complete Workflow

### 1. Feature Definition

Conversational process creates:
`docs/features/01-user-authentication.md`

### 2. Create features.json Entry

```json
{
  "id": "F001",
  "name": "User Authentication System",
  "status": "pending",
  "definitionDoc": "docs/features/01-user-authentication.md",
  "subtasks": [...]
}
```

### 3. Create GitHub Issue (Optional)

```bash
./scripts/create-issue.sh F001
# Creates issue #15
```

### 4. Link Issue in JSON

```json
{
  "id": "F001",
  "externalTracking": {
    "system": "github",
    "issueNumber": 15
  }
}
```

### 5. Implementation

Work on subtasks, updating JSON:

```json
{
  "id": "F001",
  "status": "in_progress",
  "progress": 60,
  "subtasks": [
    {"id": "F001.1", "status": "completed"},
    {"id": "F001.2", "status": "completed"},
    {"id": "F001.3", "status": "in_progress"}
  ]
}
```

### 6. Sync to Issue

```bash
./scripts/sync-status.sh
# Updates issue #15 with progress comment
```

### 7. Completion

```json
{
  "id": "F001",
  "status": "completed",
  "progress": 100,
  "completedDate": "2025-12-05"
}
```

Close GitHub issue with completion comment.

---

## Tool-Specific Integration

### GitHub

- Use `gh` CLI for automation
- Create issues with templates
- Sync using GitHub API
- Project boards for visualization

### Jira

- Use Jira REST API
- Map features to stories
- Epics map to Jira epics
- Use Jira workflows

### Linear

- Use Linear API/SDK
- Map to Linear issues
- Projects map to projects
- Cycles for sprint planning

### Your Own System

- Build custom integration
- Use features.json as data source
- Implement sync as needed
- Maintain feature documents as spec

---

## Next Steps

1. **Choose your tracking approach**
2. **Set up features.json** (see [templates/features.json.example](./templates/features.json.example))
3. **Create integration scripts** (if using external tracker)
4. **Define first feature**
5. **Create tracking entry**
6. **Start implementation**

---

## Related Documentation

- [01-METHODOLOGY.md](./01-METHODOLOGY.md) - Feature definition process
- [03-PROJECT-BREAKDOWN.md](./03-PROJECT-BREAKDOWN.md) - Large project decomposition
- [templates/features.json.example](./templates/features.json.example) - Complete example
- [templates/features.schema.json](./templates/features.schema.json) - JSON schema

---

**Remember**: The tracking system serves the feature definition, not the other way around. Start with clear specifications, then choose tracking that fits your workflow.
