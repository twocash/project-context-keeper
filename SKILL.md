---
name: project-context-keeper
description: Manages project context across coding sessions with progressive timeline tracking. Auto-activates for any GitHub/coding work. Loads, updates, and saves project state with full session history. Supports incremental saves and automation integration.
license: (internal)
---

# Project Context Keeper v3

Progressive context management with timeline tracking and auto-activation. Preserves decision history, tracks velocity, enables incremental saves, and integrates with automation workflows.

## Core Philosophy

1. **Timeline, Not Snapshot:** Sessions append to history (nothing is lost)
2. **Auto-Activated:** Triggers on any GitHub/coding work without explicit command
3. **Incremental Saves:** Save individual features/milestones within a session
4. **Decision Context:** Capture WHY, not just WHAT
5. **Human-Led Updates:** User provides summaries, AI prompts and structures
6. **Schema-Driven:** Strict structure for consistency
7. **Token-Efficient:** Character limits on all fields

---

## Auto-Activation Triggers

This skill **automatically activates** when:

### Primary Triggers (Always Load Context)
- User mentions working on code in GitHub repositories
- User references a project by name that has a context file
- User asks to continue work from previous session
- User mentions file paths in `/c/GitHub/` or similar dev directories
- User discusses implementing features, fixing bugs, or refactoring
- User references Git operations (commit, push, branch, merge, PR)
- Conversation involves modifying code files in a tracked project

### Secondary Triggers (Offer Context Load)
- User asks about project status: "where are we?", "what's next?", "what did we do last time?"
- User mentions technical debt, blockers, or architectural decisions
- Session appears to be continuing previous development work

### Incremental Save Triggers (Auto-Prompt)
- Feature completion is confirmed during active session
- User says "that works", "feature complete", "milestone reached"
- Major decision point is reached
- Blocker is resolved
- User explicitly says "save this" or "checkpoint"

### Never Auto-Activate On
- General technical questions unrelated to active projects
- Research or learning tasks
- Reading documentation
- Casual conversation about coding

---

## Commands

### Primary
* `context: start` - Explicitly load context (auto-triggered in most cases)
* `context: save` - End session, append to timeline
* `context: checkpoint` - Save incremental progress without ending session
* `context: history` - View full timeline (last 10 sessions by default)
* `context: insights` - Show velocity metrics and patterns
* `context: automate` - Generate continuous-claude command from next_action

### Utility
* `context: status` - Quick view of current state only
* `context: resume-automation` - Check automation progress
* `context: skip` - Explicitly tell Claude not to load context for this session

---

## Workflows

### 0. Auto-Start (New in v3)

**When Triggered:** User mentions GitHub work without explicit command

**AI Actions:**
1. Detect project reference or path pattern
2. Check for `devbridge-context.md` in likely locations
3. If found: Load silently and display condensed status
4. If not found: Ask "Should I track context for this project?"

**Display (Condensed):**
```
📊 [Project Name] • [state] • Last: [X days ago]
✅ Last completed: [summary]
🎯 Next: [next_action]
```

Then proceed with user's request.

---

### 1. Explicit Start: `context: start`

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

### 2. Incremental Save: `context: checkpoint` (New in v3)

**User:** `context: checkpoint` or auto-triggered on feature completion

**AI Actions:**
Quick interview (2-3 questions):

1. "What just got completed?"
2. "Any decision or blocker to note?"
3. "Still working toward: [current next_action]?"

Then:
- Append mini-entry to current session's timeline
- Update files_touched list
- Keep session active (don't end it)
- Confirm: "✅ Checkpoint saved. Session continues."

**Mini-Entry Format:**
```markdown
#### Checkpoint: [Time]
- Completed: [summary]
- Files: [list]
- Decision: [if any]
```

---

### 3. Save Session: `context: save`

**User:** `context: save`

**AI Actions:**
Interview for updates (one question at a time):

1. "What was completed this session? (Include all checkpoints)"
2. "Any key decisions? (Decision / Rationale / Alternatives)"
3. "Any blockers resolved? (What / How / Time spent)"
4. "Next priority for next session?"
5. "Current state? (in_progress/needs_testing/ready_to_deploy/blocked)"
6. "Session duration in hours?"
7. "Files touched?" (pre-filled from checkpoints if any)
8. [Detect Git commits if possible]

Then:
- Consolidate any checkpoint entries into session summary
- Update "Current State" section (overwrite)
- Append new session to "Timeline" section (preserve)
- Compute and update "Insights" section
- Write to devbridge-context.md
- Confirm: "✅ Context saved. Session [N] added to timeline."

---

### 4. View History: `context: history`

**User:** `context: history` (or `context: history --last 5`)

**AI Actions:**
Parse timeline, display formatted:

```
📖 Timeline: [Project Name]

Session N • [Date], [Time] • [Type] • [Duration]
├─ Completed: [summary]
├─ Checkpoints: [count] (if any)
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

### 5. Show Insights: `context: insights`

**User:** `context: insights`

**AI Actions:**
Parse timeline and compute:

```
📊 Project Insights: [Project Name]

Velocity:
- Sessions per week: X.X
- Avg session: X.X hours
- Features completed: N
- Checkpoints per session: X.X (indicates granularity)

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

### 6. Trigger Automation: `context: automate`

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

### 7. Check Automation: `context: resume-automation`

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
checkpoints_total: [count]

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
**Checkpoints:** [count] (if any)

**Completed:**
[What was accomplished]

#### Checkpoint: [Time]
- Completed: [feature summary]
- Files: [list]
- Decision: [if any]

[Additional checkpoints...]

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
- Checkpoints: N

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
  "checkpoints": [
    {
      "timestamp": "ISO 8601 time only",
      "completed": "string (max 150 chars)",
      "files": ["path", "..."],
      "decision": "string (max 150 chars, optional)"
    }
  ],
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
- Checkpoint completed: 150 chars
- Next action: 200 chars
- Notes for next: 300 chars
- Decision text: 150 chars each
- Blocker description: 100 chars
- File paths: 100 chars each

---

## Best Practices

### For Users

1. **Let auto-trigger work:** Just start coding, context loads automatically
2. **Use checkpoints liberally:** Each feature completion = checkpoint
3. **Be specific in completions:** "Built auth" → "Built JWT auth with refresh token rotation"
4. **Document decisions:** Include WHY and what alternatives were rejected
5. **Track blocker time:** Helps identify patterns
6. **Write notes for "future you":** What would help in a month?

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

### For Checkpoints

1. **One feature = one checkpoint:** Don't bundle unrelated changes
2. **Note decisions at checkpoint:** Capture reasoning while fresh
3. **Update files list:** Accurate file tracking improves insights
4. **Don't over-checkpoint:** 3-5 per multi-hour session is typical

---

## Migration from v2

If upgrading from v2:

**AI will detect v2 format and enhance:**

1. Backs up v2 file: `devbridge-context-v2-backup.md`
2. Adds checkpoint structure to schema
3. Adds checkpoint count to insights
4. Future saves support checkpoint entries
5. Preserves all existing data

**No data loss. Fully backward compatible with v2 and v1.**

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

### Multi-Project Detection (v3)

AI maintains internal cache of active projects:
- When file paths match known projects, context auto-loads
- User can say "switch to [project]" to change active context
- Simultaneous work on multiple projects is tracked separately

### Smart Checkpoint Prompts (v3)

AI watches for completion signals:
- "that works", "looks good", "feature done"
- Successful test runs
- File modifications followed by user satisfaction
- Offers checkpoint without interrupting flow

### Analytics (Current)

`context: insights` computes:
- Velocity trends
- Checkpoint patterns (indicates development pace)
- Blocker patterns
- Hot file analysis
- Automation ROI
- State duration tracking

---

## Examples

### Example 1: Auto-Start

**User:** "I need to add OAuth support to the anchor-loop project"

**Claude:** 
```
📊 Anchor Loop • in_progress • Last: 2 days ago
✅ Last completed: Set up Supabase auth hooks
🎯 Next: Add OAuth provider configuration

Starting OAuth implementation...
```

### Example 2: Mid-Session Checkpoint

**User:** "Okay, Google OAuth is working now"

**Claude:**
```
Nice! Should I checkpoint this? 
[Yes/No/Continue]
```

**User:** "Yes"

**Claude:**
```
What files did you modify for Google OAuth?

[User provides list]

✅ Checkpoint saved: Google OAuth provider configured
Session continues. Next: Add Microsoft provider?
```

### Example 3: Session End with Multiple Features

**User:** "context: save"

**Claude:**
```
This session had 3 checkpoints:
1. Google OAuth configured
2. Microsoft OAuth added
3. Auth UI updated

Overall, what was the main accomplishment?

[Continue with standard save interview...]
```

---

## Notes

- Auto-triggers reduce friction in development workflow
- Timeline remains append-only (never overwrites history)
- Checkpoints enable fine-grained progress tracking
- Current State section always shows latest snapshot
- Insights now include checkpoint velocity metrics
- Schema is strict to prevent token bloat
- All timestamps are ISO 8601 UTC
- File is Git-friendly markdown
- Compatible with continuous-claude automation
- Designed for token efficiency despite rich context
- v3 maintains full backward compatibility with v1 and v2
