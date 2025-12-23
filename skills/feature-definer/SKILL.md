---
name: feature-definer
version: 2.0.0
description: |
  Guide users through conversational feature definition with v2 verification workflow. Use when user says "define a feature", "help me plan", "new feature", or mentions unclear requirements. Prevents rework by ensuring clear understanding before implementation.
---

# Feature Definer Skill (v2)

## When to Use This Skill

Trigger this skill when the user:
- Says "define a feature" or "help me plan a feature"
- Mentions "new feature" with unclear requirements
- Asks "how should I build X"
- Has complex requirements to clarify
- Mentions data models or relationships that need clarification
- Wants to document a feature before implementing

**Goal**: Clear, documented understanding with verification structure before writing code.

---

## The Process (v2 Enhanced)

### Step 0: Check for v2 Verification Workflow

**BEFORE starting feature definition**, check if project has v2 structure:

```
Look for:
- features.json with "version": "2.0"
- ARCHITECTURE.md exists
- verification/ directory exists
- .claude/commands/ directory exists
```

**If v2 structure exists**: Follow v2 workflow (includes verification setup)
**If v1 or no structure**: Suggest running project-initializer skill first

---

### Step 1: Understand the Context

Ask the user:
1. What problem are they solving?
2. Who is the user/audience?
3. What's the expected outcome?

**Example Questions**:
- "Can you explain what you're trying to build?"
- "Who will use this feature?"
- "What problem does this solve?"

### Step 2: Clarify Through Conversation

Ask targeted clarifying questions based on the feature type.

**Data Model Questions**:
- How are entities X and Y related?
- Is this a 1:1, 1:n, or n:m relationship?
- Should this field be nullable?
- What happens when we delete X?
- What's the primary identifier?
- **v2 NEW**: What are the exact field names and types?

**Flow Questions**:
- What happens if [edge case]?
- Can the user skip this step?
- Who can perform this action?
- What's the failure case?
- What notifications are needed?
- Is this synchronous or asynchronous?

**Scope Questions**:
- Does this feature handle X?
- Is Y in scope or future?
- What's the MVP vs. nice-to-have?
- What can we defer?

**Architecture Questions**:
- Why this approach over alternatives?
- What are the trade-offs?
- How does this scale?
- What dependencies does this introduce?

**v2 NEW - Implementation Questions**:
- What files will need to be created?
- What files will need to be modified?
- What are the dependencies between these files?
- Are there existing schemas/types that must be used?

### Step 3: Select Appropriate Template

Based on project governance and complexity:

**Standard Template**: For production systems, comprehensive documentation needed
**Quick Template**: For prototypes, POCs, rapid iteration

Ask the user which template fits their needs if unclear.

### Step 4: Synthesize into Feature Document

Create a feature document using the selected template. Fill in:

- Purpose & problem statement
- User stories
- Conceptual flow (happy path, alternatives, errors)
- Data model (if applicable)
- Key questions and answers from conversation
- **v2 NEW**: Implementation plan section with files to create/modify
- **v2 NEW**: Dependencies section (internal and external)
- What's out of scope
- Success criteria

### Step 5: Review with User

Present the feature document and ask:
- "Does this capture your intent correctly?"
- "Are there any gaps or misunderstandings?"
- "Should we clarify anything further?"

Iterate until user approves.

### Step 6: Create features.json Entry (v2 Format)

**For v2 projects**, create entry with verification structure:

```json
{
  "id": "feature-id",
  "title": "Feature Title",
  "status": "defined",
  "priority": "high|medium|low",
  "description": "Brief description",
  "feature_doc": "features/feature-id.md",
  "created": "YYYY-MM-DD",
  "updated": "YYYY-MM-DD",
  "verification": {
    "file": null,
    "status": "PENDING",
    "last_updated": null
  },
  "files": [],
  "decisions": [],
  "checkpoints": [],
  "current_checkpoint": null
}
```

**For v1 projects**, use standard format (no verification fields).

### Step 7: Next Steps (v2 Enhanced)

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
```

**For v1 projects**:
```
✅ Feature defined and documented
✅ Added to features.json

Ready to begin implementation.
```

---

## v2 Verification Rules

### Feature Status Enforcement

**"defined"**: Feature document exists, not verified
**"ready"**: Verification checklist exists, ready to implement
**"in-progress"**: Implementation started
**"completed"**: All files verified and tested

**IMPORTANT**:
- A feature CANNOT move from "defined" to "ready" without running `/pre-implement`
- A feature CANNOT move to "completed" without all files having `verification_status: "VERIFIED"`

If user asks to mark feature as "ready" without verification setup:
```
⚠️ Cannot mark feature as ready without verification setup.

This feature needs:
1. Verification checklist (verification/[feature-id].md)
2. File dependency mapping
3. Implementation order established

Please run: /pre-implement [feature-id]

This prevents the $400 mistakes. The workflow exists for a reason.
```

### File Identification Requirement

**For v2 projects**, during Step 4 (feature document creation), you MUST include:

**"Files to Create/Modify" section**:
```markdown
## Files to Create/Modify

| File | Action | Purpose |
|------|--------|---------|
| schema/product.py | CREATE | Product data model |
| services/writer.py | CREATE | Write product data |
| services/reader.py | MODIFY | Add product reading |
| tests/test_product.py | CREATE | Product tests |
```

This list feeds into `/pre-implement` for dependency analysis.

---

## Template Selection Guide

| Project Type | Governance Level | Template | Verification |
|--------------|-----------------|----------|--------------|
| POC, prototype | Quick | Quick Template | Optional (v2) |
| Production system | Standard/Enterprise | Standard Template | Required (v2) |
| Client work | Standard | Standard Template | Required (v2) |
| Internal tool | Quick or Standard | Based on needs | Based on needs |

---

## Example Conversation Flow (v2)

**User**: "I need to add user authentication"

**You**: "I'll help you define this feature. I see this project has v2 verification workflow enabled.

Let me ask some clarifying questions:

1. What authentication method - email/password, OAuth, both?
2. Do you need password reset functionality?
3. Should sessions persist across browser restarts?
4. What happens if someone tries to register with an existing email?
5. Do you need role-based access control or just authenticated/not authenticated?
6. **NEW**: What files will need to be created or modified for this?"

**User**: [Answers questions including file list]

**You**: "Thank you. Based on our conversation, I'll create a feature document. Which template would you prefer - standard (comprehensive) or quick (lightweight)?"

**User**: "Standard please"

**You**: [Creates feature document using standard template with "Files to Create/Modify" section]

"I've created a feature document at `features/user-authentication.md`. Here's a summary:

**Purpose**: Secure user login with email/password
**Key Decisions**:
- JWT-based sessions
- 7-day session persistence
- Password reset via email
- No OAuth in v1

**Files to Create/Modify**:
- schema/user.py (CREATE)
- services/auth_service.py (CREATE)
- api/routes/auth.py (CREATE)
- tests/test_auth.py (CREATE)

Does this accurately capture what we discussed?"

**User**: "Yes, looks good"

**You**: "Great! I've added this feature to features.json.

✅ Feature defined: user-authentication
📄 Document: features/user-authentication.md

**Next step**: Run verification setup
→ /pre-implement user-authentication

This will create the verification checklist and dependency map. Do NOT start implementing until this is complete."

---

## Integration Points

### With features.json (v2)

After creating feature document, automatically create v2 tracking entry with:
- Feature metadata
- Verification structure (empty, to be filled by /pre-implement)
- Empty files array (to be filled by /pre-implement)
- Status: "defined"

### With project-initializer Skill

If project lacks v2 structure:
```
I notice this project doesn't have v2 verification workflow set up.

Would you like me to initialize it? This adds:
- Verification checklists
- Dependency tracking
- Session checkpoints
- Slash commands for verification

This prevents costly type/field mismatches during implementation.

Run: [invoke project-initializer skill]
```

### With Issue Trackers

Still offer to create GitHub issue, Jira story, etc. with link to feature document.

### With Project Breakdown

For large projects:
1. Project-breaker identifies features needed
2. Feature-definer defines each feature in detail (with v2 structure)
3. Features go into features.json with verification fields
4. Each feature runs /pre-implement before implementation

---

## v2 Workflow Checklist

When defining a feature in a v2 project, ensure:

- [ ] Feature document created with "Files to Create/Modify" section
- [ ] Feature added to features.json with v2 schema
- [ ] Verification structure initialized (empty)
- [ ] User instructed to run /pre-implement next
- [ ] User warned NOT to implement without verification setup

---

## Success Criteria (v2 Enhanced)

The process is successful when:

1. ✅ Feature document is clear and unambiguous
2. ✅ All stakeholders understand the intent
3. ✅ Edge cases are documented
4. ✅ Data model is clear (if applicable)
5. ✅ **v2 NEW**: Files to create/modify are listed
6. ✅ **v2 NEW**: Dependencies are identified
7. ✅ **v2 NEW**: Feature added to features.json with verification structure
8. ✅ **v2 NEW**: User knows to run /pre-implement next
9. ✅ Implementation can proceed with confidence
10. ✅ No "wait, that's not what I meant" moments

---

## Common Pitfalls to Avoid

❌ **Assuming Understanding**: Always verify, don't assume
❌ **Rushing**: Take time to get it right upfront
❌ **Skipping "Simple" Features**: Even simple ones benefit
❌ **Not Documenting Why**: Capture rationale, not just decisions
❌ **Ignoring Edge Cases**: They always show up later
❌ **v2 NEW**: Letting user skip /pre-implement ("I'll just start coding")
❌ **v2 NEW**: Not listing files in feature document
❌ **v2 NEW**: Marking feature "ready" without verification setup

---

## Related Skills

- **project-initializer**: For adding v2 verification workflow to projects
- **project-breaker**: For decomposing large projects into features
- **Your governance system**: For determining appropriate template level

---

## Version History

**v2.0.0** (2025-12-22):
- Added v2 verification workflow integration
- Added requirement to list files in feature document
- Added /pre-implement prompt after feature definition
- Added enforcement rules (can't mark "ready" without verification)
- Added checks for v2 project structure

**v1.0.0**: Original conversational feature definition

---

**Remember**: 15 minutes of conversation beats hours of rework. With v2, we also prevent $400 mistakes through verification. Always define, verify, then build.
