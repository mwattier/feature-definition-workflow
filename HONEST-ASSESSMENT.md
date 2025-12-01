# Honest Assessment

Before you adopt this methodology, you should know what you're getting into. This is based on how I have approached projects for a long time. I'm kinda old, set in my ways, and know what works for me. I spend a lot of time teaching Claude, and other models, how I like to do things. I borrow on ideas from Anthropic in this particular case on how to translate my method to help Claude understand me. 

I've done this stuff for a long time but haven't shared much publicly. I'm trying to be better about sharing in the hopes that someone might find some benefit. 

---

## What This Is

A structured approach I use for clarifying software features before implementation, optimized for MY AI-assisted development workflows. 

## What This Isn't

- A replacement for good judgment
- A guarantee against rework
- The only way to build software
- Appropriate for every project or team

---

## Who This Is For

**Primary audience**: Solo developers or small teams using AI assistants (Claude, ChatGPT, Copilot) for implementation.

**The specific problem it solves**: When you're working with AI assistants across multiple sessions, context drifts, assumptions go unstated, and you end up with "that's not what I meant" moments that cost hours of rework.

**If you have**:
- A PM who writes detailed specs
- Established sprint processes with refinement sessions
- A team that provides natural back-and-forth on requirements

...you may already have this. The methodology formalizes what good teams do naturally. It's most valuable when you *don't* have those things — when you're the PM, the developer, and the QA, and the AI is your only sounding board.

---

## The Overhead Is Real

I'll be honest about what's in this repo:

- 4 methodology documents
- 2 feature templates
- 2 Claude skills
- JSON schema and validation script
- Context management scripts and session file templates
- Multiple examples (only examples, I stripped out all of the real working projects I use this on)

That's a lot of infrastructure around "talk before you code." My personal style is to over document everything and this works for me. YMMV. 

**The tradeoff**: Structure enables consistency but adds friction. If you adopt all of this, you're committing to a process. That process has value to me, but it's not free. This method reduced my cognitive load during project hopping, but it does take a commitment. 

**My recommendation**: Start with just the conversation habit and one template. Add the tracking infrastructure (features.json, validation, etc.) only when you feel the need for it. Don't adopt the whole system on day one.

---

## Time Investment: Real Numbers

The "15 minutes prevents hours of rework" tagline is aspirational. Here's what it actually looks like:

| Feature Complexity | Conversation | Documentation | Total |
|-------------------|--------------|---------------|-------|
| Simple (clear scope, no data model) | 5-10 min | 5-10 min | 10-20 min |
| Medium (some unknowns, data model) | 15-25 min | 10-15 min | 25-40 min |
| Complex (many unknowns, integrations) | 30-60 min | 20-30 min | 50-90 min |

The ROI is still there — a 40-minute conversation that prevents 4 hours of rework is a 6x return. But "15 minutes" undersells the real investment for non-trivial features.

---

## The Examples Are Idealized

The authentication and data export examples in this repo show:
- Users who have answers ready (I normally do)
- Clean back-and-forth with no confusion (The AI typically needs a few rounds of clarification to fully understand what I am building)
- Tidy resolution to all questions

Real conversations are messier:
- "I don't know yet" is a valid answer (and common)
- Users/Clients/Bosses contradict earlier statements
- Scope changes mid-conversation/mid-project
- Some questions don't have good answers until you start building
- Feature 12 winds up changing feature 6 in some way

The examples demonstrate the *structure*, not the *reality*. Your conversations will be less clean. That's fine.

---

## When This Doesn't Work

**Exploratory work**: Sometimes you don't know what you're building until you build it. Over-specifying something that will change anyway is waste. For true R&D or experimental features, write code first, document after.

**Trivial changes**: A CSS color change doesn't need a feature document. Neither does fixing a typo or updating a dependency. Use judgment.

**Time pressure**: If the building is on fire, put out the fire. Document later. A shipped feature with no spec is better than a perfect spec with no feature.

**Analysis paralysis**: If you find yourself perfecting documentation instead of shipping, you've inverted the purpose. The goal is *clarity that enables action*, not *documentation as deliverable*.

---

## When I Skip It

I created this methodology and I don't use it for everything. I skip it when:

- The feature is obvious and I can hold it in my head
- I'm spiking/prototyping and expect to throw away the code
- Time pressure makes the overhead unjustifiable
- The "feature" is really just a bug fix or config change

I use it when:

- I catch myself making assumptions I can't verify
- The AI does not have the proper big picture
- The data model is non-obvious
- There are multiple valid approaches and I need to choose
- I'll be working on this across multiple sessions
- I want to be able to explain/defend/remember my decisions later

---

## The Anthropic Connection

This methodology builds on Anthropic's published research about long-running agent workflows. I cite them because:

1. Their research informed the approach (especially context window constraints and JSON-based state tracking)
2. It's intellectually honest to acknowledge sources
3. They are smarter than me. 

What I added:
- The conversational clarification layer (Anthropic's research focuses on implementation, not definition)
- Templates for documentation
- Integration between definition and tracking
- Tooling (validation, context management)

If you read their blog posts and think "this is just that with templates" — you're partially right. The templates and conversation structure are the value-add. Whether that's enough value depends on your needs.

---

## Why I Built This

I wear many hats. Sometimes solutions architect, sometimes a dev, sometimes I am just hacking somethign out, almost always solo. I am always working on multiple projects (some multi-month, complex systems). My specific pain points:

- Context drift between AI sessions
- No team to provide natural feedback on requirements
- Building the wrong thing because assumptions went unstated
- Losing track of what I decided 3 weeks ago and why

This methodology solved those problems for me. It reduced my token costs (fewer context compactions), increased my confidence in project status, and eliminated most "that's not what I meant" moments.

Your situation may be different, YMMV. Adapt accordingly.

---

## What I'd Change If Starting Over

1. **Start simpler** — I'd begin with just the conversation habit and Quick template, add structure only as needed

2. **Be more aggressive about "skip it"** — More features than I expected don't need this process

3. **Track time spent on definition** — To actually measure ROI rather than estimate it

4. **Build in "definition debt" from the start** — Acknowledge that sometimes you ship with incomplete specs and that's okay (coming soon)

---

## Feedback Welcome

This is a living methodology. I've been developing software for 25+ years but, as mentioned, I've rarely shared process publicly. There are probably blind spots.

If you try this and it doesn't work, I want to know why. If you adapt it and find improvements, I want to know those too.

Open an issue or PR. The goal is useful tools. 

---

## TL;DR

- This solves a real problem but isn't universally applicable
- The overhead is real — adopt incrementally
- Time investment is 20-90 minutes per feature, not 15 (but 15 is my target for some stuff)
- Skip it when judgment says to skip it
- The examples are cleaner than reality will be for you
- Adapt to your needs, don't follow rigidly

If you're a solo dev or small team using AI assistants and you've felt the pain of context drift and unclear requirements, this might help. If not, no hard feelings.

---

**Last Updated**: 2024-11-30
