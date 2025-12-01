# Feature Document Templates

Structured templates for documenting features clearly and completely.

---

## Purpose

Templates provide consistent structure for feature documentation while remaining flexible enough to adapt to different project needs.

---

## Available Templates

### 1. Standard Template

**File**: [templates/feature-template.md](./templates/feature-template.md)

**Use For**:
- Production systems
- Features with complexity
- Team collaboration
- Long-term maintenance
- Compliance requirements

**Sections Include**:
- Purpose & problem statement
- User stories with acceptance criteria
- Conceptual flow (happy path, alternatives, errors)
- Data model with relationships
- UI/UX notes
- API design (if applicable)
- Key questions & decisions
- Implementation notes
- Out of scope
- Dependencies
- Success criteria
- Testing plan
- Monitoring & metrics

**When to Use**: Default choice for most features

### 2. Quick Template

**File**: [templates/feature-template-quick.md](./templates/feature-template-quick.md)

**Use For**:
- Rapid prototyping
- Internal tools
- Simple features
- POCs and experiments
- Early-stage exploration

**Sections Include**:
- Purpose
- User story
- How it works
- Data model (simplified)
- Implementation notes
- Out of scope
- Success criteria

**When to Use**: Speed matters more than comprehensive documentation

---

## Template Selection Guide

| Project Type | Complexity | Template | Rationale |
|--------------|-----------|----------|-----------|
| Production API | High | Standard | Need comprehensive spec |
| Prototype | Low | Quick | Speed over detail |
| Enterprise System | High | Standard | Compliance & audit trail |
| Internal Tool | Medium | Quick or Standard | Depends on maintenance needs |
| Open Source | Medium-High | Standard | Community needs clarity |
| Regulated Industry | High | Standard + custom | Add compliance sections |

**When in doubt**: Start with Standard. You can always simplify.

---

## Adapting Templates

Templates are starting points, not rigid requirements.

### Add Sections

**Common additions**:
- **Security Considerations** - For sensitive features
- **Compliance Notes** - For regulated industries
- **Migration Plan** - For breaking changes
- **Rollback Strategy** - For high-risk features
- **Cost Analysis** - For infrastructure changes
- **Accessibility Notes** - For user-facing features

**Example Addition**:
```markdown
## Security Considerations

### Authentication
- Feature requires authenticated users
- API key OR session token accepted
- Rate limiting: 100 requests/minute per user

### Authorization
- Users can only access their own data
- Admins can access all data
- Audit log for admin access

### Data Protection
- Personal data encrypted at rest
- Export files include data classification headers
- Auto-deletion of exports after 7 days
```

### Remove Sections

If a section doesn't apply to your feature, remove it.

**Examples**:
- Remove "API Design" for UI-only features
- Remove "UI/UX Notes" for backend-only features
- Remove "Monitoring & Metrics" for simple features

### Modify Sections

Adapt section content to your domain.

**Example - E-commerce**:
Instead of generic "Data Model", use:
- Product Catalog Structure
- Order Flow
- Payment Integration
- Inventory Management

**Example - Data Pipeline**:
Instead of generic sections, use:
- Data Sources
- Transformation Logic
- Destination Schema
- Error Handling & Retry
- Data Quality Checks

---

## Using Templates Effectively

### Don't Fill Every Field

Templates show what's possible, not what's required.

**Include**: Sections relevant to your feature
**Omit**: Sections that don't apply
**Add**: Sections specific to your needs

### Focus on Clarity

The goal is clear understanding, not complete documentation.

**Good**: Clear, concise explanations
**Less Good**: Comprehensive but confusing documentation

### Document Decisions

Most important: Capture WHY, not just WHAT.

**Example**:
```markdown
## Key Decisions

**Decision**: Use database for export queue, not Redis

**Reasoning**:
- Exports can take minutes for large datasets
- Need persistence across system restarts
- Acceptable to trade some speed for reliability

**Alternatives Considered**:
- Redis: Faster but data loss risk on restart
- File system: Harder to query status
```

### Update as You Learn

Feature documents can evolve during implementation.

**When to update**:
- Discovery of new edge cases
- Architecture changes
- Scope adjustments
- Implementation insights

**Mark updates**:
```markdown
## Status Changes

- 2025-11-30: Draft created
- 2025-11-30: Approved by team
- 2025-12-01: Updated with queue timeout decision
- 2025-12-05: Implementation complete
```

---

## Template Sections Explained

### Purpose

**What**: High-level explanation of the feature
**Why**: The problem being solved
**Who**: Target users or beneficiaries

**Example**:
```markdown
## Purpose

**Problem**: Users frequently export large datasets (10,000+ records)
and experience browser timeouts waiting for CSV generation.

**Solution**: Queue large exports for background processing and notify
users when ready for download.

**Users**: All authenticated users exporting data
```

### User Story

**Format**: As a [role], I want to [action], so that [benefit]

**Include**:
- Clear role/persona
- Specific action
- Tangible benefit
- Acceptance criteria

**Example**:
```markdown
## User Story

**As a** data analyst
**I want to** export large datasets without browser timeouts
**So that** I can download complete data for offline analysis

**Acceptance Criteria**:
- [ ] Exports >1000 records are queued automatically
- [ ] User receives email when export is ready
- [ ] Download link expires after 7 days
- [ ] User can see export status in dashboard
```

### Conceptual Flow

**What**: Step-by-step description of how the feature works

**Include**:
- Happy path (normal flow)
- Alternative paths (valid variations)
- Error cases (what can go wrong)

**Be specific about**:
- Who does what
- What triggers what
- What feedback users get

**Example**:
```markdown
## Conceptual Flow

### Happy Path
1. User clicks "Export to CSV" with 5,000 records selected
2. System detects >1000 records, queues export job
3. User sees message: "Export queued. You'll receive an email when ready."
4. Background worker generates CSV (est. 2-3 minutes)
5. User receives email with download link
6. User clicks link, downloads CSV file
7. File auto-deletes after 7 days

### Alternative Path: Small Export
1. User clicks "Export to CSV" with 500 records
2. System generates CSV immediately (< 5 seconds)
3. Browser downloads file directly
4. No email, no queue

### Error Case: Export Fails
1. Export queued successfully
2. Background worker encounters error (DB timeout, OOM, etc.)
3. Job marked as failed
4. User receives email: "Export failed. Please try again or contact support."
5. User can retry from dashboard
```

### Data Model

**What**: Entities, fields, and relationships involved

**Include**:
- Entity names and purpose
- Key fields with types
- Relationships (1:1, 1:n, n:m)
- Validation rules

**Visual diagrams helpful**:
```markdown
## Data Model

### Entities

**ExportJob**
- id: UUID - Primary key
- user_id: UUID - Foreign key to User
- status: enum[queued, processing, completed, failed]
- record_count: integer - Number of records to export
- file_path: string (nullable) - S3 path when complete
- error_message: string (nullable) - If failed
- created_at: timestamp
- completed_at: timestamp (nullable)

**User**
- id: UUID
- email: string
- name: string

### Relationships
```
[User] --1:n--> [ExportJob]
```

A user can have many export jobs.
An export job belongs to one user.

### Validation Rules
- record_count must be > 0
- status transitions: queued → processing → (completed | failed)
- file_path required if status = completed
- error_message required if status = failed
```

### Key Questions & Decisions

**Most important section**: Document the conversation.

**Include**:
- Questions asked during definition
- Answers given
- Decisions made
- Alternatives considered
- Rationale for choices

**Example**:
```markdown
## Key Questions & Decisions

**Q**: Should exports be queued or synchronous?
**A**: Queue exports >1000 records, synchronous for smaller
**Reasoning**: Prevents browser timeouts while keeping small exports fast
**Alternative Considered**: Queue all exports (rejected: unnecessary for small datasets)

**Q**: How long should download links remain valid?
**A**: 7 days
**Reasoning**: Balance between user convenience and storage costs
**Alternative Considered**: 30 days (rejected: storage costs too high)

**Q**: What formats should we support?
**A**: CSV only for MVP, JSON in future
**Reasoning**: CSV is most requested format, covers 90% of use cases
**Future Consideration**: Add JSON, Excel in Phase 2
```

### Out of Scope

**Critical section**: Explicitly state what's NOT included.

**Prevents**:
- Scope creep
- Misunderstandings
- Feature bloat

**Example**:
```markdown
## Out of Scope

- ❌ Excel format (future: Phase 2)
- ❌ Scheduled/recurring exports (different feature)
- ❌ Custom column selection (use existing filters instead)
- ❌ Export templates (may never implement - low demand)
- ❌ Exporting other users' data (security concern)
```

---

## Common Pitfalls

### ❌ Too Much Upfront Detail

**Problem**: Trying to specify every implementation detail

**Solution**: Focus on what, not how. Implementation details emerge during development.

### ❌ Not Enough Context

**Problem**: Assuming everyone has your domain knowledge

**Solution**: Explain domain concepts clearly.

### ❌ Forgetting Edge Cases

**Problem**: Only documenting happy path

**Solution**: Always ask "What could go wrong?"

### ❌ Missing the Why

**Problem**: Documenting decisions without rationale

**Solution**: Always include reasoning for choices.

---

## Next Steps

1. **Choose your template** based on project needs
2. **Start a conversation** about your feature
3. **Fill in sections** as understanding develops
4. **Review with stakeholders** to ensure alignment
5. **Refine** based on feedback
6. **Approve** when specification is clear
7. **Implement** with confidence

---

## Related Documentation

- [01-METHODOLOGY.md](./01-METHODOLOGY.md) - The conversational process
- [03-PROJECT-BREAKDOWN.md](./03-PROJECT-BREAKDOWN.md) - Breaking large projects into features
- [04-ISSUE-INTEGRATION.md](./04-ISSUE-INTEGRATION.md) - Connecting to tracking systems
- [examples/](./examples/) - Real feature document examples

---

**Remember**: Templates are tools to help, not rules to follow rigidly. Adapt to your needs.
