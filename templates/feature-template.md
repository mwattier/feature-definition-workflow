# Feature: [Feature Name]

**Status**: Draft
**Priority**: [Critical/High/Medium/Low]
**Version**: 1.0
**Last Updated**: YYYY-MM-DD
**Related Features**: [List any related features]

---

## Purpose

**Problem Statement**: What problem does this solve? Why do we need it?

**Business Value**: What value does this provide to users or the business?

---

## User Story

**As a** [role/persona]
**I want to** [action/capability]
**So that** [benefit/outcome]

**Acceptance Criteria**:
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

---

## Conceptual Flow

Describe how this feature works from start to finish:

### Happy Path

1. User/system does X
2. System validates/processes Y
3. System performs Z
4. Result/feedback is A

### Alternative Paths

**Path 1: [Scenario]**
1. Step 1
2. Step 2
3. Outcome

**Path 2: [Scenario]**
1. Step 1
2. Step 2
3. Outcome

### Error Cases

**Error 1: [Invalid Input]**
- Trigger: What causes this error
- Response: How system handles it
- User Impact: What user sees/experiences

**Error 2: [System Failure]**
- Trigger: What causes this error
- Response: How system handles it
- User Impact: What user sees/experiences

---

## Data Model

### Entities/Models Involved

**EntityName1**
- `field1`: type - Description/purpose
- `field2`: type - Description/purpose
- `field3`: type - Description/purpose

**EntityName2**
- `field1`: type - Description/purpose
- `field2`: type - Description/purpose

### Relationships

```
[Entity A] --1:n--> [Entity B]
    |
    |--1:1--> [Entity C]

[Entity D] --n:m--> [Entity E]
```

**Relationship Descriptions**:
- Entity A has many Entity B (one-to-many)
- Entity A has one Entity C (one-to-one)
- Entity D has many Entity E through junction table (many-to-many)

### Database Schema Changes

**New Tables**:
```sql
-- Example table creation
CREATE TABLE example (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);
```

**Modified Tables**:
- `table_name`: Add field `field_name` (type)
- `table_name`: Modify field `field_name` to allow null

### Validation Rules

- Field X: Required, must be unique
- Field Y: Optional, max length 255
- Field Z: Must be valid email format
- Relationship A→B: Cascade on delete

---

## UI/UX Notes

*(Delete this section if not applicable - e.g., API-only features)*

### User Interface

**Screen/Page**: [Name of screen]
- **Location**: Where in the app/system
- **Access**: Who can access this
- **Layout**: Brief description or ASCII diagram

### Forms/Inputs

**Form Name**:
- Field 1: [Type] - Label, help text, validation
- Field 2: [Type] - Label, help text, validation
- Field 3: [Type] - Label, help text, validation

### Actions/Buttons

- **Action Name**: What it does, confirmation needed?, success message
- **Action Name**: What it does, confirmation needed?, success message

### Views/Tables

**View Name**:
- Columns: [List columns to display]
- Filters: [Available filter options]
- Sort: [Default sort, available sort options]
- Actions: [Row-level actions available]

### Notifications/Feedback

- Success: "Message shown on success"
- Error: "Message shown on error"
- Warnings: "Message shown for warnings"

---

## API Design

*(Delete this section if not applicable)*

### Endpoints

**POST /api/resource**
- **Purpose**: Create new resource
- **Auth**: Required role/permission
- **Request Body**:
  ```json
  {
    "field1": "string",
    "field2": 123
  }
  ```
- **Response**: 201 Created
  ```json
  {
    "id": 1,
    "field1": "string",
    "field2": 123
  }
  ```
- **Errors**: 400 (validation), 401 (unauthorized)

**GET /api/resource/{id}**
- **Purpose**: Retrieve resource by ID
- **Auth**: Required role/permission
- **Response**: 200 OK
  ```json
  {
    "id": 1,
    "field1": "string",
    "field2": 123
  }
  ```
- **Errors**: 404 (not found), 401 (unauthorized)

---

## Key Questions & Decisions

Document all questions asked during definition and the decisions made:

**Q**: [Question that was unclear or ambiguous]
**A**: [Decision made with rationale]
**Impact**: [What this decision affects]

**Q**: [Another question]
**A**: [Another decision]
**Impact**: [What this decision affects]

---

## Implementation Notes

### Services/Classes Needed

- **ServiceName**: Purpose and key methods
- **HelperClass**: Purpose and key methods

### Jobs/Queues

*(Delete if not applicable)*

- **JobName**: What it does, when it runs, priority
- **JobName**: What it does, when it runs, priority

### Events/Listeners

*(Delete if not applicable)*

- **Event**: When it fires
- **Listener**: What it does in response

### External Integrations

*(Delete if not applicable)*

- **Integration**: Purpose, authentication, rate limits
- **Integration**: Purpose, authentication, rate limits

### Caching Strategy

*(Delete if not applicable)*

- **Cache Key Pattern**: `prefix:identifier`
- **TTL**: How long cached
- **Invalidation**: When/how cache is cleared

### Security Considerations

- **Authorization**: Who can access this feature
- **Input Validation**: What needs validation
- **Data Sanitization**: What needs sanitization
- **Sensitive Data**: How to protect it

### Performance Considerations

- **Expected Load**: Typical usage patterns
- **Optimization Needed**: Indexes, caching, etc.
- **Bottlenecks**: Potential performance issues

---

## Out of Scope

Explicitly state what this feature does NOT do:

- ❌ Does not handle X (that's in Feature Y)
- ❌ Does not support Z (future consideration)
- ❌ Does not include A (out of scope for MVP)

---

## Dependencies

### Required Before This

- ✅ Feature X must be complete
- ✅ Library Y must be installed
- ✅ Infrastructure Z must be configured

### Blocks These Features

- Feature A cannot start until this is done
- Feature B depends on this

### Related/Adjacent Features

- Feature C is similar but different because...
- Feature D complements this by...

---

## Success Criteria

How do we know this feature is complete and working?

### Functional Criteria

1. ✅ User can perform action X successfully
2. ✅ System validates input Y correctly
3. ✅ Data is stored/retrieved as expected
4. ✅ Error handling works for edge cases

### Technical Criteria

1. ✅ Unit tests pass (target: 80%+ coverage)
2. ✅ Integration tests pass
3. ✅ Performance meets targets (e.g., < 200ms response time)
4. ✅ Security audit passes

### Quality Criteria

1. ✅ Code review approved
2. ✅ Documentation complete
3. ✅ No critical bugs in testing
4. ✅ Accessible (WCAG compliance if applicable)

---

## Testing Plan

### Unit Tests

- Test case 1: Description
- Test case 2: Description
- Test case 3: Description

### Integration Tests

- Test scenario 1: Description
- Test scenario 2: Description

### Manual Testing

- [ ] Happy path walkthrough
- [ ] Edge case A
- [ ] Edge case B
- [ ] Error handling

---

## Rollout Plan

*(Delete if not applicable - useful for phased releases)*

### Phase 1: [Name]
- What: Limited scope or user group
- When: Target date
- Success Metrics: How we measure success

### Phase 2: [Name]
- What: Expanded scope
- When: Target date
- Success Metrics: How we measure success

---

## Monitoring & Metrics

*(Delete if not applicable)*

### Metrics to Track

- Metric 1: What we measure, why it matters
- Metric 2: What we measure, why it matters
- Metric 3: What we measure, why it matters

### Alerts/Monitoring

- Alert 1: Condition, severity, response
- Alert 2: Condition, severity, response

---

## Documentation Updates Needed

- [ ] User documentation: Where and what
- [ ] API documentation: Endpoints and examples
- [ ] Developer documentation: Implementation details
- [ ] README updates: Installation/configuration

---

## Status Changes

Track the evolution of this feature document:

- YYYY-MM-DD: Draft created
- YYYY-MM-DD: Reviewed, clarifications added
- YYYY-MM-DD: Approved by [name]
- YYYY-MM-DD: Implementation started
- YYYY-MM-DD: Implementation complete
- YYYY-MM-DD: Deployed to production

---

## Notes & Insights

Free-form section for capturing insights during definition and implementation:

- Learning 1: What we learned
- Insight 2: What worked well
- Challenge 3: What was difficult and how we solved it

---

**Template Version**: 1.0
**Last Updated**: 2025-11-30
**Source**: ~/workspace/docs/processes/templates/feature-template.md
