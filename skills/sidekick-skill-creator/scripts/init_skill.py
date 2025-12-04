#!/usr/bin/env python3
"""
Initialize a new skill with proper structure.
Usage: python init_skill.py <skill-name> --path <output-directory>
"""
import argparse
import os
import re
from pathlib import Path


def create_skill(skill_name: str, output_path: str):
    """Create a new skill directory with template files."""

    # Validate skill name format
    if not re.match(r'^[a-z0-9-]+$', skill_name):
        print(f"❌ Error: Skill name must be lowercase, alphanumeric, and hyphenated")
        print(f"   Valid examples: 'my-skill', 'data-processor', 'api-integration'")
        print(f"   Invalid: '{skill_name}'")
        return False

    if skill_name.startswith('-') or skill_name.endswith('-'):
        print(f"❌ Error: Skill name cannot start or end with a hyphen")
        return False

    if '--' in skill_name:
        print(f"❌ Error: Skill name cannot contain consecutive hyphens")
        return False

    skill_dir = Path(output_path) / skill_name

    if skill_dir.exists():
        print(f"❌ Error: {skill_dir} already exists")
        return False

    # Create directories
    skill_dir.mkdir(parents=True)
    (skill_dir / "scripts").mkdir()
    (skill_dir / "references").mkdir()
    (skill_dir / "assets").mkdir()

    # Create SKILL.md template
    skill_md = f'''---
name: {skill_name}
description: [WHAT it does]. Use when (1) [trigger scenario], (2) [another trigger], (3) [another trigger]. [Requirements or constraints].
---

# {skill_name.replace("-", " ").title()}

[One-line description of what this skill does]

## Usage

### Step 1: [First Step]
```bash
# Command or action
```

### Step 2: [Second Step]
```bash
# Command or action
```

## References
- `references/[REFERENCE_FILE].md` - [What it contains]
'''

    (skill_dir / "SKILL.md").write_text(skill_md)

    # Create example reference
    reference_md = f'''# {skill_name.replace("-", " ").title()} Reference

## Table of Contents
- [Section 1](#section-1)
- [Section 2](#section-2)

## Section 1
[Detailed information that would bloat SKILL.md]

## Section 2
[More detailed information]
'''

    (skill_dir / "references" / "REFERENCE.md").write_text(reference_md)

    # Create example script
    example_script = '''#!/usr/bin/env python3
"""
Example script - replace or delete this file.
"""
import argparse


def main():
    parser = argparse.ArgumentParser(description="Example script")
    parser.add_argument("--input", required=True, help="Input file")
    parser.add_argument("--output", required=True, help="Output file")
    args = parser.parse_args()

    # TODO: Implement script logic
    print(f"Processing {args.input} -> {args.output}")


if __name__ == "__main__":
    main()
'''

    script_path = skill_dir / "scripts" / "example_script.py"
    script_path.write_text(example_script)
    os.chmod(script_path, 0o755)

    print(f"✅ Created skill: {skill_dir}")
    print(f"")
    print(f"Structure:")
    print(f"  {skill_name}/")
    print(f"  ├── SKILL.md              <- Edit this first")
    print(f"  ├── scripts/")
    print(f"  │   └── example_script.py <- Replace or delete")
    print(f"  ├── references/")
    print(f"  │   └── REFERENCE.md      <- Add domain knowledge")
    print(f"  └── assets/               <- Add templates, images")
    print(f"")
    print(f"Next steps:")
    print(f"  1. Edit SKILL.md frontmatter (name, description)")
    print(f"  2. Write the workflow in SKILL.md body")
    print(f"  3. Add scripts/ if needed")
    print(f"  4. Add references/ for detailed docs")
    print(f"  5. Package: python package_skill.py {skill_dir}")

    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Initialize a new skill")
    parser.add_argument("skill_name", help="Name of the skill (e.g., my-skill)")
    parser.add_argument("--path", required=True, help="Output directory")
    args = parser.parse_args()

    create_skill(args.skill_name, args.path)
