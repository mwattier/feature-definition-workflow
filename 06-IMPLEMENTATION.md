# Implementation Workflow

How to execute feature plans systematically, maintaining quality and context throughout the build process.

---

## Purpose

Planning is half the work. This document covers the other half: executing the plan without losing ground.

**Common failure modes during implementation:**
- Forgetting which branch you're on
- Skipping tests "just this once"
- Drifting from the spec without documenting why
- Marking things done without verifying acceptance criteria
- Losing context when switching between features

This workflow prevents those failures through structure, not discipline.

---

## Pre-Implementation Setup

Before writing any code, set up the environment for success.

### 1. Verify You Have a Clear Spec

Don't start implementation without:
- [ ] Approved feature document (or Quick template for simple features)
- [ ] Clear acceptance criteria
- [ ] Data model defined (if applicable)
- [ ] Out of scope explicitly stated
- [ ] Verification checklist created (see [05-VERIFICATION-WORKFLOW.md](./05-VERIFICATION-WORKFLOW.md))

**If any of these are missing**: Stop. Go back to feature definition. 20 minutes of clarification beats 2 hours of rework.

### 2. Create Feature Branch

```bash
# From main/master branch
git checkout main
git pull origin main

# Create feature branch
# Convention: feature/F001-short-description
git checkout -b feature/F001-user-authentication
```

**Branch naming**:
- Prefix with feature ID from features.json
- Keep description short but meaningful
- Use kebab-case

### 3. Codebase Research (If Applicable)

Before creating your worktree, understand what you're working with.

**When to do this:**
- ✅ Existing codebase with established patterns
- ✅ Feature similar to something already built
- ✅ Unfamiliar with this area of the code
- ❌ Greenfield project
- ❌ Truly novel feature with no precedent

**What to look for:**

Ask Claude (or yourself):
1. "Are there existing features similar to this? How are they structured?"
2. "What patterns does this codebase use for [auth/API/data access/etc.]?"
3. "What naming conventions, file structures, or architectural patterns should I follow?"

**Surface findings in the feature document:**

```markdown
## Codebase Research

**Similar features found:**
- PaymentController uses same service pattern we'll use here
- Existing JWT implementation in app/Services/TokenService.php

**Patterns to follow:**
- Services handle business logic, controllers are thin
- All API responses wrapped in ApiResponse::success() / ::error()

**Relevant files to reference:**
- app/Http/Controllers/PaymentController.php
- app/Services/TokenService.php
```

**Why research before worktree:** You want to know what patterns to follow before you start writing code, not discover mid-implementation that you've done it differently than the rest of the codebase.

### 4. Create Isolated Worktree (Recommended)

Worktrees let you work on features in isolation without stashing or switching branches.

```bash
# Create worktree directory (first time only)
mkdir -p ../worktrees

# Create worktree for this feature
git worktree add ../worktrees/F001 feature/F001-user-authentication

# Navigate to worktree
cd ../worktrees/F001
```

**Why worktrees:**
- Main workspace stays clean
- Can work on multiple features simultaneously
- No "forgot which branch I'm on" errors
- Easy to abandon failed experiments (just delete the directory)

**When to skip worktrees:**
- Very small changes (< 1 hour)
- Hotfixes that need immediate deployment
- When worktree overhead exceeds benefit

**When to clean up worktrees:**
- ✅ After PR merged and deployed
- ✅ After feature abandoned/cancelled
- ❌ Not while PR is under review (might need quick fixes)
- ❌ Not if feature might need hotfix shortly after merge

### 5. Update features.json

Mark the feature as started:

```json
{
  "id": "F001",
  "name": "User Authentication",
  "status": "in_progress",
  "progress": 0,
  "startedDate": "2024-12-01"
}
```

---

## During Implementation

### Execute Subtasks Systematically

Don't implement the whole feature at once. Work through subtasks from your feature document or features.json.

**For each subtask:**

1. **Read the subtask** — What specifically needs to be done?
2. **Verify dependencies** — Run `/verify-file` before writing (see [05-VERIFICATION-WORKFLOW.md](./05-VERIFICATION-WORKFLOW.md))
3. **Implement** — Write the code
4. **Verify output** — Run `/verify-file` after writing to confirm types and fields match sources
5. **Test** — Run relevant tests (don't skip this)
6. **Commit** — Small, logical commits with clear messages
7. **Update status** — Mark subtask complete in features.json

**Why verify before AND after:**
- Before: Ensures you're working from correct source-of-truth (field names, types, dependencies)
- After: Ensures what you wrote actually matches what you intended

```bash
# Commit message format
# Optional: Use Conventional Commits (feat, fix, docs, refactor, test, chore)
git commit -m "feat(F001.1): create users table migration

- Add email, password_hash, created_at fields
- Add unique index on email
- Add timestamps"

# Or simpler format if not using Conventional Commits:
git commit -m "F001.1: Create users table migration

- Add email, password_hash, created_at fields
- Add unique index on email
- Add timestamps"
```

### Run Tests After Every Change

This is non-negotiable. Every meaningful change should be followed by:

```bash
# Run relevant test suite
php artisan test --filter=AuthenticationTest  # Laravel
npm test -- --grep="authentication"           # Node
pytest tests/test_auth.py                     # Python
```

**Why every change:**
- Catch regressions immediately (not 3 hours later)
- Small failures are easier to debug than large ones
- Tests passing after each commit means any commit is deployable

### Check Against Spec Regularly

Every 30-60 minutes, or after completing a subtask:

1. Re-read the relevant section of your feature document
2. Verify implementation matches intent
3. Note any deviations in the Implementation Deltas section

**If you find yourself building something different than spec:**

Stop and ask:
- Is the spec wrong? (Update spec, document why)
- Am I wrong? (Adjust implementation)
- Is this scope creep? (Defer to separate feature)

Don't drift silently. Document the divergence.

### Track Progress in features.json

Update progress as subtasks complete:

```json
{
  "id": "F001",
  "status": "in_progress",
  "progress": 40,
  "subtasks": [
    {"id": "F001.1", "name": "Database schema", "status": "completed"},
    {"id": "F001.2", "name": "Password hashing", "status": "completed"},
    {"id": "F001.3", "name": "Login endpoint", "status": "in_progress"},
    {"id": "F001.4", "name": "Registration endpoint", "status": "pending"},
    {"id": "F001.5", "name": "Tests", "status": "pending"}
  ]
}
```

**Progress calculation**: `(completed subtasks / total subtasks) × 100`

**Tip:** Use a script to auto-calculate progress:
```bash
# Example: scripts/update-progress.sh
jq '.features[] | select(.id=="F001") | 
  .progress = ((.subtasks | map(select(.status=="completed")) | length) / 
  (.subtasks | length) * 100 | floor)' features.json
```

### Estimating Time Remaining

At 25%, 50%, 75% completion, ask yourself:
- Am I on track with the original estimate?
- Have I discovered unexpected complexity?
- Should I update features.json `actualEffort`?

**Red flags:**
- Subtask taking >2x estimate
- Multiple "just one more thing" additions
- Drifting from spec without documentation

**Action:** Stop, reassess, update estimate in features.json if needed. Estimates aren't commitments — they're tools for planning.

### Continuous Integration

If your project has CI/CD:

**After each push:**
- [ ] Check CI pipeline status
- [ ] Review failed checks (linting, tests, security scans)
- [ ] Fix issues before moving to next subtask

**Don't:**
- Push multiple times to "fix CI" without testing locally first
- Ignore failing checks with intent to "fix later"
- Wait until PR creation to discover CI issues

**Tip:** Run the same checks locally that CI runs. If CI runs `npm test && npm run lint`, run that before pushing.

### Merge Conflicts

If your feature branch falls behind main:

1. **Stay calm** — Conflicts are normal, especially on active codebases
2. **Update main**: 
   ```bash
   git checkout main && git pull
   ```
3. **Rebase or merge:**
   ```bash
   # Option A: Rebase (cleaner history)
   git checkout feature/F001-auth
   git rebase main
   
   # Option B: Merge (preserves history)
   git checkout feature/F001-auth
   git merge main
   ```
4. **Resolve conflicts** — Use your IDE's merge tool
5. **Test after resolving** — Conflicts can introduce bugs
6. **Continue:** `git rebase --continue` or commit the merge

**When to rebase vs merge:**
- **Rebase:** Clean history, solo work, before PR review
- **Merge:** Preserves context, during PR review, shared branches

---

## Pre-Completion Checklist

Before marking a feature complete, verify everything. This checklist catches what gets skipped when you're in flow.

### Verification (see [05-VERIFICATION-WORKFLOW.md](./05-VERIFICATION-WORKFLOW.md))

- [ ] All files have `verification_status: VERIFIED` in features.json
- [ ] Cross-file verification complete (types match across boundaries)
- [ ] No open issues in verification checklist
- [ ] `/verify-feature` passes

### Functionality

- [ ] All acceptance criteria from feature document met
- [ ] Happy path works end-to-end
- [ ] Edge cases from spec handled
- [ ] Error states implemented and tested
- [ ] User feedback (messages, notifications) in place

### Code Quality

- [ ] All tests pass (new and existing)
- [ ] No regressions in existing functionality
- [ ] Code follows existing patterns in codebase
- [ ] No obvious performance issues (N+1 queries, missing indexes)
- [ ] No hardcoded values that should be config

### Security (if applicable)

- [ ] Input validation on all user inputs
- [ ] Authentication checked where required
- [ ] Authorization verified (can user X do action Y?)
- [ ] No sensitive data in logs or error messages
- [ ] SQL injection / XSS / CSRF protections in place

### Data (if applicable)

- [ ] Migrations run cleanly (up and down)
- [ ] Existing data handles migration correctly
- [ ] Constraints and indexes appropriate
- [ ] Cascade/nullify behavior on delete is correct

### Documentation

- [ ] features.json status updated to "completed"
- [ ] features.json progress set to 100
- [ ] completedDate set
- [ ] Implementation deltas noted (if spec changed during build)
- [ ] Any new patterns or conventions documented

### Cleanup

- [ ] No debug code left in (console.log, dd(), print statements)
- [ ] No commented-out code blocks
- [ ] No TODO comments that should be addressed now
- [ ] Worktree cleaned up (if used)

---

## Post-Implementation

### Update features.json

```json
{
  "id": "F001",
  "name": "User Authentication",
  "status": "completed",
  "progress": 100,
  "startedDate": "2024-12-01",
  "completedDate": "2024-12-03",
  "actualEffort": "medium",
  "files": [
    "app/Models/User.php",
    "app/Http/Controllers/AuthController.php",
    "database/migrations/2024_12_01_create_users_table.php",
    "tests/Feature/AuthenticationTest.php"
  ],
  "implementationDeltas": [
    {
      "date": "2024-12-02",
      "section": "API Design",
      "description": "Changed error code from 400 to 422 for validation errors",
      "rationale": "Consistency with Laravel conventions"
    }
  ]
}
```

### Document Implementation Deltas

If anything changed from the original spec:

**In feature document:**

```markdown
## Implementation Deltas

| Date | Section | Original | Changed To | Rationale |
|------|---------|----------|------------|-----------|
| 2024-12-02 | API Design | 400 for validation | 422 for validation | Laravel convention |
| 2024-12-03 | Data Model | No retry tracking | Added retry_count | Needed for rate limiting |
```

**Why this matters:**
- Future you understands why code differs from spec
- Patterns emerge (if you keep making the same change, update your templates)
- Handoffs don't require explaining "well, the spec says X but we actually did Y"

### Create Pull Request

```bash
# From your feature branch or worktree
git push origin feature/F001-user-authentication

# Create PR via GitHub CLI or web interface
gh pr create --title "F001: User Authentication" --body "Implements user authentication per feature spec.

## Changes
- User model with password hashing
- Login/logout endpoints
- Session management with JWT
- Rate limiting on auth endpoints

## Testing
- All new tests passing
- No regressions in existing tests

## Spec
See: docs/features/01-user-authentication.md

## Checklist
- [x] Acceptance criteria met
- [x] Tests pass
- [x] Security review done
- [x] features.json updated"
```

### Clean Up Worktree

After PR is merged:

```bash
# Return to main workspace
cd /path/to/main/workspace

# Remove worktree
git worktree remove ../worktrees/F001

# Delete feature branch (optional, after merge)
git branch -d feature/F001-user-authentication
```

---

## When Things Go Wrong

### Stuck on a Subtask

If a subtask is taking more than 2x the estimated time:

1. **Stop and reassess** — Is this subtask actually multiple subtasks?
2. **Check the spec** — Did you miss something? Is the spec unclear?
3. **Document the blocker** — Add to features.json blockers
4. **Ask for help or skip** — Move to next subtask if possible, come back later

```json
{
  "id": "F001",
  "status": "blocked",
  "blockers": [
    {
      "id": "B001",
      "description": "JWT library doesn't support refresh tokens as expected",
      "severity": "medium",
      "status": "investigating",
      "createdDate": "2024-12-02"
    }
  ]
}
```

### Discovered the Spec Was Wrong

This happens. The question is how you handle it.

**If the change is small:**
1. Update the spec with the correction
2. Note in Implementation Deltas
3. Continue implementation

**If the change is significant:**
1. Stop implementation
2. Go back to feature definition conversation
3. Update spec with new understanding
4. Re-estimate if needed
5. Resume implementation

**Never**: Silently build something different than the spec. That way lies confusion.

### Tests Are Failing and You Don't Know Why

1. **Stash your changes**: `git stash`
2. **Run tests on clean branch**: Do they pass?
3. **If yes**: Your changes broke something. Apply stash, bisect to find the issue
4. **If no**: Something else broke. Don't proceed until baseline is green

**Don't**: Push forward with failing tests hoping to "fix them later"

### Context Window Exhaustion (Long Session)

If Claude is losing context mid-implementation:

1. **Commit current work**: Save your progress
2. **Update features.json**: Document where you are
3. **Write a handoff note**: In SESSION-CURRENT.md or similar

```markdown
## Session Handoff - F001

**Completed:**
- F001.1: Database schema ✓
- F001.2: Password hashing ✓

**In progress:**
- F001.3: Login endpoint (50% done, token generation working, need error handling)

**Next steps:**
1. Add rate limiting to login endpoint
2. Implement validation error responses
3. Write tests for login flow

**Key decisions made this session:**
- Using Laravel's built-in rate limiter, not custom
- JWT expires after 7 days, refresh not implemented (out of scope)
```

4. **Start fresh session**: New context with handoff note

---

## Integration with Feature Definition Workflow

This document is **06-IMPLEMENTATION.md** in the feature-definition-workflow methodology.

**The full workflow:**

1. **[01-METHODOLOGY.md]** — Conversational feature definition
2. **[02-TEMPLATES.md]** — Feature document templates
3. **[03-PROJECT-BREAKDOWN.md]** — Large project decomposition
4. **[04-ISSUE-INTEGRATION.md]** — Tracking system integration
5. **[05-VERIFICATION-WORKFLOW.md]** — Cross-reference verification before/during implementation
6. **[06-IMPLEMENTATION.md]** — This document: executing the plan

**Where this fits:**

```
Feature Definition (01-03)
    ↓
Tracking Setup (04)
    ↓
Verification Setup (05) ← Map files, dependencies, create verification checklist
    ↓
Implementation (06) ← You are here
    ↓
    ├── Per-file: /verify-file before writing
    ├── Write code
    ├── /verify-file after writing
    ├── Run tests
    ├── Update features.json
    ↓
Post-Implementation (reconciliation, handoff)
```

**05 vs 06:**
- **05-VERIFICATION-WORKFLOW** catches correctness issues (types, field names, dependencies between files)
- **06-IMPLEMENTATION** catches process issues (skipped tests, forgotten status updates, spec drift)

---

## Summary

**Before starting:**
- Verify you have a clear spec
- Create feature branch
- Set up worktree (recommended)
- Update features.json status

**During implementation:**
- Execute subtasks systematically
- Run tests after every change
- Check against spec regularly
- Track progress in features.json

**Before marking complete:**
- Run through pre-completion checklist
- Verify all acceptance criteria
- Document any implementation deltas

**After completion:**
- Update features.json
- Create PR with checklist
- Clean up worktree

---

**Remember**: The goal isn't speed. The goal is not losing ground. Structure prevents the small skips that compound into large problems.
