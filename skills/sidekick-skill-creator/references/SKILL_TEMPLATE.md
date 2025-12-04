# Skill Template

Copy this template when creating a new skill manually.

## Complete Template

**Frontmatter Fields:** Only `name` and `description` are required. Optional: `license`, `allowed-tools`, `metadata`. No other fields allowed.

```markdown
---
name: skill-name
description: [WHAT it does]. Use when (1) [trigger scenario], (2) [another trigger], (3) [another trigger]. [Requirements or constraints].
---

# Skill Name

[One-line description of what this skill does]

## When to Use This Skill

This skill activates when users want to:

**Primary Use Case:**
- "Example trigger phrase 1"
- "Example trigger phrase 2"

**Secondary Use Cases:**
- "Another scenario where this helps"

## Usage

### Step 1: [Action Name]

[Brief explanation of what this step does]

```bash
command here
```

**What this does:**
- Point 1
- Point 2

### Step 2: [Action Name]

[Brief explanation]

```bash
command here
```

## Outputs

| File | Purpose |
|------|---------|
| `output.md` | [What it contains] |
| `data.csv` | [What it contains] |

## Examples

**Example 1: Basic Usage**
```
User: "Do [task] for [context]"
Claude: [What happens]
```

**Example 2: Advanced Usage**
```
User: "Do [task] with [options]"
Claude: [What happens]
```

## Quality Standards

✅ Standard 1
✅ Standard 2
✅ Standard 3

## Time Estimate

| Step | Time |
|------|------|
| Step 1 | 5 min |
| Step 2 | 10 min |
| **Total** | **15 min** |

## Troubleshooting

**Issue: [Common problem]**
- Solution: [Fix]
- Solution: [Alternative]

## References

- `references/FILE.md` - [What it contains]
- `references/ANOTHER.md` - [What it contains]
```

## Description Examples

**Good Examples:**
```yaml
description: Generate monthly social media content calendars. Use when (1) planning content for upcoming month, (2) creating platform-specific posts, (3) aligning content with brand strategy. Requires client profile and strategy documents.
```

```yaml
description: Analyze social media performance data and generate insights. Use when (1) creating monthly reports, (2) identifying top-performing content, (3) recommending strategy improvements. Requires exported analytics data.
```

**Bad Examples:**
```yaml
# Too vague
description: Helps with social media

# Missing triggers
description: Generates content calendars for social media platforms

# Too long
description: This skill helps you create social media content by analyzing your brand voice, checking trends, generating posts for multiple platforms, scheduling them, and creating reports...
```

## Frontmatter Checklist

- [ ] `name` matches folder name exactly (lowercase, hyphenated)
- [ ] `description` explains WHAT it does (first sentence)
- [ ] `description` includes "Use when..." with 2-3 trigger scenarios
- [ ] `description` notes any requirements or constraints
- [ ] Only uses allowed fields: `name`, `description`, `license`, `allowed-tools`, `metadata`

## Body Checklist

- [ ] Under 500 lines (move details to references/)
- [ ] Uses imperative form ("Run...", "Create...", "Extract...")
- [ ] Includes "When to Use" section with trigger examples
- [ ] Links to references for detailed information
- [ ] No version history or changelogs
- [ ] No README-style documentation
- [ ] Includes example outputs or usage scenarios
