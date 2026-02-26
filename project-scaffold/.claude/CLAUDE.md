# [Project Name] — Claude Instructions

> This file is loaded automatically when Claude Code starts in this project.
> It defines project-specific rules and workflows that Claude must follow.

## Project Overview

[Brief description of what this project does — 2-3 sentences]

## Critical Files

Before implementing any feature, Claude must read:
- `ARCHITECTURE.md` — System structure and cross-component rules
- `features.json` — Current feature definitions and status
- `verification/[feature-id].md` — Verification checklist for active feature

## Mandatory Workflows

### Before Starting Any Feature

```
1. Run /pre-implement [feature-id]
2. Wait for human confirmation
3. Do not write code until verification checklist exists
```

### Implementation Workflow

Follow systematic implementation from [06-IMPLEMENTATION.md](../../06-IMPLEMENTATION.md):

**Pre-Implementation Setup**:
1. Verify clear spec exists
2. Create feature branch: `feature/F001-description`
3. Research codebase patterns (if applicable)
4. Create worktree (recommended): `git worktree add ../worktrees/F001 feature/F001-description`
5. Update features.json status to `in-progress`

**For Each Subtask**:
1. Read subtask
2. Run `/verify-file` before writing
3. Implement
4. Run `/verify-file` after writing
5. Test (non-negotiable)
6. Commit with clear message
7. Update progress in features.json

**Regular Checks** (every 30-60 minutes):
- Re-read relevant spec section
- Verify implementation matches intent
- Document any deviations
- Update progress

**Before Marking Complete**:
- Run pre-completion checklist (see 06-IMPLEMENTATION.md)
- Verify all acceptance criteria met
- Run `/verify-feature [feature-id]`
- Document implementation deltas

**Quick Reference**: Print [06-IMPLEMENTATION-CHECKLIST.md](../../06-IMPLEMENTATION-CHECKLIST.md) and keep visible during development.

### Before Modifying Any File

```
1. Check verification status for that file
2. If PENDING: Run /verify-file [filepath] first
3. If BLOCKED: Stop and report the blocking issue
4. If VERIFIED or NOT_APPLICABLE: Proceed
```

### When Referencing Fields/Types

```
1. Copy-paste field names from source files — do not type from memory
2. Include source file and line number in verification
3. If type/name doesn't match expectations, STOP and flag
```

### After Completing Any File

```
1. Re-run /verify-file [filepath]
2. Update status to VERIFIED if all checks pass
3. Update features.json with progress
```

### Before Marking Feature Complete

```
1. Run /verify-feature [feature-id]
2. Confirm all files are VERIFIED
3. Update features.json status
4. Create checkpoint
```

## Project Rules

### Naming Conventions
<!-- Update these for your project -->
| Context | Convention | Example |
|---------|------------|---------|
| Database fields | snake_case | `product_id` |
| Python variables | snake_case | `product_id` |
| API responses | snake_case | `product_id` |
| File names | kebab-case | `product-service.py` |

### Type Conventions
<!-- Update these for your project -->
| Type | Database | Python | JSON |
|------|----------|--------|------|
| Identifiers | UUID | uuid.UUID | string |
| Timestamps | TIMESTAMPTZ | datetime | ISO 8601 |
| Money | NUMERIC(12,2) | Decimal | string |

### Verification Requirements

These feature types require full verification:
- Any feature touching data models
- Any feature with cross-service dependencies
- Any feature integrating with external systems

These feature types can use reduced verification:
- Pure UI features with no data changes
- Documentation-only changes
- Configuration changes (still verify config consumers)

## Error Handling

### When You Find a Mismatch

Classify severity first (see 05-VERIFICATION-WORKFLOW.md for full definitions):

**Critical (STOP)** — Type mismatches, missing required fields, wrong nullability:
```
1. Document the mismatch in verification checklist
2. Present options to human
3. Wait for decision
4. Document decision in decision log
5. Then implement resolution
```

**Warning (FLAG)** — Naming convention violations, style inconsistencies:
```
1. Document the violation in verification checklist
2. Propose fix based on ARCHITECTURE.md conventions
3. Apply fix and continue (unless ambiguous)
4. Log in verification checklist
```

**Info (LOG)** — Unused fields, documentation gaps:
```
1. Note in verification checklist
2. Continue working
```

### When You're Uncertain

Do NOT guess. Instead:
```
1. State what you're uncertain about
2. Explain what you would need to verify
3. Ask for guidance
4. Wait for response before proceeding
```

### When Verification Fails

```
1. Update file status to BLOCKED
2. Update feature verification status to BLOCKED  
3. Document the issue with specifics
4. Stop work on dependent files
5. Report to human
```

## Checkpoints

Create checkpoints:
- Before starting a complex file
- After completing each file in a multi-file feature
- Before any risky change
- When approaching context limits
- At end of work session

Checkpoint command: `/checkpoint [brief description]`

## Available Commands

| Command | Purpose |
|---------|---------|
| `/pre-implement [feature-id]` | Set up verification before implementing |
| `/verify-file [filepath]` | Verify a specific file |
| `/verify-feature [feature-id]` | Full feature verification |
| `/verification-status` | Show current verification state |
| `/checkpoint [description]` | Save current progress |
| `/continue [checkpoint-file]` | Resume from checkpoint |

## Implementation Reference

- **[06-IMPLEMENTATION.md](../../06-IMPLEMENTATION.md)**: Complete systematic implementation workflow
- **[06-IMPLEMENTATION-CHECKLIST.md](../../06-IMPLEMENTATION-CHECKLIST.md)**: Printable quick reference checklist

## Directory Structure

```
project/
├── ARCHITECTURE.md          # System structure (read first)
├── CLAUDE.md                # This file
├── features.json            # Feature tracking
├── decisions/               # Decision logs
│   └── YYYY-MM-DD-name.md
├── verification/            # Verification checklists
│   └── [feature-id].md
├── checkpoints/             # Session checkpoints
│   └── [feature-id]-[timestamp].md
└── .claude/
    └── commands/            # Custom commands
        ├── pre-implement.md
        ├── verify-file.md
        ├── verify-feature.md
        ├── verification-status.md
        ├── checkpoint.md
        └── continue.md
```

## Remember

1. **Verify before implementing** — The checklist exists to prevent errors
2. **Copy, don't recall** — Always copy-paste field names and types
3. **Stop on mismatch** — Never auto-resolve type or naming conflicts
4. **Dependency order matters** — Verify dependencies before dependents
5. **Document decisions** — If you choose between options, log why
6. **Checkpoint often** — Context loss wastes money and time

---

*This file was generated by feature-definition-workflow. Update project-specific sections above.*
