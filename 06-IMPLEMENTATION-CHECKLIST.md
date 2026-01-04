# Implementation Workflow Checklist

**Quick reference companion to [06-IMPLEMENTATION.md](./06-IMPLEMENTATION.md)**

Print this, keep it visible, check boxes as you go. This prevents the small skips that compound into large problems.

---

## 🚀 Pre-Implementation Setup

Before writing any code:

- [ ] **Clear Spec Verified**
  - [ ] Approved feature document exists
  - [ ] Clear acceptance criteria defined
  - [ ] Data model defined (if applicable)
  - [ ] Out of scope explicitly stated
  - [ ] Verification checklist created

- [ ] **Feature Branch Created**
  ```bash
  git checkout main && git pull origin main
  git checkout -b feature/F001-short-description
  ```

- [ ] **Codebase Research Done** (if applicable)
  - [ ] Similar features identified
  - [ ] Patterns documented
  - [ ] Relevant files noted in feature doc

- [ ] **Worktree Created** (recommended)
  ```bash
  git worktree add ../worktrees/F001 feature/F001-description
  cd ../worktrees/F001
  ```

- [ ] **features.json Updated**
  - [ ] Status: `in_progress`
  - [ ] Progress: `0`
  - [ ] startedDate set

---

## 🔄 For Each Subtask

Repeat these 7 steps for every subtask:

1. [ ] **Read** the subtask — What specifically needs to be done?
2. [ ] **Verify dependencies** — Run `/verify-file` before writing
3. [ ] **Implement** — Write the code
4. [ ] **Verify output** — Run `/verify-file` after writing
5. [ ] **Test** — Run relevant tests (non-negotiable)
6. [ ] **Commit** — Small, logical commit with clear message
7. [ ] **Update status** — Mark subtask complete in features.json

---

## ⏱️ Regular Checks (Every 30-60 Minutes)

- [ ] **Spec Alignment Check**
  - [ ] Re-read relevant section of feature document
  - [ ] Verify implementation matches intent
  - [ ] Document any deviations in Implementation Deltas

- [ ] **Progress Update**
  - [ ] Update features.json progress percentage
  - [ ] Check if on track with estimate

- [ ] **Context Preservation**
  - [ ] Key decisions noted
  - [ ] Blockers documented if encountered

---

## ✅ Pre-Completion Checklist

Before marking feature complete, verify everything:

### Verification
- [ ] All files have `verification_status: VERIFIED` in features.json
- [ ] Cross-file verification complete (types match)
- [ ] No open issues in verification checklist
- [ ] `/verify-feature` passes

### Functionality
- [ ] All acceptance criteria met
- [ ] Happy path works end-to-end
- [ ] Edge cases handled
- [ ] Error states implemented and tested
- [ ] User feedback (messages, notifications) in place

### Code Quality
- [ ] All tests pass (new and existing)
- [ ] No regressions in existing functionality
- [ ] Code follows existing patterns
- [ ] No obvious performance issues
- [ ] No hardcoded values that should be config

### Security (if applicable)
- [ ] Input validation on all user inputs
- [ ] Authentication checked where required
- [ ] Authorization verified
- [ ] No sensitive data in logs/errors
- [ ] SQL injection / XSS / CSRF protections in place

### Data (if applicable)
- [ ] Migrations run cleanly (up and down)
- [ ] Existing data handles migration correctly
- [ ] Constraints and indexes appropriate
- [ ] Cascade/nullify behavior on delete is correct

### Documentation
- [ ] features.json status updated to `completed`
- [ ] features.json progress set to `100`
- [ ] completedDate set
- [ ] Implementation deltas noted (if spec changed)
- [ ] New patterns/conventions documented

### Cleanup
- [ ] No debug code left in (console.log, dd(), print)
- [ ] No commented-out code blocks
- [ ] No TODO comments that should be addressed now
- [ ] Worktree cleaned up (if used)

---

## 📝 Post-Implementation

- [ ] **features.json Updated**
  - [ ] Status: `completed`
  - [ ] Progress: `100`
  - [ ] completedDate set
  - [ ] actualEffort recorded
  - [ ] files array populated
  - [ ] implementationDeltas documented

- [ ] **Pull Request Created**
  ```bash
  git push origin feature/F001-description
  gh pr create --title "F001: Feature Name" --body "[checklist]"
  ```

- [ ] **Worktree Cleaned Up** (after PR merged)
  ```bash
  cd /path/to/main/workspace
  git worktree remove ../worktrees/F001
  git branch -d feature/F001-description
  ```

---

## 🆘 Troubleshooting Quick Reference

### ❌ Stuck on a Subtask (>2x estimate)
1. Stop and reassess — Is this multiple subtasks?
2. Check the spec — Missed something? Unclear?
3. Document the blocker in features.json
4. Ask for help or skip, come back later

### ❌ Spec Was Wrong
- **Small change**: Update spec, note in deltas, continue
- **Significant change**: Stop, go back to feature definition, re-estimate

### ❌ Tests Failing
```bash
git stash                    # Stash changes
# Run tests on clean branch  # Do they pass now?
git stash pop               # If yes, your changes broke it
```

### ❌ Context Window Exhaustion
1. Commit current work
2. Update features.json
3. Write handoff note in SESSION-CURRENT.md
4. Start fresh session with handoff note

### ❌ Merge Conflicts
```bash
git checkout main && git pull
git checkout feature/F001-description
git rebase main              # Or: git merge main
# Resolve conflicts in IDE
# Test after resolving
git rebase --continue        # Or: commit the merge
```

---

## 🎯 CI/CD Reminder

If your project has CI/CD, after each push:

- [ ] Check CI pipeline status
- [ ] Review failed checks (linting, tests, security)
- [ ] Fix issues before moving to next subtask

**Tip**: Run the same checks locally that CI runs

---

## 💡 Key Principles

1. **Test after every change** — Non-negotiable
2. **Verify before AND after** — Run `/verify-file` both times
3. **Small commits** — Each commit tells a story
4. **Check spec regularly** — Don't drift silently
5. **Document deltas** — Future you will thank you
6. **Clean up worktrees** — Only after PR merged and deployed

---

## 🔗 Full Details

For complete context, examples, and explanations, see **[06-IMPLEMENTATION.md](./06-IMPLEMENTATION.md)**

For verification process details, see **[05-VERIFICATION-WORKFLOW.md](./05-VERIFICATION-WORKFLOW.md)**

---

**Remember**: The goal isn't speed. The goal is not losing ground.
