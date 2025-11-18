# DevBridge Context

project: Chase Partnership Portal
goal: Internal tool for managing retail media partnership proposals and tracking
tech_stack: [React, Node.js, PostgreSQL, Redis]
state: blocked

last_completed: Built proposal submission form with file upload. Integrated with S3 for document storage. Created approval workflow with email notifications.

next_action: Cannot proceed. Waiting for Chase legal team to approve data retention policies before implementing database schema. Next: Implement proposal database once legal approval received.

blockers:
- Legal approval pending for data retention policies (blocked since Jan 5)
- S3 bucket permissions need IT review (submitted ticket #4729)
- Database schema requires PII handling compliance review

files_touched:
- src/forms/ProposalForm.tsx
- src/api/proposals/upload.ts
- src/services/s3.service.ts
- src/emails/approval-notification.ts

warnings:
- All PII must be encrypted at rest (use encryption-service module)
- File uploads limited to 10MB per proposal (S3 cost containment)
- Do not implement database schema until legal approval

git_state:
  branch: feature/proposal-upload
  uncommitted: false
  ahead_by: 8

urls:
  repo: https://github.com/takeflight/chase-partnership-portal
  prod: https://partners.chase.internal

local_path: /Users/jim/clients/chase-partnership-portal
timestamp: 2025-01-08T11:20:00Z
session_id: session-2025-01-08
