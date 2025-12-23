# Decision Log Template

Use this template to record architectural and implementation decisions. Decision logs capture **why** choices were made, which is often more valuable than the choice itself.

---

## Template

```markdown
# Decision: [Short Title]

> **Date**: [YYYY-MM-DD]
> **Status**: [PROPOSED | ACCEPTED | DEPRECATED | SUPERSEDED]
> **Feature**: [feature-id or "system-wide"]
> **Supersedes**: [previous-decision.md if applicable]
> **Superseded by**: [newer-decision.md if applicable]

## Context

[What is the situation that requires a decision? What problem are we solving?]

## Decision

[What did we decide to do?]

## Alternatives Considered

### [Alternative 1]
- **Description**: [What this alternative would look like]
- **Pros**: [Benefits]
- **Cons**: [Drawbacks]
- **Why not chosen**: [Specific reason]

### [Alternative 2]
- **Description**: 
- **Pros**: 
- **Cons**: 
- **Why not chosen**: 

[Add more alternatives as needed]

## Consequences

### Positive
- [Good outcome 1]
- [Good outcome 2]

### Negative
- [Tradeoff 1]
- [Tradeoff 2]

### Risks
- [Risk 1 and mitigation]
- [Risk 2 and mitigation]

## Implementation Notes

[Any specific implementation guidance that follows from this decision]

## Participants

- [Name/Role] — [Their position/input]
- Claude — [AI's analysis/recommendation]

## References

- [Link to relevant docs/issues/discussions]
```

---

## Usage Guidelines

### When to Create a Decision Log

Create a decision log when:
- Choosing between multiple valid technical approaches
- Making a decision that will be hard to reverse
- Making a decision that affects multiple features/components
- Someone might ask "why did we do it this way?" in 6 months
- Deviating from a common pattern or best practice

### When NOT to Create a Decision Log

Don't create a decision log for:
- Trivial implementation choices
- Decisions that follow established patterns
- Temporary workarounds (use TODO comments instead)
- Decisions already documented elsewhere

### Naming Convention

```
decisions/
├── 2025-12-22-uuid-for-identifiers.md
├── 2025-12-22-postgres-over-mysql.md
├── 2025-12-23-shopware-hubspot-sync-direction.md
└── 2025-12-24-feature-xyz-caching-strategy.md
```

Format: `YYYY-MM-DD-short-description.md`

### Linking to features.json

Reference decision logs in your feature entries:

```json
{
  "id": "product-normalization",
  "decisions": [
    "decisions/2025-12-22-uuid-for-identifiers.md",
    "decisions/2025-12-22-neo4j-for-relationships.md"
  ]
}
```

---

## Example Decision Logs

### Example 1: Data Type Decision

```markdown
# Decision: UUIDs for All Identifiers

> **Date**: 2025-12-22
> **Status**: ACCEPTED
> **Feature**: system-wide

## Context

We need to establish a standard for entity identifiers across the system. The data warehouse pulls from HubSpot (string IDs) and Shopware (integer IDs) and needs a unified identifier scheme.

## Decision

Use UUIDs (v4) for all internal identifiers. Store external system IDs separately as strings.

## Alternatives Considered

### Auto-increment Integers
- **Description**: Standard SERIAL/BIGSERIAL primary keys
- **Pros**: Simple, compact, fast indexes
- **Cons**: Collisions when merging data from multiple sources, predictable (security concern)
- **Why not chosen**: Cannot guarantee uniqueness across distributed sources

### Composite Keys (source + external_id)
- **Description**: Use (source_system, external_id) as primary key
- **Pros**: Direct traceability to source
- **Cons**: Complex joins, awkward foreign keys, breaks if external ID changes
- **Why not chosen**: Too complex for downstream queries

### ULIDs
- **Description**: Lexicographically sortable unique identifiers
- **Pros**: Sortable by time, unique
- **Cons**: Less tooling support, unfamiliar to team
- **Why not chosen**: UUID is more widely supported

## Consequences

### Positive
- Guaranteed uniqueness across all sources
- Can generate IDs before insert (useful for batching)
- No coordination needed between services

### Negative
- Larger storage (16 bytes vs 4-8 for integers)
- Slightly slower index operations
- Less human-readable

### Risks
- Performance impact on very large tables — mitigated by proper indexing
- Developer confusion about when to use UUID vs external ID — mitigated by documentation

## Implementation Notes

- All new tables use `id UUID PRIMARY KEY DEFAULT gen_random_uuid()`
- External IDs stored in `external_id VARCHAR(255)` with source indicator
- Never expose UUIDs in URLs if predictability is a concern (use external ID instead)

## Participants

- Mike — Proposed UUIDs based on past experience with distributed data
- Claude — Analyzed alternatives, confirmed UUID approach
```

### Example 2: Architecture Decision

```markdown
# Decision: HubSpot as Company Hierarchy Source of Truth

> **Date**: 2025-12-22
> **Status**: ACCEPTED
> **Feature**: company-sync

## Context

Companies exist in both HubSpot and Shopware. HubSpot has parent-child relationships. Shopware has customer groups. When company data conflicts, we need to know which source wins.

## Decision

HubSpot is the source of truth for:
- Company hierarchy (parent-child relationships)
- Company metadata (industry, size, etc.)
- Contact-to-company associations

Shopware is the source of truth for:
- Transaction history
- Pricing tier assignments
- Order-related data

## Alternatives Considered

### Shopware as Single Source of Truth
- **Description**: Treat Shopware as canonical, HubSpot as supplementary
- **Pros**: Simpler data flow, e-commerce focused
- **Cons**: Lose rich CRM relationships, HubSpot has better company data
- **Why not chosen**: Sales team relies on HubSpot hierarchy for account management

### Merge on Conflict
- **Description**: Attempt to intelligently merge conflicting data
- **Pros**: Preserves information from both sources
- **Cons**: Complex rules, hard to debug, silent data corruption risk
- **Why not chosen**: Too risky for business-critical data

## Consequences

### Positive
- Clear ownership eliminates ambiguity
- Sales team's workflows remain intact
- Transaction integrity preserved

### Negative  
- Must maintain mapping between HubSpot companies and Shopware customers
- Company updates must flow from HubSpot (can't edit in Shopware and expect sync)

### Risks
- Orphaned records if HubSpot company deleted — mitigate with soft deletes
- Sync lag between systems — mitigate with conflict flagging

## Participants

- Mike — Business requirement from sales team
- Claude — Technical analysis of sync implications
```

---

## For Claude

When making decisions during implementation:

1. **Recognize decision points** — When there are multiple valid approaches, stop and document
2. **Don't decide silently** — If you choose approach A over approach B, say why
3. **Create the log** — Use this template to capture the decision
4. **Link it** — Add the decision to the feature's entry in features.json
5. **Reference in code** — Add comments pointing to decision logs for non-obvious choices

```python
# Using UUID here instead of external_id for joins
# See: decisions/2025-12-22-uuid-for-identifiers.md
```
