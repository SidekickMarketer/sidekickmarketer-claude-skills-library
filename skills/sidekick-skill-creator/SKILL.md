---
name: sidekick-skill-creator
description: Guide for creating effective Claude Skills. Use when (1) creating a new skill from scratch, (2) updating an existing skill's structure or content, (3) packaging a skill for distribution, (4) learning skill design patterns. Requires Python 3.x for automation scripts.
---

# Skill Creator

This skill provides comprehensive guidance for creating effective Claude Skills that extend Claude's capabilities with specialized knowledge, workflows, and tool integrations.

## When to Use This Skill

This skill activates when users want to:

**Create New Skills:**
- "Help me create a new skill for [domain/task]"
- "I need a skill that [does something specific]"
- "Build a skill template for [workflow]"

**Update Existing Skills:**
- "Update my skill's structure"
- "Improve the description of [skill-name]"
- "Add validation to my skill"

**Package Skills:**
- "Package my skill for distribution"
- "Validate my skill before sharing"
- "Create a .zip file from my skill folder"

**Learn Patterns:**
- "What design patterns work best for skills?"
- "Show me examples of well-structured skills"
- "How should I organize my skill's resources?"

## About Skills

Skills are modular, self-contained packages that extend Claude's capabilities by providing specialized knowledge, workflows, and tools. Think of them as "onboarding guides" for specific domains or tasks.

### What Skills Provide

1. Specialized workflows - Multi-step procedures for specific domains
2. Tool integrations - Instructions for working with specific file formats or APIs
3. Domain expertise - Company-specific knowledge, schemas, business logic
4. Bundled resources - Scripts, references, and assets for complex and repetitive tasks

### Anatomy of a Skill

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter (required: name, description)
│   │   Optional: license, allowed-tools, metadata
│   └── Markdown instructions
└── Bundled Resources (optional)
    ├── scripts/          - Executable code (Python/Bash/etc.)
    ├── references/       - Documentation loaded as needed
    └── assets/           - Files used in output (templates, images)
```

### Frontmatter Requirements

**Required fields:**
- `name` - Skill identifier (must match folder name)
- `description` - What it does and when to use it

**Optional fields:**
- `license` - License information
- `allowed-tools` - Tool restrictions
- `metadata` - Additional metadata

**Important:** Only these fields are allowed. Any other fields (like `version`) will cause upload errors.

### Progressive Disclosure

1. **Metadata** - Always in context (~100 words)
2. **SKILL.md body** - When skill triggers (<5k words)
3. **Bundled resources** - As needed (unlimited)

## Skill Creation Process

### Step 1: Understand with Concrete Examples

Ask questions to understand how the skill will be used:
- "What functionality should this skill support?"
- "Can you give examples of how it would be used?"
- "What would a user say that should trigger this skill?"

### Step 2: Plan Reusable Contents

Analyze each example to identify:
- Scripts needed for repetitive code
- References for domain knowledge/schemas
- Assets for templates/boilerplate

### Step 3: Initialize the Skill

**From the skill-creator directory**, run:

```bash
cd /path/to/sidekick-skill-creator
python scripts/init_skill.py <skill-name> --path <output-directory>
```

**Example:**
```bash
python scripts/init_skill.py my-new-skill --path ~/projects/claude-skills/skills
```

This creates:
- `SKILL.md` template with proper frontmatter
- `scripts/` directory with example script
- `references/` directory with example reference
- `assets/` directory (empty, ready for templates/images)

### Step 4: Edit the Skill

**Writing Style:** Use imperative/infinitive form (verb-first), not second person.

1. Start with reusable resources (scripts/, references/, assets/)
2. Delete example files not needed
3. Update SKILL.md answering:
   - What is the purpose?
   - When should it be used?
   - How should Claude use it?

### Step 5: Package the Skill

**From any directory**, run:

```bash
python /path/to/sidekick-skill-creator/scripts/package_skill.py <path/to/skill-folder> [output-directory]
```

**Example:**
```bash
python scripts/package_skill.py ~/projects/claude-skills/skills/my-new-skill
```

This will:
1. Validate skill structure and content
2. Check frontmatter completeness
3. Verify description quality
4. Create `skill-name.zip` in the skill's parent directory (or specified output)

**Validation checks:**
- ✅ SKILL.md exists with proper frontmatter
- ✅ Description includes trigger scenarios
- ✅ No forbidden files (README.md, CHANGELOG.md, etc.)
- ✅ SKILL.md under 500 lines

### Step 6: Iterate

1. Use the skill on real tasks
2. Notice struggles or inefficiencies
3. Update SKILL.md or bundled resources
4. Test again

## Example Output

After running `init_skill.py`, you'll get:

```
my-new-skill/
├── SKILL.md              ← Edit this first
├── scripts/
│   └── example_script.py ← Replace or delete
├── references/
│   └── REFERENCE.md      ← Add domain knowledge
└── assets/               ← Add templates, images
```

After running `package_skill.py`, you'll get:

```
my-new-skill.zip          ← Ready for distribution
```

## Best Practices

**Description Format:**
```yaml
description: [WHAT it does]. Use when (1) [trigger], (2) [trigger], (3) [trigger]. [Requirements].
```

**Writing Style:**
- ✅ Use imperative form: "Run...", "Create...", "Extract..."
- ❌ Avoid second person: "You should...", "Your skill will..."

**Progressive Disclosure:**
- Keep SKILL.md focused on workflow
- Move detailed docs to `references/`
- Link to references from SKILL.md

**Skill Naming:**
- Use lowercase, hyphenated names: `my-skill-name`
- Be descriptive but concise
- Match folder name exactly

## References

- `references/SKILL_TEMPLATE.md` - Blank skill template with checklist
- `references/DESIGN_PATTERNS.md` - Common skill patterns and anti-patterns
