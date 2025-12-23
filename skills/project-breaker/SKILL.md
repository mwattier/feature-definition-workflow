---
name: project-breaker
version: 2.0.0
description: |
  Decompose large projects into manageable features using three-tier breakdown (phases → epics → features → subtasks) with v2 verification workflow. Use when starting multi-month projects, breaking down large specifications, or creating features.json from architecture docs.
---

# Project Breaker Skill (v2)

## When to Use This Skill

Trigger this skill when the user:
- Says "break down this project" or "how do I start this large project"
- Has a technical specification for a multi-month project
- Needs to create features.json from architecture docs
- Asks "how do I organize these features"
- Mentions "large project", "complex system", or "multi-phase"

**Goal**: Transform large specifications into manageable, context-window-sized features with verification structure.

---

## The Process (v2 Enhanced)

### Step 0: Check for v2 Verification Workflow

**BEFORE starting project breakdown**, check if project has v2 structure:

```
Look for:
- features.json with "version": "2.0"
- ARCHITECTURE.md exists
- verification/ directory exists
- .claude/commands/ directory exists
```

**If v2 structure exists**: Follow v2 workflow (includes file identification)
**If v1 or no structure**: Suggest running project-initializer skill first

**If ARCHITECTURE.md missing but other v2 files exist**:
```
⚠️ v2 structure detected but ARCHITECTURE.md is missing.

ARCHITECTURE.md is critical for verification workflow as it defines:
- System structure and components
- Naming conventions
- Type conventions
- Dependency rules

Should I help you create ARCHITECTURE.md first?
```

---

### Step 1: Understand Project Scope

Ask the user for:
1. Technical specification or project documentation
2. Timeline expectations
3. Team size (solo or team)
4. Any existing phase/milestone structure
5. **v2 NEW**: Existing codebase or greenfield?

**Questions**:
- "Do you have a technical spec I can review?"
- "What's the expected timeline?"
- "Are there predefined phases or should we create them?"
- **v2 NEW**: "Is there existing code or starting from scratch?"
- **v2 NEW**: "Does ARCHITECTURE.md accurately reflect current system?"

### Step 2: Identify Strategic Phases

Read the specification and identify 2-6 major strategic milestones.

**Questions for each phase**:
- What can ship to users at phase end?
- What is the strategic milestone?
- Are phases sequential or parallel?
- What dependencies exist between phases?
- **v2 NEW**: What system components does each phase touch?

**Example Phases**:
- Phase 1: Foundation (infrastructure, core systems)
- Phase 2: User Features (user-facing functionality)
- Phase 3: Scale & Polish (performance, UX refinement)

### Step 3: Decompose Phases into Epics

For each phase, identify 3-8 major initiatives (1-4 weeks each).

**Epic Characteristics**:
- Delivers cohesive functionality
- Can be demoed to stakeholders
- Has clear completion criteria
- Typically 1-4 weeks of work
- **v2 NEW**: Maps to system components from ARCHITECTURE.md

**Ask**:
- "What are the major initiatives in this phase?"
- "Can epics run in parallel or must they be sequential?"
- **v2 NEW**: "Which components from ARCHITECTURE.md does this epic affect?"

### Step 4: Break Epics into Features (v2 Enhanced)

For each epic, define 4-10 deliverable units.

**Critical Sizing Rule**: Each feature must fit in 1-3 context windows

**Size Guidelines**:
- Small: 1-4 hours (< 1 session)
- Medium: 4-8 hours (1-2 sessions)
- Large: 8-24 hours (2-4 sessions)
- ❌ Never > 24 hours - split into smaller features

**v2 NEW - For Each Feature, Identify**:
- Files to CREATE
- Files to MODIFY
- Schemas/types it depends on (from ARCHITECTURE.md)
- Naming conventions that apply
- Type conventions that apply

**Ask**:
- "Can this feature be implemented in 1-3 sessions?"
- "If no, how should we split it?"
- **v2 NEW**: "What files will this feature create or modify?"
- **v2 NEW**: "Does this feature use existing schemas from ARCHITECTURE.md?"
- **v2 NEW**: "What other features must be complete before this one?"

### Step 5: Define Feature Subtasks

For each feature, break into commit-sized implementation steps.

**Subtask Characteristics**:
- 30 minutes - 2 hours of work
- Results in a logical commit
- Clear completion criteria

**Typical subtasks**:
1. Design/planning step
2. Implementation step(s)
3. Testing step
4. Documentation step (if needed)

**v2 NEW**: For features with file dependencies, order subtasks by dependency

### Step 6: Map File Dependencies

**NEW in v2**: Create file dependency graph across features.

For the entire project:
1. List all files to be created/modified
2. Identify which features touch which files
3. Map dependencies between files
4. Identify files that multiple features depend on
5. Flag potential conflicts (multiple features modifying same file)

**Output**: Dependency matrix
```
File: config.py
  Created by: F001 (Environment Configuration)
  Used by: F002, F003, F005, F007 (4 features depend on this)
  Status: CRITICAL PATH - blocks 4 features
```

### Step 7: Assign Priorities

Use MoSCoW method with v2 considerations:

- **Critical**: Core functionality, project can't work without it
  - **v2 NEW**: Files with many dependencies
- **High**: Important features, significantly impacts value
  - **v2 NEW**: Features that unblock multiple others
- **Medium**: Nice-to-have, improves experience
- **Low**: Future enhancements, can defer

Mark features on critical path (those that block others).

**v2 NEW**: Consider verification complexity in priority:
- Features with many file dependencies → Higher priority (unblock others)
- Features with simple file structure → Can be parallelized

### Step 8: Create features.json Structure (v2 Schema)

Generate hierarchical JSON with v2 verification fields:

**For v2 projects**:
```json
{
  "version": "2.0",
  "project": {
    "name": "project-name",
    "description": "Brief description",
    "architecture_doc": "ARCHITECTURE.md"
  },
  "currentPhase": "Phase 1 - Foundation",
  "phases": [
    {
      "id": "P1",
      "name": "Phase 1 - Foundation",
      "epics": [
        {
          "id": "E1.1",
          "name": "Epic Name",
          "features": [
            {
              "id": "F001",
              "title": "Feature Name",
              "description": "Brief description",
              "status": "defined",
              "priority": "critical",
              "estimatedEffort": "medium",
              "feature_doc": "features/feature-id.md",
              "verification": {
                "file": null,
                "status": "PENDING",
                "last_updated": null
              },
              "files": [],
              "decisions": [],
              "checkpoints": [],
              "current_checkpoint": null,
              "subtasks": [...]
            }
          ]
        }
      ]
    }
  ]
}
```

**For v1 projects**: Use original format without verification fields.

### Step 9: Validate Structure (v2 Enhanced)

Check:
- [ ] Each feature fits in 1-3 sessions
- [ ] Dependencies are explicit and resolvable
- [ ] No circular dependencies
- [ ] Critical path is clear
- [ ] Can start work on first feature immediately
- **v2 NEW**: [ ] ARCHITECTURE.md exists and is populated
- **v2 NEW**: [ ] Each feature lists files to create/modify
- **v2 NEW**: [ ] File dependencies are mapped
- **v2 NEW**: [ ] Features with shared files are sequenced properly
- **v2 NEW**: [ ] Naming/type conventions from ARCHITECTURE.md noted

### Step 10: Generate Summary Report (v2 Enhanced)

Provide:
- Total features count by phase
- **v2 NEW**: Total files to create/modify
- Critical path features
- **v2 NEW**: Critical path files (most dependencies)
- Estimated timeline
- Dependencies graph
- **v2 NEW**: File dependency matrix
- **v2 NEW**: Verification complexity by feature
- Recommended starting point
- **v2 NEW**: Recommended verification order

---

## Output Format

### Summary Report Example (v2)

```markdown
# Project Breakdown: Beast Competitive Pricing System

## Overview
- Total Features: 12
- Total Files: 25 (8 CREATE, 17 MODIFY)
- Phases: 2
- Epics: 4
- Estimated Timeline: 6-8 weeks

## Phase 1: Infrastructure & Refactoring (3-4 weeks)

### Epic 1.1: Configuration Management (Week 1)
- F001: Environment Variable Configuration (Critical)
  - Files: 13 (2 CREATE, 11 MODIFY)
  - Effort: Medium (6-8h)
  - Dependencies: None
  - Blocks: F002, F003, F005

### Epic 1.2: Code Standardization (Week 2)
- F002: Unified Scraper Framework (High)
  - Files: 8 (1 CREATE, 7 MODIFY)
  - Effort: Large (16h)
  - Dependencies: F001

## Critical Path Files

1. **config.py** (F001) → Blocks 4 features
2. **base_scraper.py** (F002) → Blocks 3 features
3. **database.py** (F003) → Blocks 2 features

## Verification Complexity

- **Simple**: 4 features (1-3 files each)
- **Medium**: 6 features (4-8 files each)
- **Complex**: 2 features (9+ files each)

## Recommended Order

1. F001 (Environment Config) - Unblocks 4 features
2. F002 (Scraper Framework) - Unblocks 3 features
3. F003, F004, F005 (Can parallelize)
4. F006-F012 (Sequential by dependencies)

## Next Steps

1. Run `/pre-implement F001` to create verification checklist
2. Use `feature-definer` for detailed F001 specification
3. Implement F001 with verification workflow
4. Repeat for remaining features
```

---

## Integration Points

### With project-initializer Skill

**If v2 structure missing**:
```
I notice this project doesn't have v2 verification workflow set up.

For a project of this size ({feature-count} features, {file-count} files),
verification workflow is highly recommended. It will:
- Prevent type/field mismatches across {file-count} files
- Track dependencies between {feature-count} features
- Ensure consistent naming/typing conventions

Would you like me to initialize v2 workflow first? This adds:
- ARCHITECTURE.md (system structure)
- Verification checklists
- Dependency tracking
- Session checkpoints

Run: [invoke project-initializer skill]
```

### With feature-definer Skill

After breakdown:

**v2 Workflow**:
```
Project Spec
    ↓
Project-breaker: Create feature list with file identification
    ↓
For each feature (in dependency order):
    feature-definer: Create detailed spec
    ↓
    /pre-implement: Create verification checklist
    ↓
    Implement with /verify-file
    ↓
    /verify-feature when complete
    ↓
Complete features.json with verified features
```

**v1 Workflow** (backward compatible):
```
Project Spec
    ↓
Project-breaker: Create feature list
    ↓
For each feature:
    feature-definer: Create detailed spec
    ↓
Complete features.json with definitions
```

---

## Example Conversation (v2)

**User**: "I have an existing Python scraping project with 7 scripts. I need to refactor it and add new features. How do I break this down?"

**You**: "I'll help you decompose this project into manageable features. First, let me check your project structure.

[Checks for v2 structure]

✓ I see you have v2 verification workflow set up with ARCHITECTURE.md.
✓ features.json shows version 2.0

Let me review your ARCHITECTURE.md and existing code...

[Reviews ARCHITECTURE.md and codebase]

Based on your existing system, I've identified a two-phase approach:

**Phase 1: Infrastructure & Refactoring** (3-4 weeks)
- Epic 1.1: Configuration Management
- Epic 1.2: Code Standardization
- Epic 1.3: Testing Framework

**Phase 2: New Features** (3-4 weeks)
- Epic 2.1: Database Backend
- Epic 2.2: Scheduling & Automation
- Epic 2.3: Reporting Dashboard

Does this structure align with your goals?"

**User**: "Yes, let's focus on Phase 1 first"

**You**: "Great. Let me break Phase 1 into features...

**Epic 1.1: Configuration Management**

**F001: Environment Variable Configuration** (Critical)
- **Files to modify**: 7 scraper scripts, README.md, ARCHITECTURE.md
- **Files to create**: config.py, .env.example, .gitignore updates
- **Total**: 13 files
- **Effort**: Medium (6-8h)
- **Dependencies**: None - can start immediately
- **Blocks**: F002, F003, F005 (4 features depend on this)

This feature has significant ripple effects - it touches all 7 scrapers and unblocks 4 other features. The verification checklist will ensure we maintain consistency across all files.

Shall I continue with the other features?"

**User**: "Yes, continue"

[Continues breakdown...]

**You**: "I've completed the breakdown. Here's the summary:

**Project Breakdown Complete**
- 12 features across 2 phases
- 25 files to create/modify
- 4 features on critical path
- Estimated: 6-8 weeks

**Critical Path**:
F001 → F002 → F003 → F006 → F009 → F012

**File Dependency Analysis**:
- config.py: Required by 4 features (highest dependency)
- base_scraper.py: Required by 3 features
- 7 scraper files: Modified by multiple features (conflict potential)

I've generated features.json with v2 verification structure. All features have:
- Files to create/modify identified
- Dependencies mapped
- Verification structure initialized

**Next Steps**:
1. Review features.json structure
2. Run `/pre-implement F001` to create verification checklist
3. Use `feature-definer` for detailed F001 specification
4. Start implementation with verification workflow

Would you like me to:
A) Show the file dependency matrix?
B) Generate feature documents for first epic?
C) Explain verification approach for F001?"

---

## Validation Checklist (v2 Enhanced)

Before finalizing breakdown:

**Feature Sizing**:
- [ ] No feature > 24 hours estimated
- [ ] Most features are medium (4-8h) or small (1-4h)
- [ ] Large features (8-24h) are justified and can't be split

**Dependencies**:
- [ ] All feature dependencies are explicitly listed
- [ ] No circular dependencies
- [ ] Critical path identified
- [ ] Parallel work opportunities noted
- **v2 NEW**: [ ] File dependencies mapped
- **v2 NEW**: [ ] Features sharing files are sequenced properly
- **v2 NEW**: [ ] Files with many dependents identified

**Completeness**:
- [ ] All major requirements covered
- [ ] Each feature has acceptance criteria
- [ ] Subtasks are specific and actionable
- [ ] Priorities assigned logically
- **v2 NEW**: [ ] Each feature lists files to create/modify
- **v2 NEW**: [ ] ARCHITECTURE.md conventions noted per feature

**v2 Verification Readiness**:
- [ ] ARCHITECTURE.md exists and is populated
- [ ] Naming conventions documented
- [ ] Type conventions documented
- [ ] Component boundaries clear
- [ ] Each feature maps to system components

**Practicality**:
- [ ] Can start implementing first feature immediately
- [ ] First feature has no dependencies
- [ ] Epic completion provides value
- [ ] Phase delivery is shippable
- **v2 NEW**: [ ] First feature creates foundation files others need

---

## Anti-Patterns to Avoid

❌ **Features Too Large**
- Don't create "Build entire authentication system" (large, vague)
- Do create 6-8 specific features for auth

❌ **Flat Structure for Large Projects**
- Don't put 150 features in a flat array
- Do use phases → epics → features hierarchy

❌ **Missing Dependencies**
- Don't assume features can be done in any order
- Do explicitly list what blocks what

❌ **No Acceptance Criteria**
- Don't leave features without clear "done" definition
- Do list 3-6 specific, testable criteria

❌ **v2 NEW: No File Identification**
- Don't skip listing files to create/modify
- Do identify all files affected by each feature

❌ **v2 NEW: Ignoring ARCHITECTURE.md**
- Don't break down features without checking system structure
- Do map features to components from ARCHITECTURE.md

❌ **v2 NEW: Skipping Verification Setup**
- Don't let users start implementing without /pre-implement
- Do enforce verification workflow from the start

---

## Success Criteria (v2 Enhanced)

The breakdown is successful when:

1. ✅ Developer can start implementing first feature immediately
2. ✅ Each feature has clear specification and acceptance criteria
3. ✅ Dependencies create a valid implementation order
4. ✅ Features are right-sized for context windows
5. ✅ Progress is trackable and measurable
6. ✅ Team/stakeholders understand the plan
7. ✅ **v2 NEW**: Each feature lists files to create/modify
8. ✅ **v2 NEW**: File dependencies are mapped and understood
9. ✅ **v2 NEW**: ARCHITECTURE.md accurately reflects system
10. ✅ **v2 NEW**: Verification workflow is ready to use

---

## Next Steps After Breakdown

**v2 Workflow**:
1. **Review with stakeholders**
2. **For first feature**:
   - Run `/pre-implement [feature-id]`
   - Use `feature-definer` for detailed spec
   - Implement with `/verify-file` for each file
   - Complete with `/verify-feature`
3. **Repeat for subsequent features**
4. **Update progress** as features complete

**v1 Workflow** (backward compatible):
1. **Review with stakeholders**
2. **Use feature-definer** for first epic's features
3. **Create tracking entries** (features.json or issues)
4. **Start implementation**
5. **Update progress** as features complete

---

## Related Skills

- **project-initializer**: For adding v2 verification workflow to projects
- **feature-definer**: For creating detailed feature specifications
- **Your project management tools**: For issue tracking integration

---

## Version History

**v2.0.0** (2025-12-22):
- Added v2 verification workflow integration
- Added file identification and dependency mapping
- Added ARCHITECTURE.md integration
- Enhanced with verification complexity analysis
- Added file dependency matrix generation
- Updated output format for v2 schema
- Added v2-specific validation checks

**v1.0.0**: Original three-tier breakdown (phases → epics → features)

---

**Remember**: The goal is manageable, context-window-sized features with clear specifications and verification structure. Large projects become tractable through systematic decomposition with v2's file-level dependency tracking.
