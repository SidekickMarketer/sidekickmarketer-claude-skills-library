#!/usr/bin/env python3
"""
Package a skill into a distributable .skill file.
Usage: python package_skill.py <path/to/skill-folder> [output-directory]
"""
import argparse
import zipfile
import os
import re
from pathlib import Path


def validate_skill(skill_path: Path) -> list:
    """Validate skill structure and return list of errors."""
    errors = []

    # Check SKILL.md exists
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        errors.append("Missing SKILL.md")
        return errors  # Can't continue without SKILL.md

    # Check frontmatter
    content = skill_md.read_text()

    if not content.startswith("---"):
        errors.append("SKILL.md missing YAML frontmatter (must start with ---)")
    else:
        # Extract frontmatter
        match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if not match:
            errors.append("SKILL.md frontmatter not properly closed (missing ---)")
        else:
            frontmatter = match.group(1)

            # Check required fields
            if 'name:' not in frontmatter:
                errors.append("SKILL.md frontmatter missing 'name' field")
            else:
                # Check name matches folder name
                name_match = re.search(r'name:\s*(.+?)(?:\n|$)', frontmatter)
                if name_match:
                    skill_name = name_match.group(1).strip()
                    folder_name = skill_path.name
                    if skill_name != folder_name:
                        errors.append(f"Skill name '{skill_name}' does not match folder name '{folder_name}'")

            if 'description:' not in frontmatter:
                errors.append("SKILL.md frontmatter missing 'description' field")
            else:
                # Check description quality
                desc_match = re.search(r'description:\s*(.+?)(?:\n|$)', frontmatter, re.DOTALL)
                if desc_match:
                    desc = desc_match.group(1).strip()
                    if len(desc) < 50:
                        errors.append(f"Description too short ({len(desc)} chars). Include what it does AND when to use it.")
                    if 'use when' not in desc.lower() and 'when' not in desc.lower():
                        errors.append("Description should include 'Use when...' trigger scenarios")

            # Check for disallowed fields (per official Claude Skills spec)
            # Required: name, description
            # Optional: license, allowed-tools, metadata
            # No other fields are allowed
            allowed_fields = ['name', 'description', 'license', 'allowed-tools', 'metadata']
            field_match = re.findall(r'^([a-z-]+):', frontmatter, re.MULTILINE)
            for field in field_match:
                if field not in allowed_fields:
                    errors.append(f"Unexpected field '{field}' in frontmatter. Allowed fields: {', '.join(allowed_fields)}")

    # Check for forbidden files
    forbidden = ['README.md', 'CHANGELOG.md', 'INSTALLATION_GUIDE.md', 'QUICK_REFERENCE.md']
    for f in forbidden:
        if (skill_path / f).exists():
            errors.append(f"Remove {f} - skills should not contain human-facing documentation")

    # Check SKILL.md length
    lines = content.split('\n')
    if len(lines) > 500:
        errors.append(f"SKILL.md too long ({len(lines)} lines). Keep under 500 lines, move details to references/")

    return errors


def package_skill(skill_path: Path, output_dir: Path = None) -> bool:
    """Package skill into .skill file (zip)."""

    skill_name = skill_path.name

    # Validate first
    print(f"🔍 Validating {skill_name}...")
    errors = validate_skill(skill_path)

    if errors:
        print(f"❌ Validation failed:")
        for error in errors:
            print(f"   • {error}")
        return False

    print(f"✅ Validation passed")

    # Determine output path
    if output_dir is None:
        output_dir = skill_path.parent

    output_file = output_dir / f"{skill_name}.zip"

    # Create zip
    print(f"📦 Packaging...")
    with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(skill_path):
            # Skip hidden files and __pycache__
            dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
            files = [f for f in files if not f.startswith('.') and not f.endswith('.pyc')]

            for file in files:
                file_path = Path(root) / file
                arc_name = file_path.relative_to(skill_path)
                zf.write(file_path, arc_name)

    print(f"✅ Created: {output_file}")
    print(f"   Size: {output_file.stat().st_size / 1024:.1f} KB")

    return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Package a skill for distribution")
    parser.add_argument("skill_path", help="Path to skill folder")
    parser.add_argument("output_dir", nargs="?", default=None, help="Output directory (default: same as skill)")
    args = parser.parse_args()

    skill_path = Path(args.skill_path).resolve()
    output_dir = Path(args.output_dir).resolve() if args.output_dir else None

    if not skill_path.exists():
        print(f"❌ Error: {skill_path} not found")
        exit(1)

    success = package_skill(skill_path, output_dir)
    exit(0 if success else 1)
