# Quick Setup Guide

## Repository Structure

```
project-context-keeper/
├── SKILL.md                    # Main skill definition
├── README.md                   # Documentation
├── CHANGELOG.md                # Version history
├── LICENSE                     # MIT License
├── CONTRIBUTING.md             # Contribution guidelines
├── .gitignore                  # Git ignore rules
├── package.py                  # Packaging script
├── examples/                   # Example context files
│   ├── example-in-progress.md
│   ├── example-needs-testing.md
│   └── example-blocked.md
└── project-context-keeper.skill # Distributable package (generated)
```

## Initial Git Setup

```bash
cd C:\GitHub\project-context-keeper

# Initialize git (if not already)
git init

# Add all files
git add .

# First commit
git commit -m "Initial release v1.0.0 - Project Context Keeper skill"

# Create release tag
git tag -a v1.0.0 -m "Version 1.0.0 - Initial release"

# Add remote (replace with your GitHub URL)
git remote add origin https://github.com/yourusername/project-context-keeper.git

# Push
git push -u origin main
git push --tags
```

## Creating New Releases

### When updating the skill:

```bash
# 1. Make your changes to SKILL.md or other files

# 2. Update CHANGELOG.md with new version

# 3. Repackage
python package.py

# 4. Commit
git add .
git commit -m "Version X.Y.Z - Brief description"

# 5. Tag
git tag -a vX.Y.Z -m "Version X.Y.Z"

# 6. Push
git push && git push --tags
```

## Testing the Skill

### Option 1: Install from .skill file

1. Open Claude Desktop
2. Go to Settings → Skills
3. Click "Add Skill"
4. Select `project-context-keeper.skill`
5. Verify it appears in your skills list

### Option 2: Install from directory

**Windows:**
```bash
# Copy to Claude's skills directory
xcopy /E /I /Y C:\GitHub\project-context-keeper "%APPDATA%\Claude\skills\user\project-context-keeper"
```

**Mac/Linux:**
```bash
cp -r ~/GitHub/project-context-keeper ~/Library/Application\ Support/Claude/skills/user/
```

### Test it works:

```
User: context: start
Claude: What is the absolute local_path for this project?
User: C:\test\my-project
Claude: No devbridge-context.md found. Would you like to create one?
```

## GitHub Repository Setup

### Create on GitHub:

1. Go to https://github.com/new
2. Repository name: `project-context-keeper`
3. Description: "Claude skill for managing project context across coding sessions"
4. Public or Private (your choice)
5. Don't initialize with README (you already have one)
6. Click "Create repository"

### Connect local to GitHub:

```bash
git remote add origin https://github.com/yourusername/project-context-keeper.git
git branch -M main
git push -u origin main
git push --tags
```

### Add topics to repository:

On GitHub, add these topics:
- `claude`
- `claude-skills`
- `development-tools`
- `project-management`
- `context-management`
- `devbridge`

## Distribution

### Release on GitHub:

1. Go to your repository on GitHub
2. Click "Releases" → "Create a new release"
3. Choose tag `v1.0.0`
4. Title: "Project Context Keeper v1.0.0"
5. Description: Copy from CHANGELOG.md
6. Attach `project-context-keeper.skill` file
7. Click "Publish release"

### Users can then:

```bash
# Download the .skill file from releases
# Install in Claude Desktop via Settings → Skills
```

## Maintenance

### Version numbering:

- **Major (X.0.0)**: Breaking changes (v2 with timeline)
- **Minor (1.X.0)**: New features (backward compatible)
- **Patch (1.0.X)**: Bug fixes

### Before each release:

1. ✅ Test with real projects
2. ✅ Update CHANGELOG.md
3. ✅ Update version in README if mentioned
4. ✅ Run `python package.py`
5. ✅ Test the .skill file installs correctly
6. ✅ Commit, tag, push

## Support

### Documentation:

- README.md: User-facing documentation
- CONTRIBUTING.md: Development guidelines
- CHANGELOG.md: Version history
- Examples: Sample context files

### Getting help:

- Issues: Report bugs or request features
- Discussions: Ask questions or share use cases
- Wiki: Extended documentation (optional)

---

**Current Status:**
- ✅ Repository structure complete
- ✅ Skill packaged as `project-context-keeper.skill`
- ✅ Ready for Git initialization
- ✅ Ready for GitHub push
- ⏳ Needs: Git init + remote setup
