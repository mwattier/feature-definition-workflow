# Continue from Checkpoint

**Usage**: `/continue [checkpoint-file]` or `/continue` (uses most recent)

Resume work from a saved checkpoint. This restores context and guides the session to pick up where previous work stopped.

---

## Without Checkpoint File

If no file specified, find most recent:

1. Read `features.json`
2. Find features with status `in-progress`
3. Get `current_checkpoint` from each
4. Use most recently created checkpoint

```
No checkpoint specified. Found most recent:
→ checkpoints/product-normalization-20251222-1430.md

Loading this checkpoint. Specify a different file if needed:
/continue checkpoints/[other-file].md
```

---

## Step 1: Load Checkpoint

Read the checkpoint file completely.

Extract:
- Feature ID
- What's complete
- What's in progress
- What's remaining
- Key decisions
- Issues encountered
- Next steps

---

## Step 2: Verify Current State

Check if state has changed since checkpoint:

### Check features.json
```
Checkpoint says: [state from checkpoint]
features.json says: [current state]
Match: ✓ / ✗
```

### Check verification status
```
Checkpoint says: [verification state]
Verification checklist says: [current state]  
Match: ✓ / ✗
```

### Check files exist
```
Files mentioned in checkpoint:
- [file] — Exists: ✓ / ✗
- [file] — Exists: ✓ / ✗
```

### If State Mismatch

```
⚠ State has changed since checkpoint

Checkpoint (created [timestamp]):
- [file]: [checkpoint status]

Current:
- [file]: [current status]

Changes detected:
- [description of what changed]

Options:
A) Continue with current state (checkpoint as reference only)
B) Investigate changes before continuing
C) Load a different checkpoint

Which would you like?
```

Wait for human decision.

---

## Step 3: Load Supporting Context

Read in order:
1. `ARCHITECTURE.md` — Refresh system context
2. `features.json` — Current feature state
3. `verification/[feature-id].md` — Current verification state
4. Any decision logs referenced in checkpoint

---

## Step 4: Present Restoration Summary

```
Resuming from Checkpoint
========================

Feature: [feature-id]
Checkpoint: [filename]
Created: [timestamp]

Progress:
├── Complete: [count] files
├── In Progress: [file being worked on]
└── Remaining: [count] files

Key Context:
- [Decision or context point 1]
- [Decision or context point 2]
- [Issue or note from checkpoint]

Verification Status:
- Verified: [count]
- Pending: [count]
- Blocked: [count or "None"]

Next Steps (from checkpoint):
1. [First step]
2. [Second step]
3. [Third step]

Ready to continue. What would you like to do?
```

---

## Step 5: Confirm Understanding

Before proceeding, verify understanding:

```
Confirming I understand the current state:

I was working on: [file/task]
I stopped at: [where in the work]
The next thing to do is: [next step]

Is this correct? 
[If anything is wrong, please clarify]
```

Wait for human confirmation or correction.

---

## Step 6: Resume Work

Once confirmed, present options:

```
Ready to continue. Options:

1. Continue where I left off
   → [specific task from checkpoint]

2. Check verification status first
   → /verification-status [feature-id]

3. Re-verify a file before continuing
   → /verify-file [filepath]

4. Review the full checkpoint
   → [show checkpoint contents]

5. Something else
   → [describe what you'd like to do]
```

---

## Handling Stale Checkpoints

If checkpoint is old (>7 days) or for a completed feature:

```
⚠ Checkpoint may be stale

Checkpoint created: [timestamp] ([X days ago])
Feature status: [current status]

This checkpoint may not reflect current state accurately.

Recommendations:
- If feature is complete: This checkpoint is historical reference only
- If feature is in-progress: Verify current state before resuming
- If feature was restarted: Create fresh checkpoint

Continue anyway? Or investigate current state first?
```

---

## Quick Resume

For fast resumption when context is clear:

```
/continue

→ Loading: checkpoints/product-normalization-20251222-1430.md
→ Feature: product-normalization (2/5 files complete)
→ Last working on: services/reader.py line 45
→ Next step: Continue implementing load_product()

Continuing...
```

---

## If No Checkpoints Exist

```
No checkpoints found.

To create a checkpoint: /checkpoint [description]

To start fresh on a feature: /pre-implement [feature-id]

Current in-progress features:
- [feature-id]: [brief status]
- [feature-id]: [brief status]
```

---

## Checkpoint Navigation

List available checkpoints:
```
/continue --list

Available checkpoints:
| Feature | Checkpoint | Created | Summary |
|---------|------------|---------|---------|
| product-normalization | ...1430.md | 2025-12-22 14:30 | Completed writer |
| product-normalization | ...1200.md | 2025-12-22 12:00 | Started schema |
| company-sync | ...0900.md | 2025-12-22 09:00 | Initial setup |

To load: /continue checkpoints/[filename].md
```
