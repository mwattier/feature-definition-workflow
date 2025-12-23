# Checkpoint

**Usage**: `/checkpoint [brief description]`

Save current implementation progress to a checkpoint file. Use this to preserve context before session limits, complex changes, or end of work session.

---

## When to Create Checkpoints

Create a checkpoint:
- Before starting a complex or risky file
- After completing each file in a multi-file feature
- When conversation is getting long (approaching context limits)
- Before any significant refactoring
- At end of work session
- Before switching to a different feature
- When human requests it

---

## Checkpoint Contents

The checkpoint captures current state so a new session can resume effectively.

### Required Sections

```markdown
# Checkpoint: [feature-id] — [brief description]

> Created: [timestamp]
> Session: [session identifier if available]
> Feature: [feature-id]

## Current State

### What's Complete
[List completed files with verification status]

### What's In Progress  
[Current file being worked on, where you stopped]

### What's Remaining
[Files not yet started]

## Implementation Context

### Key Decisions Made This Session
[Decisions that affect remaining work]

### Issues Encountered
[Problems found and their resolutions, or unresolved issues]

### Dependencies Discovered
[Any new dependencies found during implementation]

## Verification State

### Files Verified
[List with status]

### Pending Verifications
[What still needs verification]

### Blocking Issues
[Any blockers, or "None"]

## Code Context

### Recently Modified Files
[List of files touched this session with brief change summary]

### Uncommitted Changes
[Summary of changes not yet committed]

### Tests Status
[Pass/fail status if tests were run]

## Next Steps

When resuming:
1. [First thing to do]
2. [Second thing to do]
3. [Continue with...]

## Notes for Next Session

[Anything the next session needs to know that doesn't fit above]
[Human preferences expressed during session]
[Clarifications received]
```

---

## Creating the Checkpoint

### Step 1: Gather State

Collect:
- Current feature from features.json
- Verification status from checklist
- Git status (if available)
- Recent conversation context

### Step 2: Write Checkpoint File

Location: `checkpoints/[feature-id]-[YYYYMMDD]-[HHMM].md`

Example: `checkpoints/product-normalization-20251222-1430.md`

### Step 3: Update features.json

```json
{
  "id": "[feature-id]",
  "checkpoints": [
    {
      "timestamp": "[ISO timestamp]",
      "file": "checkpoints/[filename].md",
      "summary": "[brief description provided by user]"
    }
  ],
  "current_checkpoint": "checkpoints/[filename].md"
}
```

### Step 4: Confirm Creation

```
Checkpoint created: checkpoints/[filename].md

Summary:
- Feature: [feature-id]
- Files complete: [count]
- Files remaining: [count]  
- Verification: [status]
- Next step: [what to do when resuming]

To resume: /continue checkpoints/[filename].md
```

---

## Checkpoint Quality

A good checkpoint allows someone (Claude or human) to resume work without needing the previous conversation.

### Test: Could a New Session Resume?

The checkpoint should answer:
- What feature is being worked on?
- What's done and what's not?
- What was I doing when I stopped?
- What decisions have been made?
- What should I do next?

If any of these are unclear, add more detail.

---

## Automatic Checkpoint Triggers

Claude should proactively suggest checkpoints when:

```
Context getting long — suggest checkpoint
"We've made significant progress on [feature]. 
Would you like me to create a checkpoint before continuing?"

Before risky change — suggest checkpoint  
"I'm about to refactor [file]. 
Should I checkpoint current state first?"

Session ending signals — suggest checkpoint
"Before we wrap up, let me create a checkpoint 
so we can resume smoothly next time."
```

---

## Checkpoint Hygiene

### Keep Recent Checkpoints
Retain last 3-5 checkpoints per feature for rollback capability.

### Archive on Feature Complete
When feature is marked complete, move checkpoints to `checkpoints/archive/[feature-id]/`

### Delete Stale Checkpoints
Checkpoints older than 30 days for completed features can be deleted.

---

## Example Checkpoint

```markdown
# Checkpoint: product-normalization — Completed writer service

> Created: 2025-12-22T14:30:00Z
> Feature: product-normalization

## Current State

### What's Complete
- [x] schema/product.py — VERIFIED
- [x] services/writer.py — VERIFIED

### What's In Progress
- services/reader.py — Started, implementing load_product()

### What's Remaining
- tests/test_reader.py
- api/product_routes.py

## Implementation Context

### Key Decisions Made This Session
- Used UUID for product_id (see decisions/2025-12-22-uuid-identifiers.md)
- Writer uses batch inserts for performance

### Issues Encountered
- Initially had type mismatch on created_at (str vs datetime)
- Resolved: Updated writer to use datetime, matching schema

### Dependencies Discovered
- reader.py needs writer.py's ProductBatch type for bulk operations

## Verification State

### Files Verified
- schema/product.py — VERIFIED
- services/writer.py — VERIFIED

### Pending Verifications  
- services/reader.py — PENDING (in progress)

### Blocking Issues
None

## Code Context

### Recently Modified Files
- services/writer.py — Implemented save_product(), batch_save()
- schema/product.py — Added ProductBatch type

### Uncommitted Changes
- services/writer.py (new file)
- schema/product.py (modified)

### Tests Status
Not yet run (reader not complete)

## Next Steps

When resuming:
1. Read this checkpoint
2. Open services/reader.py  
3. Continue implementing load_product() from line 45
4. Then implement batch_load()
5. Run /verify-file services/reader.py

## Notes for Next Session

Mike prefers explicit type hints on all function parameters.
Batch size should be configurable via environment variable.
```
