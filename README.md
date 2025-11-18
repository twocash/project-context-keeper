# Project Context Keeper

A Claude skill for managing project context across coding sessions using a standardized `devbridge-context.md` file.

## Overview

This skill provides a systematic framework for persisting project context across multiple, token-limited coding sessions. It creates a lightweight handoff system that maintains state, goals, and progress between development sessions—whether those sessions are days apart or involve different developers (human or AI).

## Installation

### From GitHub

1. Download the latest release: `project-context-keeper.skill`
2. In Claude Desktop, go to Settings → Skills
3. Click "Add Skill" and select the downloaded `.skill` file

### From Source

```bash
git clone https://github.com/yourusername/project-context-keeper.git
cd project-context-keeper
# Copy to Claude's skills directory
cp -r . ~/Library/Application\ Support/Claude/skills/user/project-context-keeper/
# Windows: Copy to %APPDATA%\Claude\skills\user\project-context-keeper\
```

## Usage

### Start a Session

```
User: context: start
Claude: What is the absolute local_path for this project?
User: /Users/jim/projects/my-app
Claude: Context for My App loaded. State: in_progress. Ready to begin.
```

### Save a Session

```
User: context: save
Claude: What was completed this session?
User: Built authentication system with JWT tokens
[... interview continues ...]
Claude: ✅ Context saved to /Users/jim/projects/my-app/devbridge-context.md
```

### Check Status

```
User: context: status
Claude: [displays current context file contents]
```

## What Gets Tracked

The skill maintains a `devbridge-context.md` file in your project root with:

- **Project metadata**: Name, goal, tech stack, paths
- **Current state**: What phase the project is in
- **Last completed**: What was just finished
- **Next action**: What to do next session
- **Files touched**: Which files were modified
- **Blockers**: Active issues preventing progress
- **Warnings**: Important gotchas and antipatterns
- **Git state**: Current branch and commit status

## Features

### Token Efficient
- Character limits on all fields
- Schema-driven to prevent bloat
- Only loads what's needed

### Human-Checkable
- User provides updates (not AI summaries)
- Plain markdown format
- Git-friendly (commit the context file)

### Session Continuity
- Pick up exactly where you left off
- Works across days, weeks, or developers
- Preserves decision context

### AI-Friendly
- Structured format for parsing
- Clear state machine
- Explicit next actions

## Schema

The context file follows a strict JSON schema with field-level character limits:

- `project`: 50 chars max
- `goal`: 120 chars max
- `last_completed`: 200 chars max
- `next_action`: 150 chars max
- `tech_stack`: 8 items, 30 chars each
- `files_touched`: 15 items, 100 chars each
- `blockers`: 3 items, 100 chars each
- `warnings`: 3 items, 100 chars each

Full schema available in SKILL.md.

## Example Context File

```markdown
# DevBridge Context

project: DrumWave Calculator
goal: Financial modeling tool for retail media partnerships
tech_stack: [React, TypeScript, Node.js, Supabase]
state: in_progress

last_completed: Built JWT authentication system with token rotation and secure password hashing

next_action: Implement CRUD endpoints for Users, Posts, and Comments per API spec

blockers: []

files_touched:
- src/auth/auth.controller.ts
- src/auth/jwt.service.ts
- src/models/user.model.ts
- tests/auth.spec.ts

warnings:
- Rate limiting needed before production deploy
- JWT_SECRET must be rotated quarterly

git_state:
  branch: feature/auth
  uncommitted: false
  ahead_by: 3

timestamp: 2025-01-15T14:30:00Z
```

## Use Cases

### Solo Development
- Maintain context between coding sessions
- Remember why decisions were made
- Track progress over time

### Team Collaboration
- Onboard new developers quickly
- Handoff work between team members
- Document architectural decisions

### AI-Assisted Development
- Provide context to Claude Code or similar tools
- Enable continuous development workflows
- Support multi-session projects

### Consulting Projects
- Track client work systematically
- Generate status reports from context
- Maintain engagement continuity

## Philosophy

### User-Led, AI-Assisted
The AI doesn't summarize—you do. This is faster, more accurate, and keeps you in control. Claude prompts you for updates but doesn't generate them automatically.

### Be Brief
Token efficiency is paramount. Every field has character limits. Only capture what's essential. The context file is a handoff document, not a journal.

### Schema-Driven
The AI must follow the structure exactly. No improvisation. This ensures consistency and parsability across sessions.

### Explicit Triggers
The skill activates only on command (`context: start`, `context: save`). No auto-spawning. This makes behavior predictable and reduces token overhead.

## Roadmap

- **v2**: Progressive timeline (append history instead of overwrite)
- **v2**: Automation integration (continuous-claude hooks)
- **v2**: Analytics (velocity metrics, blocker patterns)
- **v2**: Multi-project management
- **v2**: Notion sync

See [CHANGELOG.md](CHANGELOG.md) for version history.

## Contributing

Contributions welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT License - see [LICENSE](LICENSE) for details.

## Author

Created by Jim Calhoun  
Website: https://takeflight.com  
LinkedIn: https://linkedin.com/in/jimcalhoun

## Acknowledgments

Built for managing complex consulting projects with AI-assisted development workflows. Inspired by the need for persistent context in token-limited environments.
