# Project Breaker - Example Conversation

This document shows a complete example of using the project-breaker skill to decompose an existing Python project.

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

## Key Takeaways from Example

1. **v2 Structure Check First**: Always verify project has v2 setup before starting
2. **File Identification**: Every feature lists exactly which files it affects
3. **Dependency Mapping**: Critical path and file dependencies explicitly identified
4. **Verification Ready**: Output includes verification structure initialization
5. **Actionable Next Steps**: Clear guidance on using `/pre-implement` and verification workflow
