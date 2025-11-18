# Contributing to Project Context Keeper

Thank you for your interest in contributing! This skill is designed to help developers maintain context across coding sessions, and community input is valuable.

## How to Contribute

### Reporting Issues

If you encounter a bug or have a feature request:

1. Check existing issues to avoid duplicates
2. Create a new issue with:
   - Clear description of the problem or feature
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior
   - Your environment (OS, Claude version)

### Proposing Changes

For significant changes:

1. Open an issue first to discuss the proposal
2. Wait for feedback before starting work
3. Reference the issue in your pull request

### Code Contributions

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test thoroughly with actual projects
5. Commit with clear messages (`git commit -m 'Add amazing feature'`)
6. Push to your branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## Development Guidelines

### Skill Structure

```
project-context-keeper/
├── SKILL.md           # Main skill definition (required)
├── README.md          # Documentation
├── CHANGELOG.md       # Version history
├── LICENSE            # MIT License
├── CONTRIBUTING.md    # This file
└── examples/          # Example context files
```

### Editing SKILL.md

- Maintain YAML frontmatter format
- Keep token efficiency as priority
- Preserve schema structure
- Test with real projects before submitting

### Token Budget

This skill is designed to be token-efficient. When adding content:

- Challenge every paragraph: "Does Claude really need this?"
- Prefer examples over explanations
- Use concise language
- Respect character limits in schema

### Testing

Before submitting a PR:

1. Test with at least 2 different projects
2. Verify `context: start` loads correctly
3. Verify `context: save` preserves all fields
4. Verify `context: status` displays properly
5. Test with both new and existing context files

## Commit Message Guidelines

Use clear, descriptive commit messages:

```
feat: Add multi-project support
fix: Resolve character limit validation
docs: Update installation instructions
refactor: Simplify save workflow
test: Add example context files
```

## Pull Request Process

1. Update README.md with details of changes if needed
2. Update CHANGELOG.md following Keep a Changelog format
3. Ensure all fields in schema remain within character limits
4. Test with both Mac and Windows paths
5. Request review from maintainer

## Code of Conduct

### Our Standards

- Be respectful and inclusive
- Focus on what's best for the community
- Provide constructive feedback
- Accept constructive criticism gracefully

### Unacceptable Behavior

- Harassment or discriminatory language
- Personal attacks
- Publishing others' private information
- Other conduct deemed inappropriate

## Questions?

- Open an issue for questions about contributing
- Tag maintainers for urgent matters
- Check existing discussions before posting

## Attribution

This CONTRIBUTING.md is adapted from standard open source guidelines and tailored for Claude skills development.

Thank you for contributing! 🎉
