# Architecture Context Template

Use this template to create an `ARCHITECTURE.md` file in your project root. This document gives Claude the system-level understanding needed to make correct implementation decisions.

---

## Template

```markdown
# [Project Name] Architecture

> Last updated: [date]
> Status: [DRAFT | ACTIVE | NEEDS_REVIEW]

## System Overview

[2-3 sentences describing what this system does and why it exists]

## Core Components

### [Component 1 Name]
- **Purpose**: [What this component does]
- **Technology**: [Language, framework, database, etc.]
- **Location**: [Directory or service path]
- **Owns**: [What data/functionality this component is responsible for]

### [Component 2 Name]
- **Purpose**: 
- **Technology**: 
- **Location**: 
- **Owns**: 

[Add more components as needed]

## Data Flow

### Primary Flow: [Name this flow]
```
[Source] → [Processing Step] → [Destination]
```
[Brief explanation of when/why this flow occurs]

### Secondary Flow: [Name]
```
[Source] → [Processing Step] → [Destination]
```
[Brief explanation]

[Add more flows as needed]

## System Boundaries

### What This System Does
- [Responsibility 1]
- [Responsibility 2]

### What This System Does NOT Do
- [Non-responsibility 1 — important for preventing scope creep]
- [Non-responsibility 2]

### External Dependencies
| System | Purpose | Interface Type | Owner |
|--------|---------|----------------|-------|
| [External system] | [Why we use it] | [API/DB/File/etc.] | [Team/service] |

## Data Model Overview

### Core Entities
| Entity | Primary Store | Secondary Store | Notes |
|--------|--------------|-----------------|-------|
| [Entity name] | [Postgres/Neo4j/etc.] | [If applicable] | [Key relationships] |

### Schema Locations
- **[Entity 1]**: `[path/to/schema/file]`
- **[Entity 2]**: `[path/to/schema/file]`

## Cross-Component Rules

These rules MUST be followed when implementing features that cross component boundaries:

### Data Consistency Rules
1. [Rule about how data flows between components]
2. [Rule about what can/cannot write to specific stores]
3. [Rule about transaction boundaries]

### Naming Conventions
| Context | Convention | Example |
|---------|------------|---------|
| Database fields | [snake_case/camelCase/etc.] | `product_id` |
| API fields | [convention] | `productId` |
| Internal variables | [convention] | `product_id` |

### Type Conventions
| Type | Postgres | Python | API (JSON) |
|------|----------|--------|------------|
| Identifiers | UUID | uuid.UUID | string |
| Timestamps | TIMESTAMPTZ | datetime | ISO 8601 string |
| [Add common types] | | | |

## Dependency Map

When you touch these files, you must also verify these dependencies:

| If you modify... | Check/update... | Why |
|------------------|-----------------|-----|
| `[file/component]` | `[dependent file]` | [Relationship explanation] |
| `[schema file]` | `[all consumers]` | Schema change affects all readers |

## Current State

### Completed Components
- [x] [Component] — [brief status]

### In Progress
- [ ] [Component] — [brief status, link to feature]

### Planned
- [ ] [Component] — [brief description]

## Known Technical Debt

| Item | Impact | Location | Notes |
|------|--------|----------|-------|
| [Debt item] | [High/Med/Low] | [File/component] | [Context] |

## Decision Log Reference

Major architectural decisions are logged in `/decisions/`. Key decisions:

- `[decision-file.md]` — [One-line summary]
- `[decision-file.md]` — [One-line summary]

## For Claude

When implementing features in this project:

1. **Read this document first** for every new feature
2. **Check the Dependency Map** before modifying any file
3. **Follow Type Conventions** exactly — do not deviate
4. **Follow Naming Conventions** exactly — copy-paste, don't type from memory
5. **If unsure about a boundary**, ask before implementing
6. **Update this document** if you discover new dependencies or rules
```

---

## Usage Notes

### When to Create
Create ARCHITECTURE.md when:
- Starting a new project with multiple components
- Project has multiple data stores
- Project integrates with external systems
- Multiple features will share data models

### When to Update
Update ARCHITECTURE.md when:
- Adding a new component
- Changing data flow between components
- Adding new external dependencies
- Discovering new cross-component rules
- Completing major architectural decisions

### What NOT to Include
- Implementation details (that's what code is for)
- Feature-specific logic (that's what feature docs are for)
- Historical decisions (that's what decision logs are for)
- Step-by-step procedures (that's what commands are for)

Keep this document focused on **structure and rules**, not procedures.

---

## Example: E-commerce Data Warehouse

```markdown
# Beast Data Warehouse Architecture

> Last updated: 2025-12-22
> Status: ACTIVE

## System Overview

Consolidated data warehouse pulling from HubSpot (CRM) and Shopware (e-commerce) to enable unified reporting and analytics. Supports parent-child company relationships and complex B2B pricing tiers.

## Core Components

### Ingestion Service
- **Purpose**: Pull data from source systems on schedule
- **Technology**: Python, APScheduler
- **Location**: `/services/ingestion/`
- **Owns**: Raw data extraction, API authentication, rate limiting

### Transformation Service
- **Purpose**: Normalize and relate data from multiple sources
- **Technology**: Python, Pandas
- **Location**: `/services/transform/`
- **Owns**: Data cleaning, entity resolution, relationship mapping

### Warehouse
- **Purpose**: Store unified data model
- **Technology**: PostgreSQL
- **Location**: `/warehouse/`
- **Owns**: Canonical schema, historical tracking, query optimization

## Data Flow

### Primary Flow: Daily Sync
```
HubSpot API → Ingestion → Raw Tables → Transform → Warehouse Tables
Shopware API → Ingestion → Raw Tables → Transform → Warehouse Tables
```
Runs nightly at 2 AM. Full sync on Sundays, incremental Mon-Sat.

### Secondary Flow: Real-time Updates
```
Shopware Webhook → Ingestion → Transform → Warehouse (single record)
```
Order and customer updates within 5 minutes.

## System Boundaries

### What This System Does
- Pulls data from HubSpot and Shopware
- Resolves company/customer entities across systems
- Maintains historical record of changes
- Provides unified query interface

### What This System Does NOT Do
- Push data back to source systems (read-only)
- Handle real-time analytics (batch-oriented)
- Store PII beyond what's in source systems

## Cross-Component Rules

### Data Consistency Rules
1. HubSpot is source of truth for company hierarchy (parent-child)
2. Shopware is source of truth for order/transaction data
3. When entities conflict, flag for manual resolution — do not auto-merge

### Naming Conventions
| Context | Convention | Example |
|---------|------------|---------|
| Database fields | snake_case | `company_id` |
| Python variables | snake_case | `company_id` |
| API responses | camelCase | `companyId` |

### Type Conventions
| Type | Postgres | Python | Notes |
|------|----------|--------|-------|
| Identifiers | UUID | uuid.UUID | Always UUID, never int |
| External IDs | VARCHAR(255) | str | HubSpot/Shopware IDs are strings |
| Timestamps | TIMESTAMPTZ | datetime (UTC) | Always store UTC |
| Money | NUMERIC(12,2) | Decimal | Never float |

## Dependency Map

| If you modify... | Check/update... | Why |
|------------------|-----------------|-----|
| `warehouse/schema/company.py` | `transform/company_transformer.py` | Transformer writes to this schema |
| `warehouse/schema/company.py` | `services/ingestion/hubspot.py` | Field mapping must match |
| `transform/company_transformer.py` | `warehouse/schema/company.py` | Output must match warehouse schema |
| Any schema file | All read queries in `/reports/` | Queries depend on schema |
```

---

## Checklist for New Projects

- [ ] Created ARCHITECTURE.md in project root
- [ ] Documented all components
- [ ] Documented primary data flows
- [ ] Defined system boundaries (does/does not)
- [ ] Listed external dependencies
- [ ] Created dependency map
- [ ] Defined naming conventions
- [ ] Defined type conventions
- [ ] Added "For Claude" section with project-specific rules
