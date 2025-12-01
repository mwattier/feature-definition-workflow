# Example: Data Export API Endpoint

This example demonstrates the conversational feature definition process for a simpler API feature.

---

## Initial Request

**User**: "Add an API endpoint that lets users export their data"

---

## The Conversation

**AI**: "I'll help you define this feature. Let me ask some clarifying questions:

1. What data should be exportable - all user data or specific entities?
2. What format(s) - CSV, JSON, XML, other?
3. Should this be a synchronous download or asynchronous (queued for large datasets)?
4. Are there size limits we should consider?
5. Who can export - only their own data, or can admins export for others?"

**User**: "
1. All user data - their profile, activity history, and any content they've created
2. CSV and JSON for now
3. Good question - probably queue if it's large. Let's say queue anything over 1000 records
4. Yes, max 100,000 records per export
5. Users can only export their own data. Admin export can be a separate feature later"

**AI**: "Thanks. A few more details:

6. For queued exports - how do users know when it's ready? Email notification?
7. How long should download links remain valid?
8. Should we track who exported what and when (audit trail)?
9. Any specific fields that should NOT be exported for privacy/security?"

**User**: "
6. Yes, email with download link
7. 7 days should be fine
8. Yes, good idea - log all exports
9. Don't include password hash or any internal system IDs that users shouldn't see"

---

## Feature Document (Quick Template)

# Feature: User Data Export API

**Status**: Approved
**Priority**: Medium
**Last Updated**: 2025-11-30

---

## Purpose

Allow users to download their personal data in CSV or JSON format for backup or portability.

## User Story

**As a** registered user
**I want to** export my data in a standard format
**So that** I can back it up or transfer it to another system

---

## How It Works

### Small Export (<1000 records)

1. User calls POST /api/export with format parameter
2. System generates export file immediately
3. System returns download URL
4. User downloads file
5. System logs export in audit trail

### Large Export (≥1000 records)

1. User calls POST /api/export with format parameter
2. System creates background job
3. System returns job ID and "processing" status
4. Background worker generates export file
5. System stores file with 7-day expiry
6. System sends email to user with download link
7. User downloads file within 7 days
8. System logs export in audit trail

### Edge Cases

**User tries to export while previous export is processing**:
- Return error: "Export already in progress"
- Include job ID and estimated completion time

**Export exceeds 100,000 record limit**:
- Return error: "Export too large, please filter data"
- Suggest using date range filters (future feature)

---

## Data Model

**ExportJob**
- `id`: UUID
- `user_id`: UUID (foreign key)
- `format`: enum[csv, json]
- `status`: enum[pending, processing, completed, failed]
- `record_count`: integer
- `file_url`: string (nullable, S3 path when complete)
- `expires_at`: timestamp (7 days from completion)
- `error_message`: string (nullable, if failed)
- `created_at`: timestamp
- `completed_at`: timestamp (nullable)

**Relationships**:
```
[User] --1:n--> [ExportJob]
```

---

## Implementation Notes

**API Endpoint**:
```
POST /api/export
Authentication: Required (JWT)

Request:
{
  "format": "csv" | "json"
}

Response (small export):
{
  "download_url": "https://...",
  "record_count": 542,
  "expires_at": "2025-12-07T10:00:00Z"
}

Response (large export):
{
  "job_id": "uuid",
  "status": "pending",
  "estimated_records": 5420
}
```

**GET /api/export/{job_id}**
```
Authentication: Required (JWT, must own job)

Response:
{
  "job_id": "uuid",
  "status": "completed",
  "download_url": "https://...",
  "record_count": 5420,
  "expires_at": "2025-12-07T10:00:00Z"
}
```

**Export Data Structure**:

CSV columns: `user_id, email, name, created_at, [activity fields], [content fields]`

JSON structure:
```json
{
  "exported_at": "2025-11-30T10:00:00Z",
  "user": {
    "id": "uuid",
    "email": "...",
    "name": "..."
  },
  "activity": [...],
  "content": [...]
}
```

**Excluded Fields**:
- password_hash
- internal_id
- Any system/admin fields

**Services**:
- ExportService: Generate export files
- ExportWorker: Background job processing
- EmailService: Send completion notifications

---

## Out of Scope

- ❌ Admin export for other users (separate feature)
- ❌ Scheduled/recurring exports
- ❌ Date range filtering (future enhancement)
- ❌ Excel format (may add later)
- ❌ Selective field export (export all or nothing for now)

---

## Success Criteria

- [ ] Small exports (<1000 records) download immediately
- [ ] Large exports (≥1000 records) are queued
- [ ] CSV format generates correctly
- [ ] JSON format generates correctly
- [ ] Email notifications sent when export ready
- [ ] Download links work for 7 days then expire
- [ ] Sensitive fields excluded from export
- [ ] All exports logged in audit trail
- [ ] User can only export their own data
- [ ] Appropriate error messages for edge cases

---

## features.json Entry

```json
{
  "id": "F004",
  "name": "User Data Export API",
  "description": "Allow users to export their data in CSV or JSON format",
  "status": "pending",
  "priority": "medium",
  "progress": 0,
  "estimatedEffort": "medium",
  "definitionDoc": "docs/features/04-data-export.md",
  "dependencies": ["F001"],
  "blockers": [],
  "acceptanceCriteria": [
    "Small exports download immediately",
    "Large exports are queued and emailed",
    "CSV and JSON formats both work",
    "Download links expire after 7 days",
    "Sensitive fields excluded",
    "Audit trail maintained"
  ],
  "subtasks": [
    {
      "id": "F004.1",
      "name": "Create ExportJob database schema",
      "status": "pending",
      "estimatedTime": "1h"
    },
    {
      "id": "F004.2",
      "name": "Implement CSV export logic",
      "status": "pending",
      "estimatedTime": "2h"
    },
    {
      "id": "F004.3",
      "name": "Implement JSON export logic",
      "status": "pending",
      "estimatedTime": "1.5h"
    },
    {
      "id": "F004.4",
      "name": "Create background job worker",
      "status": "pending",
      "estimatedTime": "2h"
    },
    {
      "id": "F004.5",
      "name": "Set up file storage (S3) with expiry",
      "status": "pending",
      "estimatedTime": "1.5h"
    },
    {
      "id": "F004.6",
      "name": "Implement email notification",
      "status": "pending",
      "estimatedTime": "1h"
    },
    {
      "id": "F004.7",
      "name": "Add audit logging",
      "status": "pending",
      "estimatedTime": "1h"
    },
    {
      "id": "F004.8",
      "name": "Write tests (unit + integration)",
      "status": "pending",
      "estimatedTime": "2h"
    }
  ]
}
```

---

## Lessons Learned

### What This Example Demonstrates

1. **Discovering Requirements Through Questions**: The async/queue approach wasn't in the original request but emerged through questions about size limits

2. **Edge Cases Matter**: Questions revealed edge cases like "what if user already has export running?" and "what if too large?"

3. **Security by Default**: Question about which fields to exclude revealed need to filter sensitive data

4. **Audit Trail**: Question about tracking revealed need for audit logging

5. **Quick Template Works**: This feature used the quick template since it's straightforward - notice it's still comprehensive but more concise

### Time Investment

- **Conversation**: ~10 minutes
- **Document Creation**: ~10 minutes
- **Total**: ~20 minutes

**Result**: Clear, implementable specification that covers security, performance, and edge cases.
