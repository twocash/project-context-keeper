---
name: project-context-keeper
description: Manages project context across coding sessions with progressive timeline tracking. Loads, updates, and saves project state with full session history. Supports automation integration with continuous-claude.
license: (internal)
---

# Project Context Keeper v2

Progressive context management with timeline tracking. Preserves decision history, tracks velocity, and integrates with automation workflows.

## Core Philosophy

1. **Timeline, Not Snapshot:** Sessions append to history (nothing is lost)
2. **Decision Context:** Capture WHY, not just WHAT
3. **Human-Led Updates:** User provides summaries, AI prompts and structures
4. **Schema-Driven:** Strict structure for consistency
5. **Token-Efficient:** Character limits on all fields

## Commands

### Primary
* `context: start` - Load context, show current state and recent history
* `context: save` - End session, append to timeline
* `context: history` - View full timeline (last 10 sessions by default)
* `context: insights` - Show velocity metrics and patterns
* `context: automate` - Generate continuous-claude command from next_action

### Utility
* `context: status` - Quick view of current state only
* `context: resume-automation` - Check automation progress

---

## Workflows

### 1. Start Session: `context: start`

**User:** `context: start`

**AI Actions:**
1. Ask for project root directory (if not cached)
2. Look for `devbridge-context.md`

**If found:**
Read file and display:
```
Context for **[Project Name]** loaded.
📊 State: [state]
⏱️ Last: [X days ago] (Session [N], [duration])
✅ Completed: [last_completed summary]
🎯 Next: [next_action]

Recent Timeline:
- Session N: [summary] [duration]
- Session N-1: [summary] [duration]
- Session N-2: [summary] [duration]

Ready to begin.
```

**If not found:**
Offer to create. Prompt for: project name, goal, tech_stack.
Initialize with Session 1 in timeline.

---

### 2. Save Session: `context: save`

**User:** `context: save`

**AI Actions:**
Interview for updates (one question at a time):

1. "What was completed this session? (Be specific)"
2. "Any key decisions? (Decision / Rationale / Alternatives)"
3. "Any blockers resolved? (What / How / Time spent)"
4. "Next priority for next session?"
5. "Current state? (in_progress/needs_testing/ready_to_deploy/blocked)"
6. "Session duration in hours?"
7. "Files touched?"
8. [Detect Git commits if possible]

Then:
- Update "Current State" section (overwrite)
- Append new session to "Timeline" section (preserve)
- Compute and update "Insights" section
- Write to devbridge-context.md
- Confirm: "✅ Context saved. Session [N] added to timeline."

---

### 3. View History: `context: history`

**User:** `context: history` (or `context: history --last 5`)

**AI Actions:**
Parse timeline, display formatted:

```
📖 Timeline: [Project Name]

Session N • [Date], [Time] • [Type] • [Duration]
├─ Completed: [summary]
├─ Decisions: [if any]
├─ Resolved: [if any]
├─ Files: [count] files
└─ Next: [next priority]

[... more sessions ...]

📊 Summary:
- Total sessions: N (X human, Y automation)
- Days active: N
- Total duration: X hours
- Automation cost: $X.XX
```

---

### 4. Show Insights: `context: insights`

**User:** `context: insights`

**AI Actions:**
Parse timeline and compute:

```
📊 Project Insights: [Project Name]

Velocity:
- Sessions per week: X.X
- Avg session: X.X hours
- Features completed: N

Blocker Analysis:
1. [Blocker type]: N occurrences (avg Xmin to resolve)
2. [Blocker type]: N occurrences (avg Xmin to resolve)

Hot Files (most modified):
1. [file path] (X sessions)
2. [file path] (X sessions)

Automation Summary:
- Sessions: N
- Cost: $X.XX
- Success rate: X%

Recommendations:
- [Actionable insight based on patterns]
```

---

### 5. Trigger Automation: `context: automate`

**User:** `context: automate`

**AI Actions:**

1. Read current `next_action`
2. Analyze complexity
3. Break into sub-tasks
4. Estimate iterations and cost
5. Generate continuous-claude command
6. Add automation entry to timeline
7. Update state to `automation_running`

Display:
```
🤖 Automation Setup

Task: "[next_action]"

Sub-tasks:
1. [task 1]
2. [task 2]
3. [task 3]

Estimated: X-Y iterations
Estimated cost: $X-Y

Generated command:
────────────────────────────────────────
continuous-claude \
  --prompt "[detailed prompt with context]" \
  --max-runs X \
  --max-cost Y.00 \
  --owner [owner] \
  --repo [repo] \
  --notes-file .devbridge/automation-notes.md
────────────────────────────────────────

State changed: in_progress → automation_running

Ready to run?
```

---

### 6. Check Automation: `context: resume-automation`

**User:** `context: resume-automation`

**AI Actions:**

1. Check if state is `automation_running`
2. Read `.devbridge/automation-notes.md`
3. Check GitHub for recent PRs
4. Summarize progress

Display:
```
🤖 Automation Status

Started: X hours ago
Last update: X minutes ago

Progress:
✅ Iteration 1: [summary] (PR #X merged)
✅ Iteration 2: [summary] (PR #X merged)
🔄 Iteration 3: [summary] (PR #X pending)

Cost: $X.XX / $Y.00 budget

From notes: "[key excerpt]"

Options:
1. Let it continue
2. Pause to review
3. Stop automation
```

---

## File Structure

### Context File Format

```markdown
# DevBridge Context: [Project Name]

project: [name]
repo: [url]
local_path: [path]
created: [ISO timestamp]
last_updated: [ISO timestamp]
sessions_total: [count]

## Current State

state: [state]
next_action: [specific next step]
active_blockers: [list or none]
files_in_progress: [list]
automation_status:
  tool: [continuous-claude or none]
  started: [timestamp]
  iterations: [count]
  cost_spent: [amount]

## Timeline

### [ISO Timestamp] Session N
**Type:** Human Interactive | Automation  
**Duration:** X.X hours  
**State Change:** [from] → [to]

**Completed:**
[What was accomplished]

**Key Decisions:**
- [Decision]: [Rationale]

**Blockers Resolved:**
- [Blocker]: [How resolved] ([time spent])

**Files Touched:**
- [file path]
- [file path]

**Git Commits:** [hashes]

**Next Priority:**
[What to do next session]

**Notes for Next Dev:**
[Context that helps continuation]

---

[... previous sessions ...]

## Project Insights

**Velocity:**
- Sessions: N
- Days active: N
- Avg session: X.X hours
- Features: N

**Common Blockers:**
- [Type]: N occurrences

**Hot Files:**
1. [file]: N sessions
2. [file]: N sessions

**Automation:**
- Sessions: N
- Cost: $X.XX
- Success: X%
```

---

## Schema

### Current State (overwrites each save)

```json
{
  "state": "ready_to_start | in_progress | automation_running | automation_paused | needs_testing | blocked | ready_to_deploy | prod_deployed",
  "next_action": "string (max 200 chars)",
  "active_blockers": ["string (max 100 chars)", "..."],
  "files_in_progress": ["path (max 100 chars)", "..."]
}
```

### Timeline Entry (appends each save)

```json
{
  "timestamp": "ISO 8601",
  "session_id": "Session N",
  "session_type": "human_interactive | automation | code_review",
  "duration_hours": "number",
  "state_change": {"from": "state", "to": "state"},
  "completed": "string (max 300 chars)",
  "key_decisions": [
    {
      "decision": "string",
      "rationale": "string"
    }
  ],
  "blockers_resolved": [
    {
      "blocker": "string",
      "resolution": "string",
      "time_spent_minutes": "number"
    }
  ],
  "files_touched": ["path", "..."],
  "git_commits": ["hash", "..."],
  "automation_metadata": {
    "tool": "continuous-claude",
    "iterations": "number",
    "cost_usd": "number",
    "prs_merged": ["number", "..."]
  },
  "next_priority": "string (max 200 chars)",
  "notes_for_next": "string (max 300 chars)"
}
```

### Character Limits

- Project name: 50 chars
- Goal: 120 chars
- Completed summary: 300 chars
- Next action: 200 chars
- Notes for next: 300 chars
- Decision text: 150 chars each
- Blocker description: 100 chars
- File paths: 100 chars each

---

## Best Practices

### For Users

1. **Be specific in completions:** "Built auth" → "Built JWT auth with refresh token rotation"
2. **Document decisions:** Include WHY and what alternatives were rejected
3. **Track blocker time:** Helps identify patterns
4. **Estimate duration:** Enables velocity calculations
5. **Write notes for "future you":** What would help in a month?

### For Timeline Management

1. **Never delete entries:** Timeline is append-only
2. **Commit to Git:** Context file is your project memory
3. **Archive if >2000 lines:** Move old sessions to separate file
4. **Review quarterly:** Look for patterns in blockers/decisions

### For Automation

1. **Review automation-notes.md:** Before marking complete
2. **Check auto-merged PRs:** Code review still valuable
3. **Start conservative:** $2-3 budget, increase with confidence
4. **Use --disable-commits first:** Test behavior before real commits

---

## Migration from v1

If upgrading from v1 (snapshot-only):

**AI will detect v1 format and offer migration:**

1. Backs up v1 file: `devbridge-context-v1-backup.md`
2. Creates v2 structure:
   - Moves current fields to "Current State"
   - Creates "Timeline" with single entry from last save
   - Initializes "Insights" section
3. Preserves all existing data
4. Future saves append to timeline

**No data loss. Fully backward compatible.**

---

## Automation Integration

### Callback Hook

When continuous-claude completes, it can call:

```bash
~/.devbridge/scripts/automation-callback.sh
```

Which updates timeline with automation results.

### Context Injection

Before continuous-claude starts, inject project context:

```
You are working on [project].

Architecture decisions:
- [decision 1 from timeline]
- [decision 2 from timeline]

Code patterns:
- [pattern 1 from timeline]
- [pattern 2 from timeline]

Warnings:
- [warning 1 from current state]

Current task: [next_action]
```

This ensures automation follows established patterns.

---

## Advanced Features

### Multi-Project Support (Future)

Commands planned:
- `context: list` - Show all tracked projects
- `context: switch <n>` - Change active project
- `context: compare` - Cross-project status

### Notion Sync (Future)

Command planned:
- `context: sync-notion` - Create/update Notion page with timeline

### Analytics (Current)

`context: insights` computes:
- Velocity trends
- Blocker patterns
- Hot file analysis
- Automation ROI
- State duration tracking

---

## Triggers

This skill activates on:
- Explicit commands: "context: start", "context: save", etc.
- Questions about project state: "where are we?", "what's next?"
- Session handoffs: "continue from last time"
- Automation setup: "automate this task"

Does NOT auto-activate on:
- General coding questions
- File operations without context commands
- New conversations without project context reference

---

## Notes

- Timeline is append-only (never overwrites history)
- Current State section always shows latest snapshot
- Insights are computed automatically on each save
- Schema is strict to prevent token bloat
- All timestamps are ISO 8601 UTC
- File is Git-friendly markdown
- Compatible with continuous-claude automation
- Designed for token efficiency despite rich context
