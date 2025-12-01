# Context Management Extras

This directory contains additional files and scripts that support the larger workspace method we've developed but aren't core to the feature definition workflow itself. Consider these "bonus materials" that provide insight into how we manage AI context across sessions.

---

## The Context Problem

When working with AI agents across multiple sessions, you quickly run into a challenge: **how do you resume work efficiently without burning thousands of tokens re-reading everything?**

In a typical solo developer workspace with dozens of projects, you might have:
- 600+ markdown files
- 40+ MB of documentation
- Multiple active projects
- Historical context you want preserved but don't need every session

If the AI reads everything at session start, you waste tokens and time. If it reads nothing, it lacks context. We needed a middle ground.

---

## Our Solution: Layered Context

We developed a multi-file context system that gives the AI **just enough** context to resume work effectively, with clear pointers to deeper information when needed.

### The Four Context Files

**1. SESSION-CURRENT.md** (~2-3KB)
- What you're working on RIGHT NOW
- Today's completed work
- Immediate next steps
- Read this FIRST every session

**2. ACTIVE-PROJECTS.md** (~1-2KB)
- List of active projects with quick links
- Current phase/status for each
- Quick start commands
- Read when switching projects

**3. SESSION-RECENT.md** (~1KB)
- Last 7 days of work
- Recent completions
- Important decisions made
- Quick historical context

**4. MCP-QUICK-REF.md** (~1KB)
- MCP server usage examples
- Common commands
- Troubleshooting tips
- Read when using MCP features

**Total**: ~5-7KB instead of 40+ MB

---

## The refresh-context.sh Script

We also created a script that generates a **context summary** by pulling key information from these files plus git history and project status.

**What it does:**
- Extracts current work from SESSION-CURRENT.md
- Shows last 5 git commits
- Lists active projects and their status
- Checks features.json for in-progress features
- Identifies any blockers
- Surfaces next actions

**When to use it:**
- Start of a new session (generates fresh summary)
- After long break (what was I doing?)
- Context refresh mid-session (re-orient)

**Example output:**
```markdown
# Context Refresh Summary

Generated: 2025-11-30 10:15:23

## 🎯 CURRENT SESSION
Project: project-name
Focus: Feature F012 implementation
Status: 60% complete

## 📝 RECENT COMMITS
abc123f Add feature-benefit mapping schema
def456a Implement attribute context service
...

## 🚧 ACTIVE PROJECTS
**project-name**: Phase 1 - Foundation (80% complete)

## 📊 FEATURE STATUS
**project-name**:
  - [60%] F012: Feature-Benefit Mapping System

## ⏭️  NEXT ACTIONS
1. Complete mapping service tests
2. Build Filament UI for rule management
3. Integrate with content generation
```

The script is generic and project-agnostic - it looks for features.json in any project directory and extracts status automatically.

---

## Why This Matters for Feature Definition

When you're defining features conversationally (as this methodology teaches), context matters enormously:

- **Previous decisions** inform new features
- **Project architecture** constrains implementation
- **Dependencies** between features must be tracked
- **Progress** determines priority

The session files ensure the AI has this context without drowning in documentation.

**Integration with features.json:**
- Session files track "what's happening"
- features.json tracks "what needs to happen"
- Together they provide complete project context

---

## Session Start Workflow

Here's the pattern we use:

### At Session Start
1. AI reads SESSION-CURRENT.md first (2KB)
2. AI queries MCP memory for session handoffs (if using OpenMemory, mem0 or other)
3. If working on specific project, read that project's .claude/context.md
4. If needed, check ACTIVE-PROJECTS.md for project overview
5. If needed, run refresh-context.sh for detailed summary

**Result**: ~5-10KB of highly relevant context instead of 40MB of everything

### During Session
- Update SESSION-CURRENT.md as work progresses
- Store important decisions in MCP memory
- Update features.json when feature status changes

### At Session End
1. Update SESSION-CURRENT.md with progress and next steps
2. Add session handoff to MCP memory
3. Update project .claude/context.md if architecture changed
4. Commit changes (session files are version controlled)

---

## The Bigger Picture

This context management system is part of a larger workspace methodology we're developing based on personal requirements and Anthropic's research on long-running agent workflows.

**The complete workflow** (which we'll share later) includes:
- Context optimization (this directory's content)
- Feature definition process (core of this package)
- Structured state management (features.json)
- Issue tracker integration (for team collaboration)
- Session compaction strategies (preserving history without bloat)
- Agent specialization patterns (bootstrap vs. feature-developer agents)

For now, we're sharing the **feature definition** piece because it's immediately useful and self-contained. But these context management patterns provide a glimpse of how it all fits together.

---

## What's Included Here

### Scripts
- **refresh-context.sh** - Generate context summaries from session files

### Example Session Files
- **session-current.md.example** - Template for tracking current work
- **active-projects.md.example** - Template for project index
- **session-recent.md.example** - Template for recent history
- **mcp-quick-ref.md.example** - Template for MCP usage

These are examples showing the structure. Adapt them to your workspace.

---

## Using These in Your Workspace

**1. Copy session file templates to your workspace root:**
```bash
cp extra/*.example ~/your-workspace/
# Rename .example to actual file names
```

**2. Copy refresh-context.sh:**
```bash
cp extra/refresh-context.sh ~/your-workspace/scripts/
chmod +x ~/your-workspace/scripts/refresh-context.sh
```

**3. Customize for your projects:**
- Update ACTIVE-PROJECTS.md with your project list
- Modify refresh-context.sh to look for your project directories
- Adjust session file sections to match your workflow

**4. Establish session rhythm:**
- Start: Read SESSION-CURRENT.md
- During: Update as you work
- End: Document progress and next steps

---

## Philosophy

**Optimize for resumption, not perfection.**

These files don't need to be perfectly comprehensive or beautifully formatted. They need to be:
- **Quick to update** (2 minutes at session end)
- **Fast to read** (AI can consume in seconds)
- **Actionable** (clear next steps)
- **Current** (reflects actual state)

Think of them as breadcrumbs for your future self (or the AI helping you).

---

## Future Enhancements

We're actively developing:
- Automated session file updates (AI maintains them)
- Integration with governance system (session files track quality gates)
- Enhanced MCP memory integration (semantic search across sessions)
- Session compaction strategies (preserve history without token bloat)
- GitHub sync automation (session files as project state)

When ready, we'll share the complete workspace methodology. For now, these extras give you a head start on context management.

---

## Questions?

This is an evolving methodology. We're sharing what works for us, but your mileage may vary.

**If you try these patterns:**
- Adapt them to your needs
- Keep what works, discard what doesn't
- Share your improvements with the community

The goal is better AI-assisted development, not rigid adherence to a process.

---

**Remember**: These are supporting tools for the feature definition workflow. The core methodology (conversational clarification → structured documentation → features.json) works with or without these context management patterns. But together, they're powerful.
