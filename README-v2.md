# Feature Definition Workflow (v2)

A structured methodology for defining, verifying, and implementing software features with AI assistance. Designed to prevent costly rework by enforcing verification at every step.

**Core Principle**: 15 minutes of conversation and verification prevents hours of rework and hundreds of dollars in wasted AI compute.

---

## What's New in v2

Version 2 adds a **verification layer** that enforces cross-referencing during implementation:

| v1 (Planning) | v2 (Planning + Verification) |
|---------------|------------------------------|
| Feature definition | Feature definition |
| Project breakdown | Project breakdown |
| Issue tracking | Issue tracking |
| — | **Per-file verification** |
| — | **Dependency ordering** |
| — | **Type/naming enforcement** |
| — | **Session checkpoints** |
| — | **Decision logging** |

---

## The Problem This Solves

When building complex systems with AI assistance:

- **Type mismatches**: `product_id: UUID` in schema, `product_id: string` in generated code
- **Field name drift**: `productId` vs `product_id` vs `ProductID`
- **Lost context**: Starting fresh each session, re-explaining architecture
- **Silent errors**: AI generates code from "understanding" rather than cross-referencing sources
- **Expensive rework**: $400+ spent on bugs that were entirely preventable

These aren't AI capability failures — they're **verification failures**. The AI has the information but doesn't cross-reference it during generation.

---

## The Solution

A two-layer system:

### Layer 1: Methodology (this repo)
- Skills and templates that generate proper structure
- Lives outside any specific project
- Teaches Claude *how* to work

### Layer 2: Project Enforcement (generated per-project)
- CLAUDE.md with project-specific rules
- Slash commands that enforce verification
- Lives inside each project
- Makes Claude *follow* the methodology

---

## Quick Start

### For New Projects

1. **Initialize project structure**:
   ```
   Use the project-initializer skill:
   "Initialize this project for feature workflow"
   ```

2. **Define your first feature**:
   ```
   Use the feature-definer skill:
   "Let's define the product normalization feature"
   ```

3. **Before implementing, run**:
   ```
   /pre-implement product-normalization
   ```

4. **Implement with verification**:
   ```
   /verify-file schema/product.py
   [implement]
   /verify-file services/writer.py
   [implement]
   ...
   ```

5. **Complete with full verification**:
   ```
   /verify-feature product-normalization
   ```

### For Existing Projects

See [Adding to Existing Projects](#adding-to-existing-projects) below.

---

## Repository Structure

```
feature-definition-workflow/
├── 01-METHODOLOGY.md           # Feature definition process
├── 02-TEMPLATES.md             # Template selection guide
├── 03-PROJECT-BREAKDOWN.md     # Breaking projects into features
├── 04-ISSUE-INTEGRATION.md     # Connecting to tracking systems
├── 05-VERIFICATION-WORKFLOW.md # NEW: Verification process
├── templates/
│   ├── feature-template.md     # Feature document template
│   ├── architecture-context.md # NEW: ARCHITECTURE.md template
│   ├── decision-log.md         # NEW: Decision log template
│   ├── verification-checklist.md # NEW: Verification template
│   └── features-schema-v2.md   # NEW: Updated JSON schema
├── skills/
│   ├── feature-definer/        # Guided feature definition
│   └── project-initializer/    # NEW: Project scaffolding
├── project-scaffold/           # NEW: Files copied to projects
│   └── .claude/
│       ├── CLAUDE.md           # Project instructions template
│       └── commands/
│           ├── pre-implement.md
│           ├── verify-file.md
│           ├── verify-feature.md
│           ├── verification-status.md
│           ├── checkpoint.md
│           └── continue.md
├── examples/
├── scripts/
└── extra/
```

---

## How It Works

### Phase 1: Project Setup

```
Initialize project
    ↓
Create ARCHITECTURE.md (system structure)
    ↓
Create features.json (v2 schema)
    ↓
Install .claude/ commands
    ↓
Ready for feature definition
```

### Phase 2: Feature Definition (unchanged from v1)

```
Conversation about feature
    ↓
Clarifying questions
    ↓
Feature document created
    ↓
Added to features.json
```

### Phase 3: Pre-Implementation (NEW)

```
/pre-implement [feature-id]
    ↓
Read ARCHITECTURE.md
    ↓
Identify all files + dependencies
    ↓
Create verification checklist
    ↓
Establish implementation order
    ↓
Human confirms
```

### Phase 4: Verified Implementation (NEW)

```
For each file (in dependency order):
    ↓
/verify-file [path]
    ↓
Read all dependency files
    ↓
Create field mapping table
    ↓
Check naming conventions
    ↓
Check type conventions
    ↓
If mismatch → STOP, ask human
    ↓
If verified → implement
    ↓
Re-verify after implementation
```

### Phase 5: Feature Completion (NEW)

```
/verify-feature [feature-id]
    ↓
Check all files verified
    ↓
Verify cross-file interfaces
    ↓
Run automated checks
    ↓
Update features.json
    ↓
Feature complete
```

---

## Key Commands

| Command | Purpose |
|---------|---------|
| `/pre-implement [id]` | Set up verification before implementing |
| `/verify-file [path]` | Verify single file against dependencies |
| `/verify-feature [id]` | Full feature verification |
| `/verification-status` | Show current verification state |
| `/checkpoint [desc]` | Save session progress |
| `/continue [file]` | Resume from checkpoint |

---

## Verification Rules

### Claude Must:

1. **Copy, don't recall** — Field names and types are copy-pasted from source files
2. **Show the source** — Every field reference includes file and line number
3. **Verify dependencies first** — Can't implement file B until file A is verified
4. **Stop on mismatch** — Never auto-resolve type or naming conflicts
5. **Update checklists immediately** — Don't defer verification updates

### Claude Must Not:

1. Skip verification steps
2. Generate field names from memory
3. Auto-resolve mismatches
4. Implement out of dependency order
5. Mark files verified without cross-referencing

---

## features.json v2 Schema

```json
{
  "version": "2.0",
  "project": { ... },
  "features": [
    {
      "id": "feature-id",
      "title": "Feature Title",
      "status": "in-progress",
      "verification": {
        "file": "verification/feature-id.md",
        "status": "IN_PROGRESS",
        "files_verified": 2,
        "files_total": 5
      },
      "files": [
        {
          "path": "schema/product.py",
          "depends_on": [],
          "verification_status": "VERIFIED"
        }
      ],
      "decisions": ["decisions/2025-12-22-uuid.md"],
      "checkpoints": [...],
      "current_checkpoint": "checkpoints/..."
    }
  ]
}
```

See `templates/features-schema-v2.md` for full schema.

---

## Adding to Existing Projects

If you have an existing project:

1. **Copy the project scaffold**:
   ```
   cp -r project-scaffold/.claude your-project/
   ```

2. **Create ARCHITECTURE.md** using the template

3. **Create or migrate features.json** to v2 schema

4. **Create directories**:
   ```
   mkdir -p verification checkpoints decisions
   ```

5. **For in-progress features**, create verification checklists retroactively

---

## When Verification Catches Errors

When Claude finds a mismatch:

```
VERIFICATION FAILED: Type mismatch detected

Field: product_id
Expected (from schema/product.py:12): UUID
Found (in services/writer.py:45): str

Options:
A) Update schema to use str
B) Update writer to use UUID
C) Add explicit conversion

Action required: Human decision
```

Claude **stops and waits**. No auto-resolution. The human decides, and the decision is logged.

---

## Checkpoints

Checkpoints preserve context across sessions:

```
/checkpoint "Completed writer service, starting reader"
```

Creates `checkpoints/feature-id-20251222-1430.md` with:
- What's complete
- What's in progress
- Key decisions made
- Issues encountered
- Next steps

Resume with:
```
/continue
```

---

## Decision Logs

Major decisions are captured in `decisions/`:

```markdown
# Decision: UUIDs for All Identifiers

> Date: 2025-12-22
> Status: ACCEPTED

## Context
[Why this decision was needed]

## Decision
[What was decided]

## Alternatives Considered
[What else was considered and why not]

## Consequences
[Tradeoffs accepted]
```

Referenced in features.json and code comments.

---

## ROI

### Before This Workflow
```
Build feature based on rough idea
    ↓
Implement from AI's "understanding"
    ↓
Type mismatch in production
    ↓
Debug → Find error → Fix → Retest
    ↓
$400+ in AI compute wasted
```

### After This Workflow
```
Define feature clearly
    ↓
Set up verification
    ↓
Implement with cross-referencing
    ↓
Catch mismatch before code is written
    ↓
Zero rework needed
```

---

## Documentation

| Document | Purpose |
|----------|---------|
| [01-METHODOLOGY.md](01-METHODOLOGY.md) | Feature definition process |
| [02-TEMPLATES.md](02-TEMPLATES.md) | Template selection |
| [03-PROJECT-BREAKDOWN.md](03-PROJECT-BREAKDOWN.md) | Breaking down projects |
| [04-ISSUE-INTEGRATION.md](04-ISSUE-INTEGRATION.md) | Tracking integration |
| [05-VERIFICATION-WORKFLOW.md](05-VERIFICATION-WORKFLOW.md) | Verification process |
| [templates/](templates/) | All templates |
| [skills/](skills/) | Claude skills |

---

## License

MIT License — Copyright Mike Wattier

---

**Remember**: The goal isn't perfect documentation — it's preventing the $400 mistakes through structured verification.
