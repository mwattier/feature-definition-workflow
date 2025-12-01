# Breaking Down Large Projects

How to decompose large projects into manageable features using conversational definition and hierarchical tracking.

---

## The Problem

You have a large project with:
- Comprehensive technical specification
- Multi-phase roadmap
- Complex requirements
- 6-12 month timeline

**Question**: How do you start coding without context window exhaustion?

**Challenge**: Going from strategic documents to actionable, context-window-sized features.

---

## The Solution: Three-Tier Decomposition

Large projects need THREE levels of abstraction:

```
PHASES (Strategic - months)
  ├── EPICS (Tactical - weeks)
  │   ├── FEATURES (Operational - days)
  │   │   ├── SUBTASKS (Implementation - hours)
```

### Why This Matters

**Context Window Constraints**:
- **PHASE** = Too large (multi-month, context exhaustion guaranteed)
- **EPIC** = Still too large (multi-week, high risk of exhaustion)
- **FEATURE** = ✅ Right size (single session or 2-3 sessions max)
- **SUBTASK** = Increment within feature (commit-sized work)

**Principle**: Each feature must fit within 1-3 context windows to enable AI-assisted development without losing coherence.

---

## Step 1: Extract Phases

Read technical specification and identify major strategic milestones.

### Questions to Ask

- What can ship to users at phase end?
- What is the strategic milestone for each phase?
- Are phases sequential or can some overlap?
- What dependencies exist between phases?

### Example Phase Structure

**Phase 1: Foundation** (Month 1-2)
- Goal: Core infrastructure operational
- Deliverable: Basic system works end-to-end
- Success: Internal team can use it

**Phase 2: User Features** (Month 3-4)
- Goal: User-facing functionality complete
- Deliverable: External users can perform core tasks
- Success: Beta users providing feedback

**Phase 3: Scale & Polish** (Month 5-6)
- Goal: Production-ready system
- Deliverable: Performance, security, UX refined
- Success: Ready for public launch

---

## Step 2: Decompose Phases into Epics

For each phase, identify major initiatives (1-4 weeks each).

### Epic Characteristics

**Good Epic**:
- Delivers cohesive functionality
- Can be demoed to stakeholders
- Has clear completion criteria
- Takes 1-4 weeks to complete

**Too Small**: Just a single feature (promote to feature)
**Too Large**: Multiple unrelated initiatives (split into multiple epics)

### Example: Phase 1 Decomposition

**Phase 1: Foundation**

**Epic 1.1: Data Infrastructure** (Week 1)
- Database schema design
- Migration framework
- Seed data tooling

**Epic 1.2: API Foundation** (Week 1-2)
- REST API structure
- Authentication/authorization
- Core endpoints

**Epic 1.3: Admin Interface** (Week 2-3)
- Admin dashboard setup
- CRUD operations
- User management

**Epic 1.4: Deployment Pipeline** (Week 3-4)
- CI/CD configuration
- Environment setup
- Monitoring foundation

---

## Step 3: Break Epics into Features

For each epic, define deliverable units (1 day - 1 week each).

### Feature Sizing Guidelines

**Context Window Test**: Can this feature be implemented in 1-3 sessions?

**Size Estimates**:
- **Small**: 1-4 hours (< 1 session)
- **Medium**: 4-8 hours (1-2 sessions)
- **Large**: 8-24 hours (2-4 sessions)

❌ **Never estimate > 24 hours** - break into smaller features

### Example: Epic to Features

**Epic 1.1: Data Infrastructure**

**Feature F001: Database Schema Design** (Small - 4h)
- Design entity models
- Define relationships
- Document validation rules

**Feature F002: Migration Framework Setup** (Medium - 6h)
- Install migration tooling
- Create migration structure
- Test up/down migrations

**Feature F003: Seed Data System** (Medium - 5h)
- Create seed data factories
- Implement data loading
- Add development fixtures

---

## Step 4: Define Feature Subtasks

For each feature, break into commit-sized implementation steps.

### Subtask Characteristics

**Good Subtask**:
- 30 minutes - 2 hours of work
- Results in a logical commit
- Can be completed independently
- Has clear completion criteria

### Example: Feature to Subtasks

**Feature F002: Migration Framework Setup**

**Subtasks**:
1. Install migration library and dependencies (30 min)
2. Configure migration paths and settings (30 min)
3. Create first migration template (1 hour)
4. Implement rollback capability (1.5 hours)
5. Write migration execution tests (2 hours)
6. Document migration workflow (1 hour)

**Total**: 6 hours (medium feature)

---

## Step 5: Assign Priorities

Use MoSCoW method to prioritize features:

### Priority Levels

**Critical**
- Core functionality
- Project can't work without it
- Blocks other features
- Must be in MVP

**High**
- Important features
- Significantly impacts value
- Should be in MVP
- Can't defer long

**Medium**
- Nice-to-have
- Improves experience
- Can defer if needed
- Post-MVP acceptable

**Low**
- Future enhancements
- Can defer indefinitely
- Optional features
- Enhancement backlog

### Critical Path Identification

Mark features that block others:

```json
{
  "id": "F001",
  "priority": "critical",
  "criticalPath": true,
  "blocksFeatures": ["F002", "F003", "F005"]
}
```

**Why**: Helps prioritize when multiple features are pending.

---

## Using the Conversational Process

### For Each Feature

Before creating tracking entries, use the feature definition process:

1. **Have conversation** about the feature (15-45 minutes)
2. **Create feature document** using templates
3. **Extract subtasks** from implementation notes
4. **Identify dependencies** from discussion
5. **Create tracking entry** (features.json or issue)

### Example Workflow

**Starting Feature F002: Migration Framework**

**Conversation**:
```
User: "We need database migrations"

AI: "What migration tool do you want to use?"
User: "Probably [tool-name], it's standard for this stack"

AI: "Should migrations support rollback?"
User: "Yes, definitely need down migrations"

AI: "How will developers create new migrations?"
User: "CLI command that generates a template"

AI: "Any specific requirements for migration file naming?"
User: "Timestamp prefix, then descriptive name"
```

**Output**: Feature document created with clear requirements

**Then**: Extract subtasks and create tracking entry

---

## Hierarchical features.json Structure

For large projects, use nested structure for clarity:

```json
{
  "project": "project-name",
  "currentPhase": "Phase 1 - Foundation",
  "updated": "2025-11-30T00:00:00Z",
  "phases": [
    {
      "id": "P1",
      "name": "Phase 1 - Foundation",
      "status": "in_progress",
      "epics": [
        {
          "id": "E1.1",
          "name": "Data Infrastructure",
          "status": "in_progress",
          "features": [
            {
              "id": "F001",
              "name": "Database Schema Design",
              "status": "completed",
              "progress": 100
            },
            {
              "id": "F002",
              "name": "Migration Framework Setup",
              "status": "in_progress",
              "progress": 60
            }
          ]
        }
      ]
    }
  ]
}
```

See [templates/features.json.example](./templates/features.json.example) for complete structure.

---

## Breakdown Process Summary

### Step-by-Step

1. **Read technical specification**
2. **Identify strategic phases** (2-6 major milestones)
3. **Decompose each phase into epics** (3-8 per phase)
4. **Break each epic into features** (4-10 per epic)
5. **Define feature subtasks** (3-6 per feature)
6. **Assign priorities** (critical/high/medium/low)
7. **Identify dependencies** (what blocks what)
8. **Create feature documents** (using conversational process)
9. **Generate tracking structure** (features.json or issues)
10. **Validate** (are features right-sized?)

### Validation Checklist

Before starting implementation:

- [ ] Each feature fits in 1-3 context windows
- [ ] Dependencies are explicit and resolvable
- [ ] No circular dependencies
- [ ] Critical path is clear
- [ ] Can start work on first feature immediately
- [ ] Acceptance criteria defined for each feature
- [ ] Subtasks are commit-sized chunks

---

## Anti-Patterns to Avoid

### ❌ Feature Too Large

**Bad Example**:
```json
{
  "id": "F999",
  "name": "Build entire user authentication system",
  "estimatedEffort": "large"
}
```

**Why Bad**: "Large" likely means multi-week, guaranteed context exhaustion

**Fix**: Break into 6-10 features:
- F001: Database schema for users/sessions
- F002: Password hashing service
- F003: Login endpoint
- F004: Registration endpoint
- F005: Session management
- F006: Password reset flow
- etc.

### ❌ No Acceptance Criteria

**Bad Example**:
```json
{
  "id": "F002",
  "name": "Migration Framework Setup",
  "acceptanceCriteria": []
}
```

**Why Bad**: No clear definition of "done", leads to assumptions

**Fix**: List 3-6 specific, testable criteria:
```json
{
  "acceptanceCriteria": [
    "Migration tool installed and configured",
    "Can generate new migration from CLI",
    "Can run migrations up and down",
    "Migration status is queryable",
    "Tests verify migration execution"
  ]
}
```

### ❌ Circular Dependencies

**Bad Example**:
```json
{
  "id": "F001",
  "dependencies": ["F002"]
},
{
  "id": "F002",
  "dependencies": ["F001"]
}
```

**Why Bad**: Can't start either feature

**Fix**: Rethink architecture, find dependency-free entry point

### ❌ Flat Structure for Large Projects

**Bad**: Single array of 150 features at root level

**Why Bad**: No strategic context, hard to navigate, unclear phases

**Fix**: Use phases → epics → features hierarchy

---

## Integration with Feature Definition

### Workflow Integration

```
1. Project Breakdown
   ↓ (Creates feature list)
2. Feature Definition (per feature)
   ↓ (Creates feature document)
3. Subtask Extraction
   ↓ (From implementation notes)
4. Tracking Entry
   ↓ (features.json or issue)
5. Implementation
   ↓ (Build with clear spec)
6. Progress Update
```

### When to Define Features

**Option A: Define All Upfront**
- Create feature documents for entire phase
- Pros: Complete clarity before coding
- Cons: Time investment upfront

**Option B: Define Just-In-Time**
- Create feature documents as you reach each feature
- Pros: Spreads effort, learns as you go
- Cons: Less overall visibility

**Recommendation**: Hybrid approach
- Define first epic's features upfront
- Define remaining epics just-in-time
- Adjust as you learn

---

## Progress Tracking

### Hierarchical Rollup

```
Phase Progress = average(Epic Progress)
Epic Progress = average(Feature Progress)
Feature Progress = (completed subtasks / total subtasks) × 100
```

### Query Examples

**Current epic status**:
```bash
jq '.phases[] | select(.status=="in_progress") |
    .epics[] | select(.status=="in_progress")' features.json
```

**Features blocking next epic**:
```bash
jq '.phases[0].epics[0].features[] |
    select(.status!="completed") |
    .id, .name' features.json
```

**Overall phase progress**:
```bash
jq '.phases[0] |
    [.epics[].features[].progress] |
    add / length' features.json
```

---

## Handling Scope Changes

### New Feature Mid-Phase

Document why it was added:

```json
{
  "id": "F015b",
  "name": "Export Data to CSV",
  "addedMidPhase": true,
  "addedDate": "2025-12-15",
  "rationale": "User request for offline analysis capability",
  "priority": "medium"
}
```

### Feature Descoped

Document why it was removed:

```json
{
  "id": "F018",
  "name": "Advanced Analytics Dashboard",
  "status": "descoped",
  "descopedDate": "2025-12-10",
  "rationale": "Complexity too high for MVP, defer to Phase 2",
  "movedToPhase": "P2"
}
```

### Feature Split

Document when complexity discovered:

```json
{
  "id": "F010",
  "name": "User Profile Management",
  "status": "split",
  "splitInto": ["F010a", "F010b"],
  "splitRationale": "Profile editing separate from avatar upload complexity"
}
```

**Key Principle**: Always document WHY scope changed

---

## Next Steps

1. **Read your technical specification**
2. **Apply three-tier decomposition**
3. **Create hierarchical feature structure**
4. **Use conversational definition** for each feature
5. **Generate tracking system** (see [04-ISSUE-INTEGRATION.md](./04-ISSUE-INTEGRATION.md))
6. **Start implementation** with clear specifications

---

## Related Documentation

- [01-METHODOLOGY.md](./01-METHODOLOGY.md) - Conversational feature definition
- [02-TEMPLATES.md](./02-TEMPLATES.md) - Feature document templates
- [04-ISSUE-INTEGRATION.md](./04-ISSUE-INTEGRATION.md) - Tracking system integration
- [templates/features.json.example](./templates/features.json.example) - Complete example

---

**Remember**: The goal is manageable, context-window-sized features with clear specifications. Large projects become tractable through systematic decomposition.
