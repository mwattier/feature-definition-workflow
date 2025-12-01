# Feature Definition Methodology

A conversational approach to defining software features clearly before implementation.

---

## Purpose

This methodology ensures clear understanding before any code is written, preventing the costly "wait, that's not what I meant" moments that plague software development.

---

## The Problem We're Solving

### Context Drift

Large strategic documents and high-level requirements become confusing over time. What seemed clear at the start becomes ambiguous during implementation.

### Lost Understanding

Context gets lost between work sessions, especially in AI-assisted development where each session starts fresh.

### Unclear Relationships

Data models, entity relationships, and system boundaries remain fuzzy until implementation forces clarity - too late.

### Implementation Mismatch

What gets built doesn't match the original intent because assumptions went unstated and questions went unasked.

---

## The Solution: Conversational Definition

Before writing any code, have a structured conversation to define the feature clearly.

### Core Concept

**Don't write requirements alone - have a dialogue.**

The act of explaining a feature and answering clarifying questions reveals:
- Hidden assumptions
- Edge cases
- Simpler architectures
- Better approaches

---

## The Process Flow

### Step 1: Conceptual Explanation

**User → AI**: Explain the feature concept conversationally

**What to share**:
- The problem being solved
- Who will use this
- What the expected outcome is
- Any rough ideas about approach

**Don't worry about**:
- Perfect clarity upfront
- Complete details
- Technical specifics (those come through questions)

**Example**:
> "I need users to be able to export their data. They should be able to download it in different formats. Not sure exactly which formats yet, but probably CSV and JSON at minimum."

### Step 2: Clarifying Questions

**AI → User**: Ask targeted questions to reveal details

**Types of questions**:

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
- Are there existing patterns to follow?

**Example Exchange**:
> AI: "For the export feature - what formats are required? CSV and JSON only, or others?"
>
> User: "Start with CSV and JSON. Maybe Excel later."
>
> AI: "Should this be real-time download or queued for large datasets?"
>
> User: "Oh good point - probably queue anything over 1000 records."
>
> AI: "Who can export? All users or specific roles?"
>
> User: "Any authenticated user can export their own data. Admins can export any user's data."

### Step 3: Synthesis

**AI**: Synthesize conversation into structured feature document

**What to capture**:
- Purpose and problem statement
- User stories
- Conceptual flow (happy path, alternatives, errors)
- Data model
- Key questions asked and answers given
- Implementation notes
- What's explicitly out of scope
- Success criteria

**Format**: Use appropriate template (see [02-TEMPLATES.md](./02-TEMPLATES.md))

### Step 4: Review

**User**: Review synthesized document

**Check for**:
- Accuracy - Does this match your intent?
- Completeness - Are there gaps?
- Clarity - Will this make sense in 3 months?
- Feasibility - Can this actually be built?

**Iterate** until the document accurately captures the feature.

### Step 5: Finalize

**Both**: Mark document as approved

**What this means**:
- Specification is clear and agreed upon
- Implementation can proceed with confidence
- Document serves as reference during development
- Future sessions can reference this for context

### Step 6: Implementation

**AI** (or developer): Implement with clear context

**Benefits during implementation**:
- No guessing about requirements
- Edge cases already considered
- Data model already clear
- Scope boundaries defined

---

## Guidelines for Effective Conversations

### For Users

**1. Be Conversational**

Explain concepts as you would to a colleague, not formal documentation.

**Good**: "Users should be able to favorite items so they can find them quickly later"

**Less Good**: "The system shall provide functionality enabling users to mark resources as preferred for expedited retrieval"

**2. Think Out Loud**

Share uncertainties and possibilities. This helps the AI understand your thought process.

**Example**: "I'm thinking either we store this in the database or maybe just in Redis... probably database is safer long-term but Redis would be faster"

**3. Correct Immediately**

If the AI misunderstands, say so right away. Don't let misunderstandings compound.

**Example**: "No, that's not quite right - it's not a parent-child relationship, it's more like a many-to-many association"

**4. Use Examples**

Concrete examples clarify abstract concepts better than descriptions.

**Example**: "Like how Twitter handles mentions - you can mention multiple people in one tweet, and each person can be mentioned in multiple tweets"

**5. Ask Questions Back**

If something isn't clear to you, ask. The conversation should flow both ways.

**Example**: "Wait, if we do it that way, what happens to the child records when the parent is deleted?"

### For AI Assistants

**1. Ask Clarifying Questions**

Don't assume anything. Always verify understanding.

**Example**: "When you say 'export', do you mean a one-time download or ongoing synchronization?"

**2. Paraphrase Understanding**

Reflect back what you heard to confirm accuracy.

**Example**: "So if I understand correctly, you want templates to be tied to specific product types with no generic fallbacks - is that right?"

**3. Identify Ambiguities**

Call out when something could be interpreted multiple ways.

**Example**: "I'm not clear whether users can edit comments after posting, or if they're immutable once created"

**4. Synthesize Clearly**

Turn conversation into structured documentation that's easy to reference.

**5. Highlight Decisions**

Explicitly document choices made and alternatives considered.

**Example**: "Decision: Use database for persistence (considered Redis but chose database for data durability). Trade-off: Slightly slower but safer."

---

## When to Use This Process

### Always Use For

- ✅ New major features
- ✅ Unclear requirements
- ✅ Complex data relationships
- ✅ Multi-entity interactions
- ✅ User workflow changes
- ✅ API design
- ✅ Integration points
- ✅ Authentication/authorization features
- ✅ Features with business logic complexity

### Can Skip For

- ❌ Bug fixes with clear solution
- ❌ UI tweaks (color changes, spacing)
- ❌ Performance optimizations (unless architectural)
- ❌ Obvious enhancements
- ❌ Configuration changes
- ❌ Documentation updates

**When in doubt**: Use the process. The time investment is small compared to rework.

---

## Example Clarification Scenarios

### Scenario 1: Data Model Clarity

**Initial Request**: "Add comments to blog posts"

**Clarifying Questions**:
- Can users edit their comments after posting?
- Should comments be nested (replies to replies)?
- What happens to comments when the post is deleted?
- Who can see comments - public, registered users, specific roles?
- Do we need moderation capabilities?
- Is there a character limit?

**Result**: Clear specification preventing assumptions about editing, nesting, permissions, and moderation.

### Scenario 2: Flow Understanding

**Initial Request**: "Users should be able to import data from CSV"

**Clarifying Questions**:
- Should this be synchronous or queued for large files?
- What's the maximum file size we support?
- How do we handle invalid data - skip rows, fail entire import, or partial import?
- Do users get a preview before confirming import?
- How do we handle duplicate records?
- What feedback do users get about import progress/results?

**Result**: Complete understanding of import flow, error handling, and user feedback.

### Scenario 3: Architecture Decision

**Initial Request**: "Add caching to speed up the API"

**Clarifying Questions**:
- Which endpoints need caching - all or specific ones?
- What's the acceptable data staleness - seconds, minutes, hours?
- Do we need cache invalidation? If so, what triggers it?
- Is caching per-user or global?
- What's the expected cache hit rate needed to justify complexity?

**Result**: Discovered that only 3 endpoints need caching, staleness tolerance is high, and simple time-based expiration is sufficient.

---

## Success Metrics

This process is working when:

1. ✅ **Feature documents are unambiguous** - Anyone reading understands the intent
2. ✅ **Implementation matches intent** - What gets built is what was specified
3. ✅ **No "wait, that's not what I meant" moments** - Clarity achieved upfront
4. ✅ **Data models make sense later** - Relationships are clear months after creation
5. ✅ **New sessions can continue** - Context is preserved in documentation
6. ✅ **Questions reveal better design** - The conversation improves the solution

---

## Anti-Patterns to Avoid

### ❌ Skipping for "Simple" Features

**Problem**: Even simple features have hidden complexity.

**Example**: "Just add a delete button" seems simple, but raises questions about soft vs. hard delete, permissions, cascade behavior, undo capability, etc.

**Solution**: Quick conversation (5-10 minutes) still adds value.

### ❌ Assuming Shared Context

**Problem**: What's obvious to you isn't obvious to others (including AI).

**Example**: "Add product variants" assumes understanding of your domain's variant structure.

**Solution**: Be explicit about domain-specific concepts.

### ❌ Rushing the Conversation

**Problem**: Trying to save time by cutting questions short.

**Result**: Rework takes longer than the time saved.

**Solution**: Invest the time upfront.

### ❌ Not Documenting Why

**Problem**: Only documenting what was decided, not why.

**Result**: Future confusion about rationale.

**Solution**: Capture alternatives considered and reasoning.

### ❌ Ignoring Edge Cases

**Problem**: "We'll handle that later" for edge cases.

**Result**: Edge cases always show up in production.

**Solution**: Think through edge cases during definition.

---

## Integration with Development Workflow

### With Version Control

Feature documents should be versioned alongside code:

```
project/
├── docs/
│   └── features/
│       ├── 01-user-authentication.md
│       ├── 02-data-export.md
│       └── 03-api-caching.md
└── src/
    └── [implementation code]
```

### With Issue Tracking

Feature documents inform issue creation. See [04-ISSUE-INTEGRATION.md](./04-ISSUE-INTEGRATION.md).

### With Governance Levels

Adapt formality to project needs:

- **Rapid prototyping**: Use quick template, focus on core flow
- **Production systems**: Use standard template, comprehensive coverage
- **Regulated industries**: Add compliance sections, audit trail

### With Agentic Memory

Store key learnings in your agentic memory system (such as OpenMemory, mem0, or others):

**Examples**:
- "Pattern: Always ask about relationship cardinality early"
- "Decision: Nested UI management works well for parent-child entities in this domain"
- "Insight: Asking 'what happens when deleted?' often reveals cascade requirements"

---

## Adapting the Process

This methodology is a framework, not a rigid prescription.

**Adapt**:
- Template sections to your domain
- Formality level to your needs
- Question types to your technology
- Documentation depth to your governance

**Keep**:
- Conversational approach
- Clarifying questions before coding
- Structured synthesis
- Document decisions and rationale

---

## Next Steps

1. **Choose a template** → See [02-TEMPLATES.md](./02-TEMPLATES.md)
2. **Try defining a feature** → Use the conversational process
3. **Review the result** → Did it add clarity?
4. **Implement** → Build with clear specification
5. **Reflect** → Did it prevent rework?

---

**Remember**: The goal isn't perfect documentation - it's shared understanding that leads to correct implementation.
