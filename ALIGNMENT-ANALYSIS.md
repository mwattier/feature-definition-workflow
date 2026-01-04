# Implementation Workflow Alignment Analysis

**Created**: 2026-01-04
**Purpose**: Identify all components that need updating to align with 06-IMPLEMENTATION.md and 06-IMPLEMENTATION-CHECKLIST.md

---

## Summary

With the addition of 06-IMPLEMENTATION.md and 06-IMPLEMENTATION-CHECKLIST.md, we now have complete workflow coverage from feature definition through implementation execution. This document identifies all components that need updating to reference the new implementation guidance.

---

## ✅ Already Aligned

### Core Documentation
- ✅ **README.md** - Updated with 06-IMPLEMENTATION.md and 06-IMPLEMENTATION-CHECKLIST.md references
- ✅ **01-METHODOLOGY.md** - Methodology unchanged, covers feature definition
- ✅ **02-TEMPLATES.md** - Template selection unchanged
- ✅ **03-PROJECT-BREAKDOWN.md** - Project decomposition unchanged
- ✅ **04-ISSUE-INTEGRATION.md** - Issue tracking unchanged
- ✅ **05-VERIFICATION-WORKFLOW.md** - Verification process unchanged, complements 06-IMPLEMENTATION

---

## 🔧 Needs Updates

### 1. Skills (3 files)

#### skills/project-initializer/SKILL.md

**Current State**: Sets up verification workflow structure but doesn't mention implementation workflow

**Needed Changes**:

**Section: Post-Initialization (Line 145-172)**
```markdown
Created:
✓ ARCHITECTURE.md — Review and update component details
✓ features.json — Ready for features
✓ .claude/CLAUDE.md — Claude will follow these instructions
✓ .claude/commands/ — 6 commands installed
✓ decisions/ — Ready for decision logs
✓ verification/ — Ready for verification checklists
✓ checkpoints/ — Ready for session checkpoints

Next steps:
1. Review ARCHITECTURE.md and fill in any missing details
2. Define your first feature using /feature-define
3. Before implementing, run /pre-implement [feature-id]
4. **NEW**: Review 06-IMPLEMENTATION.md for systematic implementation workflow
5. **NEW**: Print 06-IMPLEMENTATION-CHECKLIST.md for use during development

The verification workflow is now active. Claude will:
- Require verification before implementing files
- Cross-reference all field names and types
- Stop on mismatches and ask for decisions
- Create checkpoints to preserve context
- **NEW**: Follow systematic implementation workflow from 06-IMPLEMENTATION.md

Would you like to define your first feature now?
```

#### skills/feature-definer/SKILL.md

**Current State**: Guides feature definition and prompts /pre-implement, but doesn't reference implementation execution

**Needed Changes**:

**Section: Step 7: Next Steps (v2 Enhanced) (Line 153-179)**
```markdown
Once feature is defined and added to features.json:

**For v2 projects**:
```
✅ Feature defined and documented
✅ Added to features.json

Next step: Run verification setup
→ /pre-implement [feature-id]

This will:
- Create verification checklist
- Map all file dependencies
- Establish implementation order

⚠️ Do NOT start implementation until /pre-implement is complete.

**After verification setup**:
→ Review 06-IMPLEMENTATION.md for systematic implementation workflow
→ Use 06-IMPLEMENTATION-CHECKLIST.md during implementation

Implementation workflow:
1. Pre-implementation setup (branch, worktree, codebase research)
2. Execute subtasks systematically (verify → implement → test → commit)
3. Regular checks (spec alignment, progress updates)
4. Pre-completion checklist (functionality, quality, security)
5. Post-implementation (PR creation, worktree cleanup)

See 06-IMPLEMENTATION.md for complete details.
```
```

**Section: Example Conversation Flow (v2) (Line 240-292)**
```markdown
[After feature definition is complete...]

**You**: "Great! I've added this feature to features.json.

✅ Feature defined: user-authentication
📄 Document: features/user-authentication.md

**Next steps**:
1. **Verification Setup**: Run `/pre-implement user-authentication`
   This creates the verification checklist and dependency map.

2. **Implementation**: Follow 06-IMPLEMENTATION.md workflow:
   - Create feature branch and worktree
   - Execute subtasks systematically with verification
   - Use 06-IMPLEMENTATION-CHECKLIST.md as quick reference
   - Test after every change
   - Check spec alignment regularly

3. **Completion**: Run `/verify-feature user-authentication`
   Ensures all files verified and acceptance criteria met.

Do NOT start implementing until /pre-implement is complete.

Would you like me to run /pre-implement now?"
```

**Section: Related Skills (Line 378-383)**
```markdown
## Related Skills

- **project-initializer**: For adding v2 verification workflow to projects
- **project-breaker**: For decomposing large projects into features
- **Your governance system**: For determining appropriate template level

## Related Documentation

- **06-IMPLEMENTATION.md**: Systematic implementation workflow
- **06-IMPLEMENTATION-CHECKLIST.md**: Quick-reference checklist for implementation
- **05-VERIFICATION-WORKFLOW.md**: Verification process details
```

#### skills/project-breaker/SKILL.md

**Current State**: Breaks down projects and suggests /pre-implement, but doesn't reference implementation execution

**Needed Changes**:

**Section: Next Steps After Breakdown (Line 557-574)**
```markdown
## Next Steps After Breakdown

**v2 Workflow**:
1. **Review with stakeholders**
2. **For first feature**:
   - Run `/pre-implement [feature-id]`
   - Use `feature-definer` for detailed spec
   - **NEW**: Review 06-IMPLEMENTATION.md for workflow
   - **NEW**: Print 06-IMPLEMENTATION-CHECKLIST.md for reference
   - Implement with `/verify-file` for each file
   - Test systematically after each change
   - Complete with `/verify-feature`
3. **Repeat for subsequent features**
4. **Update progress** as features complete

**Implementation Resources**:
- **06-IMPLEMENTATION.md**: Complete implementation workflow
  - Pre-implementation setup
  - Systematic subtask execution
  - Pre-completion checklist
  - Post-implementation steps
- **06-IMPLEMENTATION-CHECKLIST.md**: Printable quick reference
  - Pre-implementation setup checklist
  - For-each-subtask steps
  - Pre-completion verification
  - Troubleshooting quick reference

**v1 Workflow** (backward compatible):
1. **Review with stakeholders**
2. **Use feature-definer** for first epic's features
3. **Create tracking entries** (features.json or issues)
4. **Start implementation**
5. **Update progress** as features complete
```

**Section: Related Skills (Line 577-583)**
```markdown
## Related Skills

- **project-initializer**: For adding v2 verification workflow to projects
- **feature-definer**: For creating detailed feature specifications
- **Your project management tools**: For issue tracking integration

## Related Documentation

- **06-IMPLEMENTATION.md**: Systematic implementation workflow
- **06-IMPLEMENTATION-CHECKLIST.md**: Quick-reference implementation checklist
- **05-VERIFICATION-WORKFLOW.md**: Verification process details
```

---

### 2. Templates (2 files)

#### templates/feature-template.md

**Current State**: Feature document template without implementation references

**Needed Changes**:

**Add new section at end (before "---")**:
```markdown
## Next Steps

Once this feature is approved:

1. **Verification Setup**
   ```bash
   /pre-implement [feature-id]
   ```
   Creates verification checklist and maps dependencies.

2. **Implementation**
   - Review **06-IMPLEMENTATION.md** for systematic workflow
   - Print **06-IMPLEMENTATION-CHECKLIST.md** for reference
   - Create feature branch and worktree
   - Execute subtasks with verification
   - Test after every change

3. **Completion**
   ```bash
   /verify-feature [feature-id]
   ```
   Verifies all acceptance criteria met.

See: [06-IMPLEMENTATION.md](../06-IMPLEMENTATION.md)
```

#### templates/feature-template-quick.md

**Current State**: Quick feature template without implementation references

**Needed Changes**:

**Add section at end**:
```markdown
## Implementation

See [06-IMPLEMENTATION.md](../06-IMPLEMENTATION.md) for systematic workflow.
Use [06-IMPLEMENTATION-CHECKLIST.md](../06-IMPLEMENTATION-CHECKLIST.md) as quick reference.
```

---

### 3. Project Scaffold (1 file)

#### project-scaffold/.claude/CLAUDE.md

**Current State**: Project instructions for verification workflow, doesn't mention implementation workflow

**Needed Changes**:

**Section: Mandatory Workflows (Line 17-59)**

**Add new subsection after "Before Starting Any Feature"**:
```markdown
### Implementation Workflow

Follow systematic implementation from 06-IMPLEMENTATION.md:

**Pre-Implementation Setup**:
1. Verify clear spec exists
2. Create feature branch: `feature/F001-description`
3. Research codebase patterns (if applicable)
4. Create worktree (recommended): `git worktree add ../worktrees/F001 feature/F001-description`
5. Update features.json status to `in_progress`

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

**Quick Reference**: Print 06-IMPLEMENTATION-CHECKLIST.md and keep visible during development.
```

**Section: Available Commands (Line 136-146)**

**Add reference to implementation docs**:
```markdown
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

- **[06-IMPLEMENTATION.md](../06-IMPLEMENTATION.md)**: Complete systematic implementation workflow
- **[06-IMPLEMENTATION-CHECKLIST.md](../06-IMPLEMENTATION-CHECKLIST.md)**: Printable quick reference checklist
```

---

### 4. Examples (2 files)

#### examples/example-01-authentication.md

**Current State**: Shows feature definition but stops before implementation

**Needed Change**:

**Add section at end**:
```markdown
## Implementation

After feature definition was approved, the implementation followed 06-IMPLEMENTATION.md workflow:

### Pre-Implementation Setup
1. Created feature branch: `feature/F001-user-authentication`
2. Researched existing auth patterns in codebase
3. Created worktree: `../worktrees/F001`
4. Updated features.json: `status: "in_progress"`

### Verification Setup
```bash
/pre-implement F001
```

Created verification checklist identifying:
- Files to create: User model, auth service, routes, tests
- Dependencies: None (foundation feature)
- Type conventions: UUID for user_id, bcrypt for passwords, JWT for tokens

### Systematic Implementation

**Subtask F001.1: User Model**
1. Ran `/verify-file schema/user.py` (before writing)
2. Implemented user model with email, password_hash, created_at fields
3. Ran `/verify-file schema/user.py` (after writing - verified types match)
4. Ran tests: `pytest tests/test_user_model.py`
5. Committed: "F001.1: Create user model with authentication fields"
6. Updated features.json: F001.1 status = "completed"

**Subtask F001.2: Password Hashing**
[Similar systematic approach...]

### Result

All acceptance criteria met. Full verification passed. Feature completed in 2 sessions (8 hours).

See [06-IMPLEMENTATION.md](../06-IMPLEMENTATION.md) for complete workflow details.
```

#### examples/example-02-api-endpoint.md

**Current State**: Shows feature definition but stops before implementation

**Needed Change**: (Similar to example-01, showing implementation workflow in action)

---

### 5. Scripts (no updates needed)

**scripts/validate-features.py** - Validation script, no implementation workflow references needed

**scripts/README.md** - Documents validation, doesn't need implementation references

---

### 6. Extra (no updates needed)

**extra/README.md** - Context management, orthogonal to implementation workflow

**extra/refresh-context.sh** - Generates summaries, doesn't need implementation references

---

## Priority Order for Updates

### High Priority (Core Workflow)
1. ✅ **skills/feature-definer/SKILL.md** - Most commonly used, directly transitions to implementation
2. ✅ **project-scaffold/.claude/CLAUDE.md** - Every project gets this, needs implementation guidance
3. ✅ **skills/project-initializer/SKILL.md** - Sets up workflow, should reference implementation

### Medium Priority (Enhanced Guidance)
4. ✅ **skills/project-breaker/SKILL.md** - Large projects benefit from implementation guidance
5. ✅ **templates/feature-template.md** - Feature docs should reference implementation workflow
6. ✅ **templates/feature-template-quick.md** - Quick template should at least link to workflow

### Low Priority (Examples)
7. ⚠️ **examples/example-01-authentication.md** - Nice to show workflow in action
8. ⚠️ **examples/example-02-api-endpoint.md** - Nice to show workflow in action

---

## Testing Alignment

After updates, verify:
- [ ] Skills reference 06-IMPLEMENTATION.md at appropriate points
- [ ] Skills reference 06-IMPLEMENTATION-CHECKLIST.md as a tool
- [ ] Templates provide clear next steps to implementation
- [ ] Project scaffold CLAUDE.md includes implementation workflow
- [ ] Examples show implementation in action (if updated)
- [ ] No broken links between documents
- [ ] Workflow progression is clear: Define → Verify → Implement → Complete

---

## Impact Summary

**Files Requiring Updates**: 8 (3 skills, 2 templates, 1 project scaffold, 2 examples)
**Files Already Aligned**: All core docs (01-05), README, scripts, extra

**Estimated Update Time**: 2-3 hours to update all components with references and workflow integration

**Risk Level**: Low - Adding references and guidance, not changing existing functionality

---

## Next Steps

1. Update high-priority files first (skills, project scaffold)
2. Update templates
3. Optionally enhance examples with implementation sections
4. Test complete workflow end-to-end
5. Commit all changes together with comprehensive message

---

**Document Status**: Analysis complete, ready for implementation
