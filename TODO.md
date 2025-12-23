# TODO

Improvements to feature-definition-workflow methodology and tooling.

**Last Updated**: 2025-12-07

---

## Priority 1: Critical - Enforcement & Validation

### From F015 Process Failure (2025-12-07)

- [ ] **Update validate-features.py with new rules**
  - Add check: "completed" features with pending subtasks = ERROR
  - Add check: progress mismatch with subtask completion = ERROR
  - Add check: dependencies with incomplete subtasks = WARNING
  - Add reporting: show which specific subtasks are blocking
  - Add pre-start validation mode: `--check-dependencies FXX`
  - Exit code 1 if any completed features have pending subtasks

- [ ] **Create pre-commit hook template**
  - Already documented in 06-STATUS-MANAGEMENT.md
  - Add to scripts/ directory as installable hook
  - Test with mktg-laravel project

- [ ] **Update feature-definer skill**
  - Add mandatory dependency validation step before starting
  - Reference 05-DEPENDENCY-VALIDATION.md checklist
  - Add status update procedures from 06-STATUS-MANAGEMENT.md
  - Add testing requirements (unit + feature + manual UI)

- [ ] **Update project-breaker skill**
  - Ensure subtasks are properly defined with clear completion criteria
  - Add guidance on what makes a subtask "critical" vs "optional"
  - Reference that subtask completion affects parent status

---

## Priority 2: High Impact, Low Effort

### From suggestions.md (Opus 4.5 recommendations)

- [ ] **Add 2-minute triage step before template selection** (Improvement 1)
  - Add to 01-METHODOLOGY.md as "Step 0: Triage"
  - 9-point checklist (data model clarity, scope clarity, technical clarity)
  - Scoring system to determine Quick vs Standard template
  - Update 02-TEMPLATES.md to reference triage
  - Update feature-definer SKILL.md to include triage

- [ ] **Add approval checklist to templates** (Improvement 6)
  - Add checklist to feature-template.md
  - Add abbreviated checklist to feature-template-quick.md
  - Checklist covers: clarity, completeness, actionability
  - Update feature-definer SKILL.md Step 5 to reference checklist
  - Optionally add completeness scoring to validate-features.py

- [ ] **Create standalone prompts for non-Claude-Code users** (Improvement 5)
  - Create prompts/ directory
  - Add feature-definer-prompt.md (copy-paste ready)
  - Add project-breaker-prompt.md (copy-paste ready)
  - Add prompts/README.md explaining usage
  - Update main README.md with "Usage Without Claude Code" section

---

## Priority 3: Medium Impact, Medium Effort

### From suggestions.md

- [ ] **Address feature document staleness** (Improvement 2)
  - Add "Implementation Deltas" table to templates (Option A)
  - Add "Post-Implementation Reconciliation" section to Standard template (Option C)
  - Add fields to features.schema.json: `definitionComplete`, `reconciledDate`, `implementationDeltas`
  - Update validate-features.py to report on unreconciled features

- [ ] **Add definition debt tracking** (Improvement 4)
  - Add "Definition Debt" concept to 01-METHODOLOGY.md
  - Add fields to features.schema.json: `definitionDebt`, `definitionDebtReason`, `definitionDebtPriority`
  - Update validate-features.py to report definition debt metrics
  - Add "fast track" option to feature-definer that marks debt explicitly

---

## Priority 4: Structural Improvements

### From suggestions.md

- [ ] **Add explicit workflow states and transitions** (Improvement 3)
  - Add "Feature Lifecycle States" section to 01-METHODOLOGY.md
  - Lifecycle: IDENTIFIED → DEFINED → APPROVED → IN_PROGRESS → COMPLETED
  - Add "Progressive Definition" guidance to 03-PROJECT-BREAKDOWN.md (make prominent)
  - Update project-breaker SKILL.md to output features in "identified" state
  - Update feature-definer SKILL.md to transition features to "defined" state
  - Add `lifecycleState` enum to features.schema.json
  - Update validate-features.py to track lifecycle transitions

---

## Priority 5: Additional Enhancements

### From original TODO.md

- [ ] **Sync with vector database**
  - Investigate mem0.ai integration for feature definitions
  - Store key decisions, patterns, learnings
  - Enable semantic search across all feature documents
  - Cross-project intelligence (learn from past features)

- [ ] **Chat UI/UX for project progress**
  - Web interface to visualize features.json
  - Filter by status, priority, lifecycle state
  - Dependency graph visualization
  - Definition debt dashboard

---

## Validation & Testing

- [ ] **Test all changes against existing examples**
  - authentication example (example-01-authentication.md)
  - API endpoint example (example-02-api-endpoint.md)
  - Ensure backward compatibility

- [ ] **Update schema version**
  - Bump features.schema.json version when adding fields
  - Document migration path for existing features.json files

- [ ] **Create test features.json files**
  - Valid example with all new fields
  - Invalid examples for validation testing
  - Edge cases (circular deps, false completion, etc.)

---

## Documentation Updates

- [ ] **Update README.md**
  - Link to new 05-DEPENDENCY-VALIDATION.md and 06-STATUS-MANAGEMENT.md
  - Add "Lessons Learned" section referencing F015 failure
  - Add cost/benefit metrics ($100 lesson)
  - Update workflow diagram to include enforcement steps

- [ ] **Create CHANGELOG.md**
  - Document methodology evolution
  - Track breaking changes to schema
  - Reference process improvements and why they were added

- [ ] **Update CITATIONS.md**
  - Add reference to F015 process failure case study
  - Document enforcement procedures origin

---

## Integration Testing

- [ ] **Test complete workflow end-to-end**
  - Start with project-breaker on new spec
  - Use feature-definer for 3-5 features
  - Implement features following new validation procedures
  - Update statuses according to 06-STATUS-MANAGEMENT.md rules
  - Run validate-features.py at each step
  - Verify no false completions possible

- [ ] **Create validation test suite**
  - Unit tests for validate-features.py enhancements
  - Test cases for all new validation rules
  - Performance testing on large features.json files (100+ features)

---

## Future Considerations

- [ ] **GitHub Actions integration**
  - Auto-validate features.json on PR
  - Block PRs with validation errors
  - Post validation report as PR comment

- [ ] **VS Code extension**
  - Syntax highlighting for feature documents
  - Inline validation warnings
  - Quick actions (mark subtask complete, update progress)

- [ ] **CLI tool for common operations**
  - `fdef start FXX` - Run pre-start validation
  - `fdef complete FXX.N` - Mark subtask complete, update progress
  - `fdef status` - Show project overview
  - `fdef validate` - Run full validation

---

## Notes

- Maintain backward compatibility with existing features.json files
- New schema fields should have sensible defaults
- Keep "minimal viable process" philosophy - additions are optional enhancements
- Document WHY for each change (link to issue/failure that motivated it)

---

**References**:
- suggestions.md (Opus 4.5 recommendations from 2024-11-30)
- HONEST-ASSESSMENT.md (Reality check and limitations)
- F015 Process Failure (2025-12-07) - $100 lesson in dependency validation
- 05-DEPENDENCY-VALIDATION.md - Pre-start validation procedures
- 06-STATUS-MANAGEMENT.md - Status accuracy enforcement
