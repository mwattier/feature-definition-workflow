# Project Breaker - Reference Material

This document contains detailed examples, anti-patterns, and success criteria for the project-breaker skill.

---

## Detailed Output Format Example (v2)

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
