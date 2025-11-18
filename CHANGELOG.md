# Changelog

All notable changes to the Project Context Keeper skill will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-01-17

### Added
- Initial release of Project Context Keeper skill
- `context: start` command to load project context
- `context: save` command to persist session updates
- `context: status` command to view current context
- Structured `devbridge-context.md` format with JSON schema
- Character limits on all fields for token efficiency
- User-led update interview (AI prompts, user provides)
- Git state tracking (branch, uncommitted changes, ahead_by)
- Support for blockers and warnings
- Files touched tracking
- Timestamp tracking (ISO 8601 format)

### Philosophy
- Token-efficient by design (character limits per field)
- User-led, AI-assisted (no automatic summaries)
- Schema-driven (strict structure enforcement)
- Explicit triggers only (no auto-spawning)

### Schema
- Project: 50 char max
- Goal: 120 char max
- Last completed: 200 char max
- Next action: 150 char max
- Tech stack: 8 items, 30 chars each
- Files touched: 15 items, 100 chars each
- Blockers: 3 items, 100 chars each
- Warnings: 3 items, 100 chars each

## [Unreleased] - Future Versions

### Planned for v2.0
- Progressive timeline (append history instead of overwrite)
- `context: automate` command for continuous-claude integration
- `context: history` command to view full timeline
- `context: insights` command for velocity metrics
- `context: resume-automation` command for checking automation progress
- Automation callback hooks
- Multi-project context management
- Notion sync integration
- Analytics and pattern recognition

### Under Consideration
- `context: export` for markdown reports
- `context: compare` to diff sessions
- `context: search` for full-text timeline search
- `context: forecast` for completion predictions
- Cost tracking for automation sessions
- Visual dashboards in Notion
