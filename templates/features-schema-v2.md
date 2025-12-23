# features.json Schema (v2)

This schema extends the original features.json format to include verification tracking, file dependencies, checkpoints, and decision references.

---

## Full Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Features",
  "type": "object",
  "required": ["version", "project", "features"],
  "properties": {
    "version": {
      "type": "string",
      "description": "Schema version",
      "const": "2.0"
    },
    "project": {
      "type": "object",
      "required": ["name"],
      "properties": {
        "name": { "type": "string" },
        "description": { "type": "string" },
        "repository": { "type": "string" },
        "architecture_doc": { 
          "type": "string",
          "description": "Path to ARCHITECTURE.md",
          "default": "ARCHITECTURE.md"
        }
      }
    },
    "features": {
      "type": "array",
      "items": { "$ref": "#/definitions/feature" }
    }
  },
  "definitions": {
    "feature": {
      "type": "object",
      "required": ["id", "title", "status", "verification"],
      "properties": {
        "id": {
          "type": "string",
          "description": "Unique identifier (kebab-case)",
          "pattern": "^[a-z0-9-]+$"
        },
        "title": {
          "type": "string",
          "description": "Human-readable title"
        },
        "description": {
          "type": "string",
          "description": "Brief description of the feature"
        },
        "status": {
          "type": "string",
          "enum": ["planned", "in-progress", "blocked", "complete", "archived"],
          "description": "Current feature status"
        },
        "priority": {
          "type": "string",
          "enum": ["critical", "high", "medium", "low"],
          "default": "medium"
        },
        "feature_doc": {
          "type": "string",
          "description": "Path to detailed feature document"
        },
        "dependencies": {
          "type": "array",
          "items": { "type": "string" },
          "description": "IDs of features this depends on"
        },
        "verification": {
          "$ref": "#/definitions/verification"
        },
        "files": {
          "type": "array",
          "items": { "$ref": "#/definitions/file_entry" }
        },
        "decisions": {
          "type": "array",
          "items": { "type": "string" },
          "description": "Paths to decision log files"
        },
        "checkpoints": {
          "type": "array",
          "items": { "$ref": "#/definitions/checkpoint" }
        },
        "current_checkpoint": {
          "type": "string",
          "description": "Path to most recent checkpoint"
        },
        "created_at": {
          "type": "string",
          "format": "date-time"
        },
        "updated_at": {
          "type": "string",
          "format": "date-time"
        }
      }
    },
    "verification": {
      "type": "object",
      "required": ["file", "status"],
      "properties": {
        "file": {
          "type": "string",
          "description": "Path to verification checklist"
        },
        "status": {
          "type": "string",
          "enum": ["PENDING", "IN_PROGRESS", "VERIFIED", "BLOCKED", "NOT_APPLICABLE"]
        },
        "last_updated": {
          "type": "string",
          "format": "date-time"
        },
        "files_verified": {
          "type": "integer",
          "minimum": 0
        },
        "files_total": {
          "type": "integer", 
          "minimum": 0
        },
        "blocking_issues": {
          "type": "integer",
          "minimum": 0,
          "default": 0
        }
      }
    },
    "file_entry": {
      "type": "object",
      "required": ["path", "verification_status"],
      "properties": {
        "path": {
          "type": "string",
          "description": "File path relative to project root"
        },
        "action": {
          "type": "string",
          "enum": ["create", "modify", "delete"],
          "default": "create"
        },
        "depends_on": {
          "type": "array",
          "items": { "type": "string" },
          "description": "Paths of files this file depends on"
        },
        "verification_status": {
          "type": "string",
          "enum": ["PENDING", "IN_PROGRESS", "VERIFIED", "BLOCKED", "NOT_APPLICABLE"]
        },
        "verified_at": {
          "type": "string",
          "format": "date-time"
        }
      }
    },
    "checkpoint": {
      "type": "object",
      "required": ["timestamp", "file", "summary"],
      "properties": {
        "timestamp": {
          "type": "string",
          "format": "date-time"
        },
        "file": {
          "type": "string",
          "description": "Path to checkpoint file"
        },
        "summary": {
          "type": "string",
          "description": "Brief description of checkpoint state"
        }
      }
    }
  }
}
```

---

## Example features.json

```json
{
  "version": "2.0",
  "project": {
    "name": "Genixly",
    "description": "AI-powered product data infrastructure platform",
    "repository": "https://github.com/mwattier/genixly",
    "architecture_doc": "ARCHITECTURE.md"
  },
  "features": [
    {
      "id": "product-normalization",
      "title": "Product Data Normalization Service",
      "description": "Ingest product data from any platform and normalize into universal models",
      "status": "in-progress",
      "priority": "high",
      "feature_doc": "docs/features/product-normalization.md",
      "dependencies": ["graph-schema", "ingestion-api"],
      "verification": {
        "file": "verification/product-normalization.md",
        "status": "IN_PROGRESS",
        "last_updated": "2025-12-22T14:30:00Z",
        "files_verified": 2,
        "files_total": 5,
        "blocking_issues": 0
      },
      "files": [
        {
          "path": "schema/product.py",
          "action": "create",
          "depends_on": [],
          "verification_status": "VERIFIED",
          "verified_at": "2025-12-22T14:00:00Z"
        },
        {
          "path": "services/normalizer.py",
          "action": "create",
          "depends_on": ["schema/product.py"],
          "verification_status": "VERIFIED",
          "verified_at": "2025-12-22T14:15:00Z"
        },
        {
          "path": "services/writer.py",
          "action": "create",
          "depends_on": ["schema/product.py"],
          "verification_status": "PENDING"
        },
        {
          "path": "services/reader.py",
          "action": "create",
          "depends_on": ["schema/product.py", "services/writer.py"],
          "verification_status": "PENDING"
        },
        {
          "path": "api/product_routes.py",
          "action": "create",
          "depends_on": ["services/reader.py", "services/writer.py"],
          "verification_status": "PENDING"
        }
      ],
      "decisions": [
        "decisions/2025-12-22-uuid-for-identifiers.md",
        "decisions/2025-12-22-postgres-for-operational.md"
      ],
      "checkpoints": [
        {
          "timestamp": "2025-12-22T12:00:00Z",
          "file": "checkpoints/product-normalization-20251222-1200.md",
          "summary": "Completed schema definition"
        },
        {
          "timestamp": "2025-12-22T14:30:00Z",
          "file": "checkpoints/product-normalization-20251222-1430.md",
          "summary": "Completed normalizer service"
        }
      ],
      "current_checkpoint": "checkpoints/product-normalization-20251222-1430.md",
      "created_at": "2025-12-22T10:00:00Z",
      "updated_at": "2025-12-22T14:30:00Z"
    },
    {
      "id": "graph-schema",
      "title": "Neo4j Graph Schema",
      "description": "Define temporal graph schema for product relationships",
      "status": "complete",
      "priority": "critical",
      "feature_doc": "docs/features/graph-schema.md",
      "dependencies": [],
      "verification": {
        "file": "verification/graph-schema.md",
        "status": "VERIFIED",
        "last_updated": "2025-12-21T16:00:00Z",
        "files_verified": 3,
        "files_total": 3,
        "blocking_issues": 0
      },
      "files": [
        {
          "path": "graph/schema.py",
          "action": "create",
          "depends_on": [],
          "verification_status": "VERIFIED",
          "verified_at": "2025-12-21T15:00:00Z"
        },
        {
          "path": "graph/nodes.py",
          "action": "create",
          "depends_on": ["graph/schema.py"],
          "verification_status": "VERIFIED",
          "verified_at": "2025-12-21T15:30:00Z"
        },
        {
          "path": "graph/relationships.py",
          "action": "create",
          "depends_on": ["graph/schema.py", "graph/nodes.py"],
          "verification_status": "VERIFIED",
          "verified_at": "2025-12-21T16:00:00Z"
        }
      ],
      "decisions": [
        "decisions/2025-12-20-neo4j-for-relationships.md",
        "decisions/2025-12-21-temporal-versioning.md"
      ],
      "checkpoints": [],
      "created_at": "2025-12-20T09:00:00Z",
      "updated_at": "2025-12-21T16:00:00Z"
    },
    {
      "id": "ingestion-api",
      "title": "Data Ingestion API",
      "description": "REST API for ingesting product data from external sources",
      "status": "planned",
      "priority": "high",
      "feature_doc": "docs/features/ingestion-api.md",
      "dependencies": ["graph-schema"],
      "verification": {
        "file": "verification/ingestion-api.md",
        "status": "PENDING",
        "files_verified": 0,
        "files_total": 0,
        "blocking_issues": 0
      },
      "files": [],
      "decisions": [],
      "checkpoints": [],
      "created_at": "2025-12-22T10:00:00Z",
      "updated_at": "2025-12-22T10:00:00Z"
    }
  ]
}
```

---

## Migration from v1

If you have an existing features.json without verification:

### Add Required Fields

For each feature, add:

```json
{
  "verification": {
    "file": "verification/[feature-id].md",
    "status": "PENDING",
    "files_verified": 0,
    "files_total": 0,
    "blocking_issues": 0
  },
  "files": [],
  "decisions": [],
  "checkpoints": []
}
```

### Create Verification Files

For each feature, create `verification/[feature-id].md` using the template.

### Update Version

Change `"version": "1.0"` to `"version": "2.0"`

---

## Validation

Use the provided `scripts/validate-features.py` to validate your features.json:

```bash
python scripts/validate-features.py features.json
```

Validation checks:
- Schema compliance
- Required fields present
- Dependency graph is acyclic (no circular dependencies)
- Referenced files exist
- Status consistency (e.g., can't be "complete" with PENDING verification)

---

## Status Rules

### Feature Status vs Verification Status

| Feature Status | Allowed Verification Status |
|----------------|----------------------------|
| planned | PENDING |
| in-progress | PENDING, IN_PROGRESS, BLOCKED |
| blocked | BLOCKED (must have blocking_issues > 0) |
| complete | VERIFIED |
| archived | any (historical) |

### Automatic Status Transitions

When all files reach VERIFIED → Feature verification becomes VERIFIED
When any file becomes BLOCKED → Feature verification becomes BLOCKED
When blocking_issues reaches 0 and was BLOCKED → Feature verification becomes IN_PROGRESS
