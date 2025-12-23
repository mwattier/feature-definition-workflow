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
```
VERIFICATION FAILED: Mismatch detected

Field: [field_name]
Expected (from [source]:[line]): [type/name]
Found (in [target]:[line]): [type/name]

Mismatch type: TYPE | NAME | NULLABILITY

Options:
A) Update source to match target
B) Update target to match source
C) Add explicit conversion
D) This is intentional (document why)

Action required: Human decision
```
**STOP** — Do not auto-resolve. Wait for human input.

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

If non-compliant:
```
NAMING VIOLATION: [field] does not follow [convention]

Location: [filepath]:[line]
Current: [current name]
Expected: [corrected name]

Action required: Fix naming before proceeding
```
**STOP** — This is not optional.

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

If non-compliant:
```
TYPE VIOLATION: [field] does not follow type convention

Location: [filepath]:[line]
Architecture rule: [rule from ARCHITECTURE.md]
Current: [current type]
Expected: [expected type]

Action required: Fix type before proceeding
```
**STOP** — This is not optional.

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
4. **Line numbers matter** — Always include them for re-verification
5. **Update checklist immediately** — Don't defer updates
