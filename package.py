#!/usr/bin/env python3
"""
Package the project-context-keeper skill into a distributable .skill file.

Usage:
    python package.py
"""

import zipfile
from pathlib import Path
import sys

def package_skill():
    """Package the skill directory into a .skill file."""
    
    # Current directory
    skill_dir = Path.cwd()
    skill_name = skill_dir.name
    
    # Output file
    output_file = skill_dir / f"{skill_name}.skill"
    
    # Files to exclude
    exclude = {
        '.git', '.gitignore', '.DS_Store', '__pycache__',
        'package.py', f'{skill_name}.skill', '.vscode', 
        'node_modules', '.env'
    }
    
    print(f"Packaging skill: {skill_name}")
    print()
    
    # Validate SKILL.md exists
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        print("ERROR: SKILL.md not found")
        return False
    
    print("SKILL.md found")
    
    # Create the .skill file (zip format)
    try:
        with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Walk through all files
            for file_path in skill_dir.rglob('*'):
                if file_path.is_file():
                    # Skip excluded files/directories
                    if any(excluded in file_path.parts for excluded in exclude):
                        continue
                    
                    # Calculate relative path
                    arcname = file_path.relative_to(skill_dir.parent)
                    zipf.write(file_path, arcname)
                    print(f"  Added: {arcname}")
        
        print()
        print(f"SUCCESS: Packaged skill to {output_file}")
        print()
        print("Next steps:")
        print("  1. Test: Install in Claude Desktop and verify it works")
        print("  2. Commit: git add . && git commit -m 'Initial release'")
        print("  3. Tag: git tag -a v1.0.0 -m 'Version 1.0.0'")
        print("  4. Push: git push && git push --tags")
        
        return True
        
    except Exception as e:
        print(f"ERROR creating .skill file: {e}")
        return False

if __name__ == "__main__":
    success = package_skill()
    sys.exit(0 if success else 1)
