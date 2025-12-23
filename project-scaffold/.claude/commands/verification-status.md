# Verification Status

**Usage**: `/verification-status` or `/verification-status [feature-id]`

Display current verification status for active feature or specified feature.

---

## Without Feature ID

Show status for currently active work:

1. Check `features.json` for features with status `in-progress`
2. For each in-progress feature, show verification state

```
Active Features Verification Status
===================================

Feature: [feature-id]
Title: [title]
Overall: [PENDING | IN_PROGRESS | VERIFIED | BLOCKED]

Files:
| File | Status | Dependencies Satisfied |
|------|--------|------------------------|
| [path] | VERIFIED | ✓ |
| [path] | PENDING | ✓ |
| [path] | PENDING | ✗ (waiting on [file]) |

Progress: [verified]/[total] files ([percentage]%)

---

[Repeat for each in-progress feature]
```

---

## With Feature ID

Show detailed status for specific feature:

```
Verification Status: [feature-id]
=================================

Feature: [title]
Status: [status]
Last Updated: [timestamp]

Files (in dependency order):
┌─────────────────────────────────────────────────────────────────┐
│ # │ File                    │ Status   │ Depends On │ Blocks   │
├───┼─────────────────────────┼──────────┼────────────┼──────────┤
│ 1 │ schema/product.py       │ VERIFIED │ —          │ #2, #3   │
│ 2 │ services/writer.py      │ VERIFIED │ #1         │ #3       │
│ 3 │ services/reader.py      │ PENDING  │ #1, #2     │ —        │
└───┴─────────────────────────┴──────────┴────────────┴──────────┘

Cross-File Verification:
| Interface | Status |
|-----------|--------|
| reader.py → writer.py | PENDING |

Blocking Issues: [count]
[List any blocking issues]

Next Action:
→ [What should be done next]
```

---

## Status Indicators

```
VERIFIED     ✓  All checks passed, implementation matches spec
PENDING      ○  Not yet verified
IN_PROGRESS  ◐  Verification started but not complete  
BLOCKED      ✗  Issue found, requires resolution
N/A          —  Not applicable (no dependencies)
```

---

## Quick Status (One-liner)

For fast status check in conversation:

```
[feature-id]: [verified]/[total] files, [status]
```

Example:
```
product-normalization: 2/5 files, IN_PROGRESS
company-sync: 4/4 files, VERIFIED
```

---

## When Status Is BLOCKED

If any feature is blocked, prominently display:

```
⚠ BLOCKED: [feature-id]

Blocking Issue:
[Description of what's blocking]

Location: [file:line or verification checklist reference]

Resolution Required:
[What needs to happen to unblock]

This feature cannot proceed until the blocking issue is resolved.
```

---

## Recommended Next Actions

Based on status, suggest next steps:

### If All PENDING
```
Next: Run /pre-implement [feature-id] to set up verification
```

### If IN_PROGRESS
```
Next: Run /verify-file [first-pending-file] to continue verification
```

### If BLOCKED  
```
Next: Resolve blocking issue, then re-run /verify-file [blocked-file]
```

### If All VERIFIED
```
Next: Run /verify-feature [feature-id] for final cross-file checks
      Then update feature status to complete
```
