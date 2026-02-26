# Verification Workflow

A structured verification process that ensures Claude cross-references all dependencies before and during implementation.

**Core Principle**: Claude has the information. This workflow forces Claude to verify against that information rather than generate from memory.

---

## The Problem This Solves

When implementing features that touch multiple components, common failures occur:

* **Type mismatches** — `product_id: UUID` in one schema, `product_id: string` in generated code
* **Field name drift** — `productId` vs `product_id` vs `ProductID`
* **Missing dependencies** — File A depends on File B, but File B's changes aren't reflected
* **Schema divergence** — Two files reference the same data structure differently

These are not capability failures. Claude understands types, naming conventions, and dependencies. These are **verification failures** — Claude generates from its understanding rather than cross-referencing the source.

---

## Verification Principles

### 1. Copy, Don't Recall

When referencing a field name or type, Claude must copy-paste from the source file, not generate from understanding.

### 2. Show the Source

Every field reference must include where it came from. Use function/type/class names as primary anchors, with line numbers as secondary convenience (line numbers shift as code changes):
```
product_id (UUID) — from ProductSchema in schema/product.py (line 12)
```

### 3. Dependencies First

Files must be verified in dependency order. If `read_results.py` depends on `write_results.py`, verify `write_results.py` first.

### 4. Explicit Status

Every file has a verification status: `PENDING`, `VERIFIED`, or `NOT_APPLICABLE`. No ambiguity.

---

## Verification Workflow

### Phase 1: Pre-Implementation Mapping

Before any code is written, Claude must complete:

```
1. List all files that will be created or modified
2. For each file, identify:
   - What schemas/types it depends on
   - What other files depend on it
   - External systems it interfaces with
3. Order files by dependency (dependencies first)
4. Create verification checklist
```

### Phase 2: Per-File Verification

Before implementing each file:

```
1. Read all dependency files
2. Create field mapping table:
   | Field | Type | Source File | Source Line |
   |-------|------|-------------|-------------|
3. For fields that exist in multiple sources:
   - Confirm they match exactly
   - If they don't match, STOP and flag for human decision
4. Only after mapping is complete, begin implementation
5. After implementation, verify output matches mapping
```

### Phase 3: Cross-File Verification

After all files in a feature are implemented:

```
1. For each dependency relationship:
   - Confirm calling code matches called code exactly
   - Confirm types flow correctly across boundaries
2. Run any available type checkers / linters
3. Update verification status to VERIFIED
```

---

## Verification Checklist Template

Each feature gets a verification checklist at `verification/[feature-id].md`:

```markdown
# Verification: [feature-id]

## Status: PENDING | IN_PROGRESS | VERIFIED

## Files

| File | Depends On | Status | Verified By | Timestamp |
|------|------------|--------|-------------|-----------|
| schema/product.py | (none) | VERIFIED | Claude | 2025-12-22T14:00:00Z |
| services/writer.py | schema/product.py | VERIFIED | Claude | 2025-12-22T14:15:00Z |
| services/reader.py | schema/product.py, services/writer.py | PENDING | — | — |

## Field Mappings

### schema/product.py
| Field | Type | Line |
|-------|------|------|
| product_id | UUID | 12 |
| name | str | 13 |
| created_at | datetime | 14 |

### services/writer.py
| Field Used | Expected Type | Source | Matches Source |
|------------|---------------|--------|----------------|
| product_id | UUID | schema/product.py:12 | ✓ |
| name | str | schema/product.py:13 | ✓ |

## Cross-File Verification

| Caller | Callee | Interface | Status |
|--------|--------|-----------|--------|
| reader.py:get_product() | writer.py:write_product() | ProductSchema | PENDING |

## Issues Found

- [ ] None yet

## Sign-Off

- [ ] All files VERIFIED
- [ ] All cross-file checks VERIFIED
- [ ] Human review complete (if required)
```

---

## Integration with features.json

Each feature entry must include:

```json
{
  "id": "product-normalization",
  "verification": {
    "file": "verification/product-normalization.md",
    "status": "PENDING",
    "last_updated": "2025-12-22T14:00:00Z"
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

**Implementation cannot begin on a file until all files it depends on have `verification_status: VERIFIED`.**

---

## Mismatch Severity Levels

Not all verification failures carry the same weight. Classify mismatches before deciding whether to stop:

### Critical (STOP)

These break correctness. Claude must stop and wait for a human decision.

- **Type mismatches**: `UUID` vs `str`, `int` vs `float`, wrong nullability
- **Missing required fields**: A dependency expects a field that doesn't exist
- **Wrong cardinality**: 1:1 vs 1:n relationship mismatch
- **Schema divergence**: Two files define the same structure differently

### Warning (FLAG)

These break consistency but not correctness. Claude flags them, proposes a fix based on ARCHITECTURE.md conventions, and continues unless the fix is ambiguous.

- **Naming convention violations**: `productName` where snake_case is required
- **Style inconsistencies**: Mixed quote styles, inconsistent import ordering
- **Documentation gaps**: Missing docstrings on public interfaces

### Info (LOG)

These are worth noting but don't block work.

- **Unused fields**: Fields defined in schema but not yet consumed
- **Missing optional fields**: Fields that exist in source but aren't used by target
- **Documentation suggestions**: Type hints that could be more specific

---

## When Verification Fails

If during verification Claude finds a mismatch:

### Type Mismatch (Critical - STOP)
```
VERIFICATION FAILED [CRITICAL]: Type mismatch detected

Field: product_id
Expected (from schema/product.py:12): UUID
Found (in services/writer.py:45): str

Severity: CRITICAL — types affect runtime correctness
Action required: Human decision needed
Options:
  A) Update schema/product.py to use str
  B) Update services/writer.py to use UUID
  C) Add type conversion at boundary
```

### Field Name Mismatch (Warning - FLAG)
```
VERIFICATION WARNING [WARNING]: Field name mismatch detected

Expected (from schema/product.py:13): product_name
Found (in services/writer.py:46): productName

Severity: WARNING — naming convention violation
Architecture rule: Database and Python fields use snake_case (ARCHITECTURE.md)
Proposed fix: Update services/writer.py:46 to use product_name

Proceeding with proposed fix unless you object.
```

### Unused Field (Info - LOG)
```
VERIFICATION NOTE [INFO]: Unused field detected

Field: updated_at defined at schema/product.py:15
Not referenced by any dependent file in this feature

No action required. Logged for awareness.
```

**For Critical issues, Claude must STOP and present options. Do not auto-resolve.**
**For Warning issues, Claude flags and proposes a fix but can continue.**
**For Info issues, Claude logs and continues.**

---

## Verification Tiers

Not every feature needs the same level of verification rigor. Choose the tier that matches the risk:

### Lite

For prototypes, UI-only changes, config tweaks. Low risk of cross-component breakage.

**What you do**:
- Conversational definition + Quick template
- Dependency map (which files, what order)
- Implement and test

**What you skip**:
- Field-by-field mapping tables
- Per-file /verify-file commands
- Warning-level STOP gates (naming violations are ignored at this tier)

**Note**: Critical-severity mismatches (type errors, missing required fields, wrong nullability) still trigger STOP even at Lite tier. Lite reduces ceremony, not safety.

### Standard (Default)

For production features. The default tier unless you have a reason to go lighter or heavier.

**What you do**:
- Full feature definition
- /pre-implement to create verification checklist
- /verify-file at component boundaries (where data crosses between files)
- STOP on type mismatches (Critical severity)
- FLAG naming violations (Warning severity)

**What you skip**:
- Line-by-line field mapping for internal-only code
- Human sign-off (unless required by project policy)

### Full

For multi-data-store features, external API integrations, anything where a type mismatch would be expensive to debug in production.

**What you do**:
- Everything in Standard
- Field-by-field mapping tables with line numbers for every file
- Cross-file interface verification (caller/callee contracts)
- External system contract verification (API schemas, DB schemas)
- Human sign-off before marking complete

| Signal | Tier |
|--------|------|
| Prototype, spike, throwaway code | Lite |
| Single data store, internal only | Standard |
| Multiple data stores, external APIs | Full |
| UI-only, no data model changes | Lite |
| New data model or schema changes | Standard or Full |
| Touching payment, auth, or PII | Full |

---

## Structural vs. Behavioral Correctness

This verification workflow checks **structural correctness**: field names, types, interfaces, and dependency ordering. It catches the "wrong name" and "wrong type" class of bugs.

It does not check **behavioral correctness**: whether the logic is right, whether edge cases are handled, whether the algorithm produces correct results. That's the job of unit tests, integration tests, and code review.

Use both. Verification prevents the structural bugs that waste hours of debugging. Tests prevent the logic bugs that verification can't see.

---

## Verification for Different Feature Types

### Data Model Features
Full verification required:
- Schema field mapping
- Type verification
- Cross-file dependency verification

### API Endpoint Features
Full verification required:
- Request/response schema mapping
- Type verification
- Integration with data layer verification

### UI-Only Features
Reduced verification:
- Verify prop types match API response types
- Mark data layer as NOT_APPLICABLE if no changes

### Configuration Features
Targeted verification:
- Verify config keys match expected consumers
- Verify value types

---

## Claude Commands for Verification

These commands are installed in each project's `.claude/commands/` directory:

### /pre-implement
Run before starting any feature implementation. Maps all files, dependencies, and creates verification checklist.

### /verify-file [filepath]
Run verification for a specific file. Creates field mapping, checks against dependencies.

### /verify-feature [feature-id]
Run full verification for all files in a feature. Checks cross-file dependencies.

### /verification-status
Show current verification status for active feature.

---

## Enforcement

The feature-definer skill will:

1. **Refuse to mark a feature as "ready for implementation"** until:
   - Verification file exists
   - All files are mapped with dependencies
   - Dependency order is established

2. **Refuse to mark a feature as "complete"** until:
   - All files have `verification_status: VERIFIED`
   - Cross-file verification is complete
   - No open issues in verification checklist

This is not optional. The structure exists to prevent the $400 mistakes.

---

## Quick Reference

**Before implementing any file:**
```
1. Run /verify-file [filepath]
2. Confirm all dependencies are VERIFIED
3. Create field mapping table
4. Get human confirmation if any mismatches
5. Only then write code
```

**After implementing any file:**
```
1. Re-run /verify-file [filepath]
2. Confirm implementation matches mapping
3. Update status to VERIFIED
4. Proceed to next file in dependency order
```

**Before marking feature complete:**
```
1. Run /verify-feature [feature-id]
2. Confirm all files VERIFIED
3. Confirm all cross-file checks pass
4. Update feature status in features.json
```
