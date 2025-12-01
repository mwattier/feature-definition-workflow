# Project Breaker Skill

A Claude Code skill for decomposing large projects into manageable, context-window-sized features.

---

## What This Does

This skill transforms large technical specifications into structured feature lists that are practical for AI-assisted implementation.

**The Problem**: You have a 450-line technical spec for a 6-month project. Where do you start?

**The Solution**: Three-tier decomposition into phases → epics → features → subtasks.

---

## Installation

### To Your Project

```bash
cd ~/your-project
mkdir -p .claude/skills
cp -r path/to/feature-definition-workflow/skills/project-breaker .claude/skills/
```

### To Your Workspace

```bash
mkdir -p ~/.claude/skills
ln -s path/to/feature-definition-workflow/skills/project-breaker ~/.claude/skills/project-breaker
```

---

## Usage

Just ask Claude:
- "Break down this large project"
- "Help me decompose this technical spec"
- "Create features.json from this architecture document"
- "How should I organize these requirements?"

Claude will guide you through the decomposition process.

---

## How It Works

### Three-Tier Decomposition

```
PHASES (Strategic - months)
  ├── EPICS (Tactical - weeks)
  │   ├── FEATURES (Operational - days)
  │   │   ├── SUBTASKS (Implementation - hours)
```

### The Process

1. **Identify Phases** (2-6 major milestones)
2. **Break into Epics** (3-8 initiatives per phase)
3. **Define Features** (4-10 deliverables per epic)
4. **Create Subtasks** (3-6 implementation steps per feature)
5. **Assign Priorities** (critical/high/medium/low)
6. **Map Dependencies** (what blocks what)
7. **Generate features.json** (hierarchical structure)
8. **Validate** (sizing, dependencies, practicality)

---

## Example Output

### Input
- 450-line technical specification
- 6-month timeline estimate
- Multiple integrated systems

### Output

```json
{
  "project": "marketplace-platform",
  "phases": [
    {
      "id": "P1",
      "name": "Phase 1 - Foundation",
      "epics": [
        {
          "id": "E1.1",
          "name": "Core Infrastructure",
          "features": [
            {
              "id": "F001",
              "name": "Database Schema Design",
              "estimatedEffort": "small",
              "subtasks": [
                {"id": "F001.1", "name": "Design entity models"},
                {"id": "F001.2", "name": "Create migrations"},
                {"id": "F001.3", "name": "Add indexes"},
                {"id": "F001.4", "name": "Test with sample data"}
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

Plus summary report, timeline estimate, and critical path analysis.

---

## Key Benefits

### Before Breakdown

❌ Large, overwhelming specification
❌ Unclear where to start
❌ Risk of context window exhaustion
❌ Hard to track progress

### After Breakdown

✅ Clear starting point (F001)
✅ Features sized for 1-3 sessions each
✅ Dependencies mapped explicitly
✅ Progress trackable systematically
✅ Phases provide strategic milestones

---

## Feature Sizing Guidelines

**Critical Rule**: Each feature must fit in 1-3 context windows

- **Small**: 1-4 hours (< 1 session)
- **Medium**: 4-8 hours (1-2 sessions)
- **Large**: 8-24 hours (2-4 sessions)
- **❌ Never > 24 hours** - split it

---

## Integration

### With Feature Definer

**Workflow**:
1. Project-breaker creates feature list
2. Feature-definer creates detailed specs for each
3. Features.json updated with complete definitions

### With Tracking Systems

Output connects to:
- features.json for AI workflows
- GitHub Issues for collaboration
- Jira/Linear for enterprise PM

---

## Example Session

```
You: "I have a technical spec for a marketplace platform.
     It's about 450 lines and covers 6 months of work."

Claude: "I'll help you break this down. Let me read the spec...

[Reviews document]

I see this as a 2-phase project:

**Phase 1: Foundation** (2-3 months)
- Core infrastructure
- User management
- Basic marketplace functionality

**Phase 2: Full Features** (3-4 months)
- Advanced search
- Payment integration
- Analytics & reporting

Does this phase structure make sense?"

You: "Yes, focus on Phase 1 for now"

Claude: "Great. I've broken Phase 1 into 3 epics with 22 features.

**Epic 1.1: Core Infrastructure** (5 features, ~20 hours)
- F001: Database Schema (4h)
- F002: API Framework (6h)
- F003: Authentication (8h)
- F004: Authorization (5h)
- F005: Deployment Pipeline (5h)

All features are sized for 1-2 sessions. You can start with F001
immediately - it has no dependencies.

Should I create the complete features.json?"
```

---

## Files

```
project-breaker/
├── SKILL.md                   # Skill definition for Claude
└── README.md                  # This file
```

---

## Related Documentation

- **Project Breakdown Guide**: `../../03-PROJECT-BREAKDOWN.md`
- **Feature Integration**: `../../04-ISSUE-INTEGRATION.md`
- **Feature Definer Skill**: `../feature-definer/`

---

## Best Used With

- Large projects (3+ months)
- Complex technical specifications
- Multi-phase roadmaps
- Team collaborations

**Not Needed For**:
- Small projects (< 10 features)
- Simple, clear requirements
- Single-feature additions

---

## Contributing

Improvements and examples welcome! This skill is part of the feature-definition-workflow methodology.

---

## License

MIT License - Part of feature-definition-workflow

---

**Remember**: The goal is manageable, context-window-sized features. Large projects become tractable through systematic decomposition.
