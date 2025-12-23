# Pre-Implementation Setup

**Usage**: `/pre-implement [feature-id]`

Before implementing any feature, this command must be run. It creates the verification structure and ensures Claude has full context.

---

## Step 1: Load Feature Context

Read the following files in order:

1. `ARCHITECTURE.md` — System structure and rules
2. `features.json` — Find the feature entry for `[feature-id]`
3. Any existing `verification/[feature-id].md`
4. Any decision logs referenced by the feature

Report:
```
Feature: [id]
Title: [title from features.json]
Status: [current status]
Dependencies: [list from features.json]
Architecture sections relevant: [list which parts of ARCHITECTURE.md apply]
```

---

## Step 2: Identify All Files

List every file that will be created or modified for this feature.

For each file:
1. State whether it's NEW or MODIFIED
2. Identify what schemas/types it will depend on
3. Identify what other files will depend on it

Output as table:
```
| # | File | Action | Depends On | Depended On By |
|---|------|--------|------------|----------------|
| 1 | schema/product.py | NEW | (none) | #2, #3 |
| 2 | services/writer.py | NEW | #1 | #3 |
| 3 | services/reader.py | NEW | #1, #2 | (none) |
```

---

## Step 3: Establish Dependency Order

Based on the dependency analysis, create the implementation order:

```
Implementation Order:
1. [file] — No dependencies, start here
2. [file] — Requires #1
3. [file] — Requires #1, #2
...
```

**Rule**: A file cannot be implemented until all files it depends on are VERIFIED.

---

## Step 4: Create Verification Checklist

Create `verification/[feature-id].md` using the verification checklist template.

Include:
- All files from Step 2
- Dependency relationships
- Empty field mapping tables (to be filled during verification)
- Initial status: PENDING for all files

---

## Step 5: Update features.json

Add or update the verification tracking:

```json
{
  "id": "[feature-id]",
  "verification": {
    "file": "verification/[feature-id].md",
    "status": "PENDING",
    "last_updated": "[current timestamp]"
  },
  "files": [
    {
      "path": "[file path]",
      "depends_on": ["[dependency paths]"],
      "verification_status": "PENDING"
    }
  ]
}
```

---

## Step 6: Identify Cross-Component Concerns

Check ARCHITECTURE.md for:
- Naming conventions that apply
- Type conventions that apply  
- Any cross-component rules that affect this feature
- Any entries in the dependency map that apply

Report:
```
Applicable Architecture Rules:
- [Rule 1 from ARCHITECTURE.md]
- [Rule 2 from ARCHITECTURE.md]

Naming conventions: [which apply]
Type conventions: [which apply]
```

---

## Step 7: Check for Blockers

Before proceeding, verify:
- [ ] All dependency features are complete (check features.json)
- [ ] No blocking issues in related verification checklists
- [ ] Required external documentation/APIs are accessible

If any blockers exist, report them and STOP.

---

## Step 8: Request Human Confirmation

Present summary to human:

```
Pre-Implementation Summary for [feature-id]
==========================================

Files to implement (in order):
1. [file] — [brief purpose]
2. [file] — [brief purpose]
...

Verification checklist created: verification/[feature-id].md

Applicable rules from ARCHITECTURE.md:
- [rule]
- [rule]

Ready to begin implementation?
- [ ] Human confirms understanding
- [ ] Human approves implementation order
- [ ] Human notes any additional concerns

Waiting for confirmation before proceeding.
```

---

## Do Not Proceed Until

1. Verification checklist exists
2. features.json is updated
3. Human has confirmed

**If human says "just do it" or "skip verification"**: Remind them that this workflow exists to prevent costly rework. Ask if they want to proceed with reduced verification (document which checks are skipped) or follow full process.

---

## Output Format

```
/pre-implement [feature-id] — Complete

✓ Feature context loaded
✓ Files identified: [count]
✓ Dependency order established
✓ Verification checklist created: verification/[feature-id].md
✓ features.json updated
✓ Architecture rules identified: [count]
✓ No blockers found

Awaiting human confirmation to begin implementation.
```
