# Project Context Keeper v3

A Claude skill for managing development context across coding sessions with progressive timeline tracking, auto-activation, and incremental saves.

## What's New in v3

### Auto-Activation
- No more manual `context: start` commands for most work
- Automatically detects when you're working on GitHub projects
- Silently loads context and shows condensed status
- "Just start coding" - context management happens in background

### Incremental Saves (Checkpoints)
- Save individual features/milestones within a session
- Use `context: checkpoint` or let Claude detect completion signals
- Each checkpoint captures what was done + files touched
- Session end consolidates all checkpoints into full session entry

### Smarter Triggers
- Detects GitHub paths, project names, Git operations
- Recognizes completion signals: "that works", "feature done", etc.
- Offers checkpoints without interrupting flow
- Multi-project awareness (caches active projects)

## Quick Start

### First Time Setup

1. Start working on a GitHub project
2. Claude will detect and ask: "Should I track context for this project?"
3. Provide project name, goal, tech stack
4. Context file created at `[project-root]/devbridge-context.md`

### Daily Usage

**Start working:**
```
User: "I need to add OAuth to anchor-loop"
Claude: 📊 Anchor Loop • in_progress • Last: 2 days ago
        ✅ Last: Set up Supabase auth
        🎯 Next: OAuth configuration
        
        Starting OAuth work...
```

**Mid-session checkpoint:**
```
User: "Google OAuth is working"
Claude: Nice! Checkpoint this? [Yes/No]
User: Yes
Claude: ✅ Checkpoint saved. Session continues.
```

**End session:**
```
User: context: save
Claude: [Interviews for session summary, including all checkpoints]
        ✅ Context saved. Session 42 added to timeline.
```

## Commands

### Primary
- **Auto-start** - Just mention your GitHub project
- `context: save` - End session, save to timeline
- `context: checkpoint` - Save progress mid-session
- `context: history` - View past sessions
- `context: insights` - Velocity metrics and patterns

### Utility
- `context: status` - Quick state check
- `context: skip` - Don't load context this time
- `context: automate` - Generate continuous-claude command

## File Structure

Context is stored as `devbridge-context.md` in your project root:

```
project-root/
├── devbridge-context.md    ← Your project memory
├── .devbridge/
│   └── automation-notes.md ← Automation logs (if used)
└── [your code]
```

The context file contains:
- **Current State** - Latest snapshot (overwritten each save)
- **Timeline** - Append-only session history with checkpoints
- **Insights** - Auto-computed velocity and pattern analysis

## Schema

### Session Entry
- Timestamp, duration, state changes
- Completed work summary
- Checkpoint entries (if any)
- Key decisions with rationale
- Blockers resolved with time spent
- Files touched + Git commits
- Next priority + notes for future

### Checkpoint Entry
- Timestamp within session
- What was completed (150 char max)
- Files modified
- Optional decision note

## Best Practices

### For Checkpoints
- One feature = one checkpoint
- Don't over-checkpoint (3-5 per multi-hour session)
- Capture decisions while fresh
- Update files list accurately

### For Context Management
- Let auto-trigger handle loading
- Use explicit `context: start` only when auto-detection fails
- Commit context file to Git (it's project memory)
- Review `context: insights` quarterly for patterns

### For Timeline
- Never delete entries (append-only)
- Be specific in completions
- Document decision rationale
- Track blocker resolution time

## Integration

### With continuous-claude
- Generate automation commands via `context: automate`
- Context is injected into automation prompts
- Automation sessions saved to timeline with cost tracking
- Resume with `context: resume-automation`

### With Git
- Context file is markdown (Git-friendly)
- Commit after significant milestones
- Include in `.gitignore` if context contains sensitive info
- Checkpoint helps tie context to specific commits

## Migration

### From v2
- Automatic detection and upgrade
- Backup created: `devbridge-context-v2-backup.md`
- All data preserved
- New checkpoint structure added
- Future saves support checkpoints

### From v1
- Two-step migration (v1 → v2 → v3)
- Snapshot converted to timeline entry
- All existing data preserved

## Philosophy

1. **Timeline, Not Snapshot** - History is append-only
2. **Auto-Activated** - Context management fades into background
3. **Incremental Progress** - Checkpoint granular wins
4. **Decision Context** - Capture WHY, not just WHAT
5. **Human-Led** - You summarize, AI structures
6. **Token-Efficient** - Character limits prevent bloat

## Examples

See SKILL.md for detailed examples of:
- Auto-start workflows
- Mid-session checkpointing
- Session end with multiple features
- Automation setup and monitoring
- Timeline analysis and insights

## License

Internal use only.

## Version

Current: v3.0  
Compatible with: v2.x, v1.x (with auto-migration)
