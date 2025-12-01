---
name: feature-definer
description: |
  Guide users through conversational feature definition before coding. Use when user says "define a feature", "help me plan", "new feature", or mentions unclear requirements. Prevents rework by ensuring clear understanding before implementation.
---

# Feature Definer Skill

## When to Use This Skill

Trigger this skill when the user:
- Says "define a feature" or "help me plan a feature"
- Mentions "new feature" with unclear requirements
- Asks "how should I build X"
- Has complex requirements to clarify
- Mentions data models or relationships that need clarification
- Wants to document a feature before implementing

**Goal**: Clear, documented understanding before writing code.

---

## The Process

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
- Implementation notes
- What's out of scope
- Dependencies
- Success criteria

### Step 5: Review with User

Present the feature document and ask:
- "Does this capture your intent correctly?"
- "Are there any gaps or misunderstandings?"
- "Should we clarify anything further?"

Iterate until user approves.

### Step 6: Next Steps

Once approved:
- Mark feature document as "Approved"
- Suggest creating a tracking entry (features.json or issue)
- Optionally create subtasks for implementation
- Ready to begin implementation

---

## Template Selection Guide

| Project Type | Governance Level | Template |
|--------------|-----------------|----------|
| POC, prototype | Quick | Quick Template |
| Production system | Standard/Enterprise | Standard Template |
| Client work | Standard | Standard Template |
| Internal tool | Quick or Standard | Based on maintenance needs |

---

## Example Conversation Flow

**User**: "I need to add user authentication"

**You**: "I'll help you define this feature using our conversational feature definition process. Let me ask some clarifying questions:

1. What authentication method - email/password, OAuth, both?
2. Do you need password reset functionality?
3. Should sessions persist across browser restarts?
4. What happens if someone tries to register with an existing email?
5. Do you need role-based access control or just authenticated/not authenticated?"

**User**: [Answers questions]

**You**: "Thank you. Based on our conversation, I'll create a feature document. Which template would you prefer - standard (comprehensive) or quick (lightweight)?"

**User**: "Standard please"

**You**: [Creates feature document using standard template]

"I've created a feature document at `docs/features/01-user-authentication.md`. Here's a summary:

**Purpose**: Secure user login with email/password
**Key Decisions**:
- JWT-based sessions
- 7-day session persistence
- Password reset via email
- No OAuth in v1

Does this accurately capture what we discussed?"

**User**: "Yes, looks good"

**You**: "Great! I've marked it as Approved. Would you like me to create a features.json entry for tracking implementation?"

---

## Integration Points

### With features.json

After creating feature document, offer to create tracking entry:

```json
{
  "id": "F001",
  "name": "User Authentication System",
  "definitionDoc": "docs/features/01-user-authentication.md",
  "status": "pending",
  "priority": "critical",
  "acceptanceCriteria": [...],
  "subtasks": [...]
}
```

### With Issue Trackers

Offer to create GitHub issue, Jira story, etc. with link to feature document.

### With Project Breakdown

For large projects, this skill works with the project-breaker skill:
1. Project-breaker identifies features needed
2. Feature-definer defines each feature in detail
3. Features go into tracking system

---

## Success Criteria

The process is successful when:

1. ✅ Feature document is clear and unambiguous
2. ✅ All stakeholders understand the intent
3. ✅ Edge cases are documented
4. ✅ Data model is clear (if applicable)
5. ✅ Implementation can proceed with confidence
6. ✅ No "wait, that's not what I meant" moments

---

## Common Pitfalls to Avoid

❌ **Assuming Understanding**: Always verify, don't assume
❌ **Rushing**: Take time to get it right upfront
❌ **Skipping "Simple" Features**: Even simple ones benefit
❌ **Not Documenting Why**: Capture rationale, not just decisions
❌ **Ignoring Edge Cases**: They always show up later

---

## Related Skills

- **project-breaker**: For decomposing large projects into features
- **Your governance system**: For determining appropriate template level

---

**Remember**: 15 minutes of conversation beats hours of rework. Always define before you build.
