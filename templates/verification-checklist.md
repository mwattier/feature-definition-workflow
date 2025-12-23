# Verification Checklist Template

This template is used to create verification checklists for each feature. The checklist tracks per-file verification status and ensures dependencies are verified in the correct order.

---

## Template

Create this file at `verification/[feature-id].md`:

```markdown
# Verification: [feature-id]

> **Feature**: [Feature title from features.json]
> **Created**: [YYYY-MM-DD]
> **Last Updated**: [YYYY-MM-DD]

## Status: PENDING | IN_PROGRESS | VERIFIED | BLOCKED

## Files

| # | File | Depends On | Status | Verified By | Timestamp |
|---|------|------------|--------|-------------|-----------|
| 1 | [path/to/file.py] | (none) | PENDING | — | — |
| 2 | [path/to/other.py] | #1 | PENDING | — | — |
| 3 | [path/to/another.py] | #1, #2 | PENDING | — | — |

### Dependency Order

Files must be implemented and verified in this order:
1. [file.py] — No dependencies, can start immediately
2. [other.py] — Requires #1 to be VERIFIED
3. [another.py] — Requires #1 and #2 to be VERIFIED

---

## Field Mappings

### [File 1: path/to/file.py]

**Dependencies**: None

**Schema/Type Definitions**:
| Field | Type | Line | Notes |
|-------|------|------|-------|
| | | | |

**Status**: PENDING | VERIFIED | NOT_APPLICABLE

---

### [File 2: path/to/other.py]

**Dependencies**: path/to/file.py

**Fields Used From Dependencies**:
| Field | Expected Type | Source File | Source Line | Matches |
|-------|---------------|-------------|-------------|---------|
| | | | | ☐ |

**New Fields Defined**:
| Field | Type | Line | Notes |
|-------|------|------|-------|
| | | | |

**Status**: PENDING | VERIFIED | NOT_APPLICABLE

---

### [File 3: path/to/another.py]

**Dependencies**: path/to/file.py, path/to/other.py

**Fields Used From Dependencies**:
| Field | Expected Type | Source File | Source Line | Matches |
|-------|---------------|-------------|-------------|---------|
| | | | | ☐ |

**Status**: PENDING | VERIFIED | NOT_APPLICABLE

---

## Cross-File Verification

| Caller | Callee | Interface/Contract | Status |
|--------|--------|-------------------|--------|
| [file:function()] | [file:function()] | [params/return type] | PENDING |

---

## External Interfaces

| External System | Interface Point | Contract | Verified Against |
|-----------------|-----------------|----------|------------------|
| [HubSpot/Shopware/etc.] | [endpoint/table] | [expected format] | [doc/schema link] |

---

## Issues Found

### Open Issues
- [ ] [Issue description]

### Resolved Issues
- [x] [Issue description] — [Resolution]

---

## Sign-Off

### Automated Checks
- [ ] Type checker passes (mypy/pyright)
- [ ] Linter passes
- [ ] Tests pass

### Manual Verification
- [ ] All files status = VERIFIED
- [ ] All cross-file checks status = VERIFIED
- [ ] Dependency order was followed

### Human Review
- [ ] Required: [Yes/No]
- [ ] Completed: [date] by [name]
- [ ] Notes: [any review notes]

---

## Verification Log

| Timestamp | Action | Details |
|-----------|--------|---------|
| [datetime] | Created checklist | [files identified] |
| [datetime] | Verified [file] | [notes] |
| [datetime] | Found issue | [description] |
| [datetime] | Resolved issue | [resolution] |
```

---

## Status Definitions

### File Status

| Status | Meaning | Can Proceed? |
|--------|---------|--------------|
| `PENDING` | Not yet verified | No — verify first |
| `IN_PROGRESS` | Currently being verified | No — wait for completion |
| `VERIFIED` | All fields confirmed, implementation matches | Yes |
| `BLOCKED` | Issue found, needs resolution | No — resolve issue first |
| `NOT_APPLICABLE` | No cross-component dependencies | Yes — document why |

### Overall Feature Status

| Status | Meaning |
|--------|---------|
| `PENDING` | Checklist created, no files verified yet |
| `IN_PROGRESS` | Some files verified, work ongoing |
| `VERIFIED` | All files and cross-checks verified |
| `BLOCKED` | Issue found that blocks completion |

---

## Field Mapping Rules

### What to Map

For each file, map:
- **Schema definitions**: All fields in models, dataclasses, TypedDicts
- **Function parameters**: Input types for functions that cross file boundaries
- **Return types**: Output types for functions called by other files
- **External data**: Fields read from APIs, databases, files

### How to Map

1. **Copy exactly** — Don't type field names from memory
2. **Include line numbers** — Makes re-verification fast
3. **Note the source** — Always trace back to origin

```markdown
| Field | Type | Source File | Source Line | Matches |
|-------|------|-------------|-------------|---------|
| product_id | UUID | schema/product.py | 12 | ✓ |
```

### What "Matches" Means

A field matches if:
- Field name is **exactly** identical (case-sensitive)
- Type is **exactly** identical or explicitly converted
- Nullability is **exactly** identical

If any of these differ, it does NOT match — flag for resolution.

---

## Handling NOT_APPLICABLE

Some files genuinely have no cross-component dependencies. When marking NOT_APPLICABLE:

```markdown
### [File: utils/string_helpers.py]

**Dependencies**: None

**Status**: NOT_APPLICABLE

**Reason**: Pure utility functions with no external data dependencies. 
Input/output types are primitive (str, int). No schema dependencies.
```

The reason must be explicit. "It's simple" is not sufficient.

---

## When Verification Fails

### Type Mismatch
```markdown
## Issues Found

### Open Issues
- [ ] TYPE_MISMATCH: `product_id` is `UUID` in schema/product.py:12 
      but `str` in services/writer.py:45
      
      **Options**:
      A) Update schema to use str
      B) Update writer to use UUID  
      C) Add explicit conversion at line 45
      
      **Waiting for**: Human decision
```

### Name Mismatch
```markdown
- [ ] NAME_MISMATCH: Field is `product_name` in schema/product.py:13
      but `productName` in services/writer.py:46
      
      **Architectural rule**: Database fields use snake_case (see ARCHITECTURE.md)
      
      **Resolution**: Update services/writer.py to use `product_name`
```

### Missing Field
```markdown
- [ ] MISSING_FIELD: `created_at` expected by services/reader.py:78
      but not present in schema/product.py
      
      **Options**:
      A) Add created_at to schema
      B) Remove dependency from reader
      
      **Waiting for**: Human decision
```

---

## Integration with features.json

```json
{
  "id": "product-normalization",
  "verification": {
    "file": "verification/product-normalization.md",
    "status": "IN_PROGRESS",
    "last_updated": "2025-12-22T14:30:00Z",
    "files_verified": 2,
    "files_total": 5,
    "blocking_issues": 0
  },
  "files": [
    {
      "path": "schema/product.py",
      "depends_on": [],
      "verification_status": "VERIFIED"
    },
    {
      "path": "services/writer.py", 
      "depends_on": ["schema/product.py"],
      "verification_status": "VERIFIED"
    },
    {
      "path": "services/reader.py",
      "depends_on": ["schema/product.py", "services/writer.py"],
      "verification_status": "PENDING"
    }
  ]
}
```

---

## Checklist for Creating a New Verification

- [ ] Created `verification/[feature-id].md`
- [ ] Listed all files that will be created/modified
- [ ] Identified dependencies between files
- [ ] Ordered files by dependency (dependencies first)
- [ ] Created field mapping tables (can be empty initially)
- [ ] Linked to features.json
- [ ] Set initial status to PENDING
