# Project Initializer Skill

This skill sets up a new project with the complete verification workflow structure. Run this when starting a new project or adding the verification workflow to an existing project.

---

## Skill Activation

Activate this skill when:
- User says "initialize project for feature workflow"
- User says "set up verification workflow"  
- User says "scaffold project structure"
- User is starting a new project that will use feature-definition-workflow

---

## Conversation Flow

### Step 1: Gather Project Information

```
I'll help you set up the verification workflow for your project.

First, I need some information:

1. Project name: [ask]
2. Brief description: [ask]  
3. Repository URL (optional): [ask]
4. Primary language/framework: [ask]
5. Does this project have multiple components/services? [yes/no]
6. Does this project integrate with external systems? [list them]
```

### Step 2: Identify Naming Conventions

```
What naming conventions should we enforce?

Database fields: [snake_case / camelCase / other]
API fields: [snake_case / camelCase / other]
Variables: [snake_case / camelCase / other]
File names: [kebab-case / snake_case / other]

Any exceptions? [ask]
```

### Step 3: Identify Type Conventions

```
What type conventions should we enforce?

Identifiers: [UUID / integer / string]
Timestamps: [datetime / ISO string / unix timestamp]
Money/currency: [Decimal / float / integer cents]

Primary database: [PostgreSQL / MySQL / MongoDB / other]
```

### Step 4: Confirm Structure

```
I'll create the following structure:

project/
├── ARCHITECTURE.md          # System structure and rules
├── features.json            # Feature tracking (v2 schema)
├── decisions/               # Decision logs
│   └── .gitkeep
├── verification/            # Verification checklists  
│   └── .gitkeep
├── checkpoints/             # Session checkpoints
│   └── .gitkeep
└── .claude/
    ├── CLAUDE.md            # Claude instructions
    └── commands/
        ├── pre-implement.md
        ├── verify-file.md
        ├── verify-feature.md
        ├── verification-status.md
        ├── checkpoint.md
        └── continue.md

Shall I proceed? [yes/no]
```

---

## File Generation

### ARCHITECTURE.md

Generate using the template from `templates/architecture-context.md`, populated with:
- Project name and description
- Components (if multi-component)
- External systems
- Naming conventions from Step 2
- Type conventions from Step 3
- Empty dependency map (to be filled as features are defined)

### features.json

Generate initial structure:

```json
{
  "version": "2.0",
  "project": {
    "name": "[project name]",
    "description": "[description]",
    "repository": "[repo URL or null]",
    "architecture_doc": "ARCHITECTURE.md"
  },
  "features": []
}
```

### .claude/CLAUDE.md

Generate using the template from `project-scaffold/.claude/CLAUDE.md`, populated with:
- Project name
- Naming conventions
- Type conventions
- Project-specific rules if any

### Claude Commands

Copy all commands from `project-scaffold/.claude/commands/`:
- pre-implement.md
- verify-file.md
- verify-feature.md
- verification-status.md
- checkpoint.md
- continue.md

### Directory Placeholders

Create `.gitkeep` files in:
- decisions/
- verification/
- checkpoints/

---

## Post-Initialization

After creating files:

```
Project initialized with verification workflow.

Created:
✓ ARCHITECTURE.md — Review and update component details
✓ features.json — Ready for features
✓ .claude/CLAUDE.md — Claude will follow these instructions
✓ .claude/commands/ — 6 commands installed
✓ decisions/ — Ready for decision logs
✓ verification/ — Ready for verification checklists
✓ checkpoints/ — Ready for session checkpoints

Next steps:
1. Review ARCHITECTURE.md and fill in any missing details
2. Define your first feature using /feature-define
3. Before implementing, run /pre-implement [feature-id]

The verification workflow is now active. Claude will:
- Require verification before implementing files
- Cross-reference all field names and types
- Stop on mismatches and ask for decisions
- Create checkpoints to preserve context

Would you like to define your first feature now?
```

---

## Adding to Existing Project

If project already has some structure:

```
I see this project already has some files. I'll add the verification workflow without overwriting existing content.

Existing files found:
- [list existing files]

I will:
- CREATE: .claude/CLAUDE.md (new)
- CREATE: .claude/commands/ (new directory)
- CREATE: verification/ (new directory)
- CREATE: checkpoints/ (new directory)
- CREATE: decisions/ (new directory)
- CREATE: features.json (new)
- CREATE: ARCHITECTURE.md (new — you'll need to fill in existing architecture)

I will NOT modify any existing files.

Proceed? [yes/no]
```

---

## Integration with feature-definer Skill

After project is initialized, the feature-definer skill should:

1. Check for features.json v2 schema
2. When defining features, include verification structure
3. After feature definition, prompt to run /pre-implement
4. After feature definition, prompt to run /pre-implement
5. Refuse to mark features as "ready for implementation" without verification setup

---

## Skill Metadata

```yaml
name: project-initializer
version: 1.0.0
description: Initialize project with verification workflow structure
triggers:
  - "initialize project"
  - "setup verification workflow"
  - "scaffold project"
  - "add verification to project"
dependencies:
  - feature-definer
outputs:
  - ARCHITECTURE.md
  - features.json
  - .claude/CLAUDE.md
  - .claude/commands/*
  - verification/
  - checkpoints/
  - decisions/
```
