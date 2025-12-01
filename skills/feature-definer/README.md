# Feature Definer Skill

A Claude Code skill for guiding conversational feature definition before implementation.

---

## What This Does

This skill helps you define features clearly through structured conversation **before** writing any code. It prevents:

- Context drift and misunderstanding
- "Wait, that's not what I meant" moments
- Unclear data models and relationships
- Hours of rework

**Time Investment**: 15-45 minutes of conversation
**Time Saved**: Hours of rework and confusion

---

## Installation

### To Your Project

```bash
cd ~/your-project
mkdir -p .claude/skills
cp -r path/to/feature-definition-workflow/skills/feature-definer .claude/skills/
```

### To Your Workspace

```bash
mkdir -p ~/.claude/skills
ln -s path/to/feature-definition-workflow/skills/feature-definer ~/.claude/skills/feature-definer
```

---

## Usage

Just ask Claude:
- "Help me define a new feature"
- "I need to plan [feature name]"
- "Let's use the feature definition process"
- "Define a feature for user authentication"

Claude will automatically trigger this skill and guide you through the process.

---

## How It Works

1. **You explain** the feature concept conversationally
2. **Claude asks** clarifying questions about:
   - Data models and relationships
   - User flows and edge cases
   - Scope and boundaries
   - Architecture decisions
3. **Claude synthesizes** a structured feature document
4. **You review** and correct any misunderstandings
5. **Feature is approved** and ready for implementation

---

## Templates

The skill uses two templates:

### Standard Template
- Comprehensive documentation
- For production systems
- ~20 sections including API design, testing, monitoring

### Quick Template
- Lightweight documentation
- For prototypes and POCs
- ~8 core sections

Claude will help you choose the right one based on your needs.

---

## Example Session

```
You: "I need to add data export functionality"

Claude: "I'll help you define this feature. Let me ask some questions:

1. What formats should we support - CSV, JSON, others?
2. Should exports be real-time or queued for large datasets?
3. Who can export - all users or specific roles?
4. How long should download links remain valid?
5. Do we need to track who exported what?"

[You answer questions]

Claude: "Based on our conversation, I'll create a feature document.
Which template - standard or quick?"

You: "Standard"

Claude: [Creates comprehensive feature document]

"Here's the feature document. Does this match your intent?"

[You review and approve]

Claude: "Great! Would you like me to create a features.json entry
for tracking implementation?"
```

---

## Benefits

### Before Implementation

- ✅ **Clear understanding** - Shared clarity between human and AI
- ✅ **Better decisions** - Questions reveal superior approaches
- ✅ **Documented rationale** - Why choices were made
- ✅ **Edge cases covered** - Thought through upfront

### During Implementation

- ✅ **No rework** - Building the right thing the first time
- ✅ **Context preserved** - Documentation survives sessions
- ✅ **Systematic progress** - Clear specification to reference

---

## Integration

Works with:

- **features.json** - For structured tracking
- **GitHub Issues** - For collaboration
- **Jira/Linear** - For enterprise workflows
- **project-breaker skill** - For large project decomposition

---

## Files

```
feature-definer/
├── SKILL.md                   # Skill definition for Claude
├── README.md                  # This file
└── templates/                 # (Copied from parent workflow)
    ├── feature-template.md
    └── feature-template-quick.md
```

---

## Related Documentation

- **Main Methodology**: `../../01-METHODOLOGY.md`
- **Template Guide**: `../../02-TEMPLATES.md`
- **Project Breakdown**: `../../03-PROJECT-BREAKDOWN.md`

---

## Contributing

Improvements and examples welcome! This skill is part of the feature-definition-workflow methodology.

---

## License

MIT License - Part of feature-definition-workflow

---

**Remember**: The goal isn't perfect documentation - it's shared understanding that leads to correct implementation.
