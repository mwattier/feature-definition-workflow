# Citations & References

This methodology builds on research and best practices from the AI development community.

---

## Primary Inspirations

### Anthropic Research

**Effective Harnesses for Long-Running Agents**
- **Source**: Anthropic Engineering Blog
- **URL**: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- **Published**: 2025
- **Key Contributions**:
  - Single-feature focus prevents context window exhaustion
  - JSON over Markdown for state tracking
  - Bootstrap vs iteration agent patterns
  - Systematic feature progression

**What We Adapted**:
- Context window sizing constraints (features fit in 1-3 windows)
- features.json structure for tracking
- Hierarchical decomposition (phases → epics → features)
- Systematic progress tracking approach

**What We Added**:
- Conversational feature definition process
- Template system for documentation
- Integration between definition and tracking
- Skills for automated guidance

---

**Multi-Context Window Workflows**
- **Source**: Claude 4 Best Practices Documentation
- **URL**: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-4-best-practices#multi-context-window-workflows
- **Key Contributions**:
  - Filesystem-based context management
  - Structured progress files
  - Multi-session workflow patterns

**What We Adapted**:
- Feature documents as filesystem artifacts
- Structured tracking over compaction
- Session-to-session handoff patterns

**What We Added**:
- Conversational clarification before documentation
- Feature definition templates
- Integration with issue trackers

---

## Additional Influences

### Requirements Engineering Best Practices

**Conversational Requirements Elicitation**
- Clarifying questions reveal hidden assumptions
- Iterative refinement over upfront perfect specs
- Document WHY not just WHAT

**What We Applied**:
- Structured question types (data model, flow, scope, architecture)
- Conversation-first approach before documentation
- Decision rationale capture

---

### Agile & User Story Practices

**User Story Format**
- "As a [role], I want to [action], so that [benefit]"
- Acceptance criteria for clear "done" definition

**What We Adapted**:
- User story structure in templates
- Acceptance criteria as success metrics
- Iterative refinement mindset

**What We Changed**:
- Added extensive clarification conversation before story
- More detailed implementation notes
- Tighter integration with tracking

---

### MoSCoW Prioritization

**Method**: Must have, Should have, Could have, Won't have
- **Source**: Dai Clegg (1994)
- **Applied As**: Critical, High, Medium, Low priority levels

---

## Our Contributions

This methodology combines and extends these influences with:

1. **Conversational Feature Definition Process**
   - Structured dialogue before documentation
   - Question frameworks for different feature types
   - Template selection guidance

2. **Integration Framework**
   - Feature documents → features.json
   - Tracking system handoff patterns
   - Multi-tool integration (JSON, issues, memory systems)

3. **Large Project Decomposition**
   - Three-tier breakdown methodology
   - Context-window-sized feature splitting
   - Hierarchical progress tracking

4. **Claude Skills**
   - feature-definer for guided definition
   - project-breaker for decomposition
   - Automated workflow support

5. **Generic, Tool-Agnostic Approach**
   - Works with any tracking system
   - Adaptable to any governance level
   - No vendor lock-in

---

## Differences from Source Material

### Anthropic's Focus

- **Problem**: Context window exhaustion in long-running agent workflows
- **Solution**: Structured progress tracking, single-feature focus
- **Scope**: Implementation phase

### Our Focus

- **Problem**: Unclear requirements lead to rework
- **Solution**: Conversational clarification before implementation
- **Scope**: Definition phase → Implementation phase

### Integration

We connect the missing piece:

```
Requirements
    ↓
[Our Addition] Conversational Feature Definition
    ↓
Clear Specifications
    ↓
[Anthropic Pattern] Structured Implementation Tracking
    ↓
Systematic Progress
```

---

## Acknowledgments

**Anthropic Engineering Team**
- For publishing research on long-running agent patterns
- For detailed examples and practical guidance
- For multi-context window workflow insights

**AI Development Community**
- For exploring and sharing implementation patterns
- For feedback on conversational development approaches

---

## License

This methodology is shared under MIT License.

The underlying research and patterns from Anthropic remain under their respective licenses and copyrights.

---

## Further Reading

### From Anthropic

- **Building Effective Agents**: https://www.anthropic.com/research/building-effective-agents
- **Claude 4 Best Practices**: https://docs.anthropic.com/claude/docs/claude-4-best-practices
- **Prompt Engineering Guide**: https://docs.anthropic.com/claude/docs/prompt-engineering

### Related Topics

- **Requirements Engineering**: "Software Requirements" by Karl Wiegers & Joy Beatty
- **Agile User Stories**: "User Stories Applied" by Mike Cohn
- **Context Window Management**: Various AI community blog posts and research

---

## Contributing

Found other relevant sources or inspirations? Contributions to this citation list welcome.

Please include:
- Source name and author
- URL or publication details
- What aspect influenced this methodology
- How it was adapted or extended

---

**Last Updated**: 2025-11-30
