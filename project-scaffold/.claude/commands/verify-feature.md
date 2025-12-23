# Verify Feature

**Usage**: `/verify-feature [feature-id]`

Run complete verification for all files in a feature. This includes per-file verification and cross-file interface verification.

---

## Step 1: Load Feature State

Read:
1. `features.json` — Get feature entry
2. `verification/[feature-id].md` — Get current checklist
3. `ARCHITECTURE.md` — Get applicable rules

Report current state:
```
Feature: [feature-id]
Title: [title]
Total files: [count]
Verified: [count]
Pending: [count]
Blocked: [count]
```

---

## Step 2: Check Individual File Status

For each file in the feature:

| File | Status | Last Verified |
|------|--------|---------------|
| [path] | [status] | [timestamp or "—"] |

### If Any Files Are PENDING

```
Pending files must be verified first:
1. [filepath] — Run: /verify-file [filepath]
2. [filepath] — Run: /verify-file [filepath]

Complete individual file verification before running /verify-feature
```

### If Any Files Are BLOCKED

```
Blocked files prevent feature verification:

[filepath] — BLOCKED
Issue: [issue from checklist]
Resolution required before proceeding.

Cannot complete feature verification until blocks are resolved.
```
**STOP** — Report blockers and wait.

---

## Step 3: Cross-File Interface Verification

For each pair of files where one calls/imports the other:

### 3.1 Identify Interfaces

```
Cross-file interfaces found:
| Caller | Callee | Interface Type |
|--------|--------|----------------|
| reader.py:load_product() | writer.py:save_product() | Function call |
| api/routes.py | services/product.py | Import |
| services/sync.py | schema/product.py | Type reference |
```

### 3.2 Verify Each Interface

For each interface:

```
Interface: [caller] → [callee]

Caller expects:
- Function: [function name]
- Parameters: [list with types]
- Return type: [type]
- Location: [file:line]

Callee provides:
- Function: [function name]
- Parameters: [list with types]  
- Return type: [type]
- Location: [file:line]

Match: ✓ EXACT | ⚠ MISMATCH
```

### If Interface Mismatch

```
INTERFACE MISMATCH DETECTED

Caller: [file:line]
  Expects: [what caller expects]

Callee: [file:line]
  Provides: [what callee provides]

Mismatch: [specific difference]

Options:
A) Update caller to match callee
B) Update callee to match caller
C) Add adapter/conversion layer

Action required: Human decision
```
**STOP** — Do not auto-resolve.

---

## Step 4: Verify External Interfaces

If the feature integrates with external systems (APIs, databases, etc.):

```
External interface: [system name]

Expected (from documentation/schema):
| Field | Type | Required |
|-------|------|----------|
| [copy from external docs] | | |

Implemented:
| Field | Type | Required | Matches |
|-------|------|----------|---------|
| [copy from code] | | | ✓ / ✗ |
```

### If External Interface Mismatch

```
EXTERNAL INTERFACE MISMATCH

System: [external system]
Documentation: [link/reference]

Expected: [what external system expects]
Implemented: [what code does]

This may cause runtime failures.

Action required: Verify against external documentation
```
**STOP** — This requires human verification.

---

## Step 5: Run Available Automated Checks

If the project has automated tooling:

```
Running automated checks...

Type checker (mypy/pyright):
[output or "Not configured"]

Linter (ruff/flake8/eslint):
[output or "Not configured"]

Tests:
[output or "Not configured"]
```

### If Automated Checks Fail

```
AUTOMATED CHECK FAILED

Tool: [tool name]
Error:
[error output]

This must be resolved before feature verification is complete.
```
Do not mark feature as VERIFIED if automated checks fail.

---

## Step 6: Update Verification Checklist

Update `verification/[feature-id].md`:

1. **Overall status**: IN_PROGRESS → VERIFIED (or BLOCKED)
2. **Cross-file verification section**: Fill in all interface checks
3. **Sign-off checklist**: Check completed items
4. **Verification log**: Add completion entry

---

## Step 7: Update features.json

```json
{
  "id": "[feature-id]",
  "verification": {
    "file": "verification/[feature-id].md",
    "status": "VERIFIED",
    "last_updated": "[timestamp]",
    "files_verified": [total],
    "files_total": [total],
    "blocking_issues": 0
  }
}
```

---

## Step 8: Final Report

### Success

```
/verify-feature [feature-id] — VERIFIED

Summary:
├── Files: [count]/[count] verified
├── Cross-file interfaces: [count] verified
├── External interfaces: [count] verified
├── Naming conventions: ✓ Compliant
├── Type conventions: ✓ Compliant
├── Automated checks: ✓ Passed (or "N/A")
└── Status: VERIFIED

Updated: verification/[feature-id].md
Updated: features.json

Feature is ready for deployment/merge.
```

### Partial / Blocked

```
/verify-feature [feature-id] — INCOMPLETE

Summary:
├── Files: [verified]/[total] verified
├── Blocked files: [count]
├── Pending interfaces: [count]
└── Status: [IN_PROGRESS | BLOCKED]

Issues requiring resolution:
1. [issue description]
2. [issue description]

Cannot mark feature as VERIFIED until issues are resolved.
```

---

## Verification Completeness Checklist

Before marking VERIFIED, confirm:

- [ ] All files have status VERIFIED
- [ ] All cross-file interfaces verified
- [ ] All external interfaces verified  
- [ ] Naming conventions followed
- [ ] Type conventions followed
- [ ] Automated checks pass (if configured)
- [ ] No open issues in verification checklist

If ANY item is unchecked, feature is NOT VERIFIED.
