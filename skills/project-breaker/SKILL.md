---
name: project-breaker
description: |
  Decompose large projects into manageable features using three-tier breakdown (phases → epics → features → subtasks). Use when starting multi-month projects, breaking down large specifications, or creating features.json from architecture docs.
---

# Project Breaker Skill

## When to Use This Skill

Trigger this skill when the user:
- Says "break down this project" or "how do I start this large project"
- Has a technical specification for a multi-month project
- Needs to create features.json from architecture docs
- Asks "how do I organize these features"
- Mentions "large project", "complex system", or "multi-phase"

**Goal**: Transform large specifications into manageable, context-window-sized features.

---

## The Process

### Step 1: Understand Project Scope

Ask the user for:
1. Technical specification or project documentation
2. Timeline expectations
3. Team size (solo or team)
4. Any existing phase/milestone structure

**Questions**:
- "Do you have a technical spec I can review?"
- "What's the expected timeline?"
- "Are there predefined phases or should we create them?"

### Step 2: Identify Strategic Phases

Read the specification and identify 2-6 major strategic milestones.

**Questions for each phase**:
- What can ship to users at phase end?
- What is the strategic milestone?
- Are phases sequential or parallel?
- What dependencies exist between phases?

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

**Ask**:
- "What are the major initiatives in this phase?"
- "Can epics run in parallel or must they be sequential?"

### Step 4: Break Epics into Features

For each epic, define 4-10 deliverable units.

**Critical Sizing Rule**: Each feature must fit in 1-3 context windows

**Size Guidelines**:
- Small: 1-4 hours (< 1 session)
- Medium: 4-8 hours (1-2 sessions)
- Large: 8-24 hours (2-4 sessions)
- ❌ Never > 24 hours - split into smaller features

**Ask**:
- "Can this feature be implemented in 1-3 sessions?"
- "If no, how should we split it?"

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

### Step 6: Assign Priorities

Use MoSCoW method:

- **Critical**: Core functionality, project can't work without it
- **High**: Important features, significantly impacts value
- **Medium**: Nice-to-have, improves experience
- **Low**: Future enhancements, can defer

Mark features on critical path (those that block others).

### Step 7: Create features.json Structure

Generate hierarchical JSON with:
- All phases, epics, features, subtasks
- Status (all start as "pending")
- Dependencies
- Priorities
- Effort estimates
- Acceptance criteria

### Step 8: Validate Structure

Check:
- [ ] Each feature fits in 1-3 sessions
- [ ] Dependencies are explicit and resolvable
- [ ] No circular dependencies
- [ ] Critical path is clear
- [ ] Can start work on first feature immediately

---

## Output Format

### Hierarchical features.json

```json
{
  "project": "project-name",
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
              "name": "Feature Name",
              "estimatedEffort": "medium",
              "subtasks": [...]
            }
          ]
        }
      ]
    }
  ]
}
```

### Summary Report

Also provide:
- Total features count by phase
- Critical path features
- Estimated timeline
- Dependencies graph
- Recommended starting point

---

## Integration with Feature Definer

After breakdown:

1. **Project-breaker** creates feature list
2. **Feature-definer** defines each feature in detail
3. Features.json gets updated with full specifications

**Workflow**:
```
Project Spec
    ↓
Project-breaker: Create feature list
    ↓
For each feature:
    Feature-definer: Create detailed spec
    ↓
Complete features.json with definitions
```

---

## Example Conversation

**User**: "I have a 450-line technical spec for a marketplace platform. How do I break this down?"

**You**: "I'll help you decompose this into manageable features. Let me review the spec.

[Reviews spec]

I see this is a multi-phase project. I've identified:

**Phase 1: Foundation** (Weeks 1-3)
- Epic 1.1: Core Infrastructure
- Epic 1.2: User Management
- Epic 1.3: Basic Marketplace

**Phase 2: Full Marketplace** (Weeks 4-8)
- Epic 2.1: Payment Integration
- Epic 2.2: Search & Discovery
- Epic 2.3: Admin Tools

Does this phase structure make sense?"

**User**: "Yes, that looks good"

**You**: "Great. Let me break Phase 1 into features...

**Epic 1.1: Core Infrastructure** has 4 features:
- F001: Database Schema (4h - small)
- F002: API Framework Setup (6h - medium)
- F003: Authentication System (8h - medium)
- F004: Deployment Pipeline (5h - medium)

Should I continue with the other epics or would you like to review these first?"

[Continues breakdown process...]

"I've created a complete features.json with 45 features across 2 phases. Would you like me to:
1. Create GitHub issues for Phase 1 features?
2. Use feature-definer to create detailed specs for first epic?
3. Review the dependency graph?"

---

## Validation Checklist

Before finalizing breakdown:

**Feature Sizing**:
- [ ] No feature > 24 hours estimated
- [ ] Most features are medium (4-8h) or small (1-4h)
- [ ] Large features (8-24h) are justified and can't be split

**Dependencies**:
- [ ] All dependencies are explicitly listed
- [ ] No circular dependencies
- [ ] Critical path identified
- [ ] Parallel work opportunities noted

**Completeness**:
- [ ] All major requirements covered
- [ ] Each feature has acceptance criteria
- [ ] Subtasks are specific and actionable
- [ ] Priorities assigned logically

**Practicality**:
- [ ] Can start implementing F001 immediately
- [ ] First feature has no dependencies
- [ ] Epic completion provides value
- [ ] Phase delivery is shippable

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

---

## Success Criteria

The breakdown is successful when:

1. ✅ Developer can start implementing first feature immediately
2. ✅ Each feature has clear specification and acceptance criteria
3. ✅ Dependencies create a valid implementation order
4. ✅ Features are right-sized for context windows
5. ✅ Progress is trackable and measurable
6. ✅ Team/stakeholders understand the plan

---

## Next Steps After Breakdown

1. **Review with stakeholders**
2. **Use feature-definer** for first epic's features
3. **Create tracking entries** (features.json or issues)
4. **Start implementation** with F001
5. **Update progress** as features complete

---

## Related Skills

- **feature-definer**: For creating detailed feature specifications
- **Your project management tools**: For issue tracking integration

---

**Remember**: The goal is manageable, context-window-sized features with clear specifications. Large projects become tractable through systematic decomposition.
