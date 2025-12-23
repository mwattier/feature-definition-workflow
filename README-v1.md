# Feature Definition Workflow

A conversational methodology for defining software features clearly before implementation, integrated with systematic project breakdown and issue tracking.

**Core Principle**: 15 minutes of conversation prevents hours of rework.

## My Honest Assessment

I suggest reading [HONEST-ASSESSMENT](./HONEST-ASSESSMENT.md) at some point in browsing this repo. 

---

## The Problem

When building features with AI assistance (or any development approach), common issues arise:

- **"Wait, that's not what I meant"** - Rework after implementation
- **Context drift** - Understanding lost between sessions
- **Unclear requirements** - Building the wrong thing
- **Model confusion** - Data relationships unclear
- **Implementation mismatch** - Code doesn't match intent
- **Lost decisions** - Why did we choose this approach?

---

## The Solution

A structured approach combining:

1. **Conversational Feature Definition** - Clarify through dialogue before coding
2. **Feature Documentation** - Create structured specifications
3. **Project Breakdown** - Decompose large projects into manageable features
4. **Issue Integration** - Handoff to tracking systems (features.json, GitHub, Jira, etc.)

---

## How It Works

### Phase 1: Feature Definition (15-45 minutes)

```
User explains concept
    ↓
AI asks clarifying questions
    ↓
Synthesize into feature document
    ↓
Review and refine
    ↓
Approve specification
```

### Phase 2: Project Breakdown

```
Large project requirements
    ↓
Break into discrete features
    ↓
Define dependencies
    ↓
Prioritize implementation order
```

### Phase 3: Implementation Tracking

```
Feature document
    ↓
Create tracking entry (JSON/Issue)
    ↓
Implement with clear specification
    ↓
Update progress systematically
```

---

## What's Included

### Documentation

- **[01-METHODOLOGY.md](./01-METHODOLOGY.md)** - Complete feature definition process
- **[02-TEMPLATES.md](./02-TEMPLATES.md)** - Feature document templates and guidance
- **[03-PROJECT-BREAKDOWN.md](./03-PROJECT-BREAKDOWN.md)** - Breaking large projects into features
- **[04-ISSUE-INTEGRATION.md](./04-ISSUE-INTEGRATION.md)** - Connecting to tracking systems

### Templates

- **Standard Template** - Comprehensive feature documentation
- **Quick Template** - Lightweight for rapid iteration
- **features.json Schema** - JSON-based tracking format
- **Example features.json** - Sample implementation

### Claude Skills

- **feature-definer** - Guided conversational definition
- **project-breaker** - Large project decomposition

### Examples

- Generic feature examples demonstrating the methodology
- Sample features.json with multiple features

### Scripts

- **validate-features.py** - Validate features.json structure and content
- Comprehensive checking of required fields, data types, dependencies
- Integration examples for CI/CD, pre-commit hooks

### Extras

- **Context management patterns** - Session file templates and scripts
- **refresh-context.sh** - Generate context summaries from session files
- Session file examples (SESSION-CURRENT, ACTIVE-PROJECTS, etc.)
- Insight into the larger workspace methodology

---

## Quick Start

### 1. Read the Methodology

Start with [01-METHODOLOGY.md](./01-METHODOLOGY.md) to understand the process.

### 2. Choose Your Template

See [02-TEMPLATES.md](./02-TEMPLATES.md) for template selection guidance.

### 3. Define Your First Feature

Use the conversational approach or install the Claude skill for guided assistance.

### 4. Set Up Tracking

See [04-ISSUE-INTEGRATION.md](./04-ISSUE-INTEGRATION.md) for integration with your tracking system.

---

## Key Benefits

### Before Implementation

- ✅ **Clear understanding** - Shared clarity between human and AI
- ✅ **Better decisions** - Questions reveal superior approaches
- ✅ **Documented rationale** - Why choices were made
- ✅ **Edge cases covered** - Thought through upfront

### During Implementation

- ✅ **No rework** - Building the right thing the first time
- ✅ **Context preserved** - Documentation survives sessions
- ✅ **Systematic progress** - Track completion objectively
- ✅ **Prevented drift** - Clear specification to reference

### Long Term

- ✅ **Future clarity** - Understand decisions months later
- ✅ **Team alignment** - Clear specs for collaboration
- ✅ **Onboarding ease** - New people understand quickly
- ✅ **Technical debt prevention** - Intentional architecture

---

## Real-World Success Pattern

### Without This Process

```
Build feature based on rough idea
    ↓
Implement interpretation of requirements
    ↓
User: "That's not what I wanted"
    ↓
Refactor/rebuild (2-3+ hours lost)
```

### With This Process

```
20-minute conversation with clarifying questions
    ↓
Discover simpler/better architecture
    ↓
Implement correct solution first time
    ↓
Zero rework needed
```

**ROI**: Small time investment upfront prevents significant rework.

---

## Methodology Principles

### 1. Conversation Over Documentation

Don't write requirements alone - have a dialogue. Questions reveal better solutions.

### 2. Explicit Over Implicit

State assumptions clearly. "I think you mean X" prevents misunderstanding.

### 3. Questions Improve Design

Clarifying questions often reveal simpler, better approaches.

### 4. Document Decisions

Capture not just what was decided, but why.

### 5. Structured Yet Flexible

Templates provide structure, but adapt to your needs.

---

## Integration Points

This methodology works with:

- **Any AI assistant** - Claude, ChatGPT, etc.
- **Any tracking system** - features.json, GitHub Issues, Jira, Linear, etc.
- **Any governance level** - Adapt formality to project needs
- **Any agentic memory system** - OpenMemory, mem0, or others
- **Any project type** - Web, mobile, data pipelines, infrastructure, etc.

---

## Credits & Inspiration

This methodology builds on research and best practices from:

- Anthropic's work on effective long-running agent workflows
- Real-world experience with AI-assisted development
- Proven patterns for requirements clarification

See [CITATIONS.md](./CITATIONS.md) for detailed references.

---

## Getting Started

1. **Understand the Process** → [01-METHODOLOGY.md](./01-METHODOLOGY.md)
2. **Learn the Templates** → [02-TEMPLATES.md](./02-TEMPLATES.md)
3. **Try an Example** → [examples/](./examples/)
4. **Set Up Tracking** → [04-ISSUE-INTEGRATION.md](./04-ISSUE-INTEGRATION.md)

---

## Contributing

This methodology is shared openly to help developers avoid rework and build better software with AI assistance.

Improvements, examples, and adaptations are welcome.

---

## License

MIT License - Copyright Mike Wattier https://selltinfoil.com

See LICENSE file for details.

---

**Remember**: The goal isn't perfect documentation - it's shared understanding that leads to correct implementation.
