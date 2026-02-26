# Verify File

**Usage**: `/verify-file [filepath]`

Verify a specific file before or after implementation. This is a rigid verification process — follow each step exactly.

---

## Pre-Verification Check

Before verifying this file:

1. **Find the feature** — Which feature does this file belong to?
2. **Load verification checklist** — Read `verification/[feature-id].md`
3. **Check dependencies** — Are all files this one depends on already VERIFIED?

If dependencies are not VERIFIED:
```
BLOCKED: Cannot verify [filepath]

Reason: Dependencies not yet verified
- [ ] [dependency-file] — Status: [status]
- [ ] [dependency-file] — Status: [status]

Verify dependencies first, in order.
```
**STOP** — Do not proceed.

---

## Step 1: Read Dependency Files

For each file this one depends on, read the file completely.

List what you found:
```
Dependency: [filepath]
Fields/Types defined:
| Field | Type | Line |
|-------|------|------|
| [copy exactly] | [copy exactly] | [number] |
```

**Rule**: Copy-paste field names and types. Do not type from memory.

---

## Step 2: Read Target File

If file exists (MODIFIED), read it completely.
If file doesn't exist yet (NEW), note that implementation is pending.

For existing files, extract:
```
Target: [filepath]
Fields/Types used:
| Field | Type Used | Line | Source Expected |
|-------|-----------|------|-----------------|
| [copy exactly] | [copy exactly] | [number] | [which dependency] |
```

---

## Step 3: Field-by-Field Verification

For each field used in the target file, verify against source:

```
Verifying: [field_name]
- Target file: [filepath]:[line] 
- Target type: [type as written]
- Source file: [source filepath]:[line]
- Source type: [type as written]
- Match: ✓ EXACT | ⚠ MISMATCH | ? NOT FOUND
```

### If EXACT Match
Continue to next field.

### If MISMATCH

Classify severity first:

**Critical (STOP)** — Type mismatches, missing required fields, wrong nullability:
```
VERIFICATION FAILED [CRITICAL]: Mismatch detected

Field: [field_name]
Expected (from [source]:[line]): [type/name]
Found (in [target]:[line]): [type/name]

Severity: CRITICAL — affects runtime correctness
Mismatch type: TYPE | NULLABILITY | MISSING_FIELD

Options:
A) Update source to match target
B) Update target to match source
C) Add explicit conversion
D) This is intentional (document why)

Action required: Human decision
```
**STOP** — Do not auto-resolve. Wait for human input.

**Warning (FLAG)** — Naming convention violations, style inconsistencies:
```
VERIFICATION WARNING [WARNING]: Convention violation

Field: [field_name]
Expected (from ARCHITECTURE.md): [convention]
Found (in [target]:[line]): [actual]

Severity: WARNING — convention violation, not a runtime error
Proposed fix: [specific fix]

Proceeding with proposed fix unless you object.
```
Continue with proposed fix. Log in verification checklist.

### If NOT FOUND
```
VERIFICATION WARNING: Field not found in source

Field: [field_name] used at [target]:[line]
Expected source: [expected source file]
Searched: [list files searched]

Possible issues:
- Field name misspelled
- Wrong source file assumed
- Field needs to be added to source

Action required: Human clarification
```
**STOP** — Wait for human input.

---

## Step 4: Verify Naming Convention

Check each field name against ARCHITECTURE.md naming conventions:

```
Convention check: [which convention from ARCHITECTURE.md]
| Field | Convention | Compliant |
|-------|------------|-----------|
| product_id | snake_case | ✓ |
| ProductName | snake_case | ✗ — should be product_name |
```

If non-compliant (Warning severity — flag and propose fix):
```
NAMING VIOLATION [WARNING]: [field] does not follow [convention]

Location: [filepath]:[line]
Current: [current name]
Expected: [corrected name]

Proposed fix: Rename to [corrected name]
Proceeding with fix unless you object.
```

---

## Step 5: Verify Type Convention

Check types against ARCHITECTURE.md type conventions:

```
Type convention check:
| Usage | Expected Type | Actual Type | Compliant |
|-------|---------------|-------------|-----------|
| Identifier | UUID | UUID | ✓ |
| Timestamp | datetime | str | ✗ |
```

If non-compliant (Critical severity — type mismatches affect correctness):
```
TYPE VIOLATION [CRITICAL]: [field] does not follow type convention

Location: [filepath]:[line]
Architecture rule: [rule from ARCHITECTURE.md]
Current: [current type]
Expected: [expected type]

Action required: Human decision needed
```
**STOP** — Type mismatches are Critical severity. Do not auto-resolve.

---

## Step 6: Update Verification Checklist

Open `verification/[feature-id].md` and update:

1. **File status**: PENDING → VERIFIED (or BLOCKED if issues)
2. **Field mapping table**: Fill in all verified fields
3. **Verification log**: Add timestamped entry
4. **Verified by**: Claude
5. **Timestamp**: Current time

---

## Step 7: Update features.json

Update the file's verification status:

```json
{
  "path": "[filepath]",
  "depends_on": ["..."],
  "verification_status": "VERIFIED",
  "verified_at": "[timestamp]"
}
```

---

## Output Format

### Success
```
/verify-file [filepath] — VERIFIED

Dependency files checked: [count]
Fields verified: [count]
Naming convention: ✓ Compliant
Type convention: ✓ Compliant

Updated: verification/[feature-id].md
Updated: features.json

Next file in dependency order: [filepath] (or "All dependencies satisfied")
```

### Blocked
```
/verify-file [filepath] — BLOCKED

Issue: [TYPE_MISMATCH | NAME_MISMATCH | NOT_FOUND | CONVENTION_VIOLATION]

Details:
[specific details]

Options presented to human. Awaiting decision.
```

---

## Critical Rules

1. **Never skip a field** — Every field must be verified
2. **Never auto-resolve mismatches** — Always ask human
3. **Copy, don't type** — Field names and types are copy-pasted
4. **Anchor to names, not just lines** — Reference function/class/type names alongside line numbers (line numbers shift as code changes)
5. **Update checklist immediately** — Don't defer updates
