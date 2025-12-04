# Skill Design Patterns

## Pattern 1: High-Level Guide with References

Keep core workflow in SKILL.md, detailed docs in references.

```
skill/
├── SKILL.md              <- Core workflow only
└── references/
    ├── API_DOCS.md       <- Detailed API reference
    ├── EXAMPLES.md       <- Code examples
    └── TROUBLESHOOTING.md <- Error handling
```

**SKILL.md links to references:**
```markdown
## Advanced Features
- **API Reference**: See [references/API_DOCS.md](references/API_DOCS.md)
- **Examples**: See [references/EXAMPLES.md](references/EXAMPLES.md)
```

## Pattern 2: Domain-Specific Organization

For skills with multiple domains, organize by domain.

```
analytics-skill/
├── SKILL.md              <- Overview + navigation
└── references/
    ├── finance.md        <- Finance metrics
    ├── sales.md          <- Sales metrics
    └── marketing.md      <- Marketing metrics
```

Claude loads only the relevant domain file.

## Pattern 3: Framework Variants

For skills supporting multiple frameworks/tools.

```
deploy-skill/
├── SKILL.md              <- Workflow + selection guidance
└── references/
    ├── aws.md            <- AWS-specific patterns
    ├── gcp.md            <- GCP-specific patterns
    └── azure.md          <- Azure-specific patterns
```

## Pattern 4: Script-Heavy Skills

When automation is primary value.

```
data-skill/
├── SKILL.md              <- How to use scripts
├── scripts/
│   ├── parse.py          <- Step 1
│   ├── transform.py      <- Step 2
│   ├── analyze.py        <- Step 3
│   └── run_all.sh        <- One-command execution
└── references/
    └── SCHEMAS.md        <- Data schemas
```

**When to use:** Complex, multi-step operations that need consistency.

## Pattern 5: Data Transformation Skills

For skills that transform data between formats or systems.

```
import-skill/
├── SKILL.md              <- Transformation workflow
├── scripts/
│   ├── validate.py       <- Data validation
│   └── transform.py      <- Format conversion
└── references/
    ├── SOURCE_FORMAT.md  <- Input schema
    └── TARGET_FORMAT.md  <- Output schema
```

**When to use:** Converting between formats, importing/exporting data, data migration.

## Pattern 6: Content Generation Skills

For skills that create content based on templates and rules.

```
content-skill/
├── SKILL.md              <- Generation workflow
├── references/
│   ├── TEMPLATES.md      <- Content templates
│   ├── STYLE_GUIDE.md    <- Brand guidelines
│   └── EXAMPLES.md       <- Sample outputs
└── assets/
    └── template.docx     <- File templates
```

**When to use:** Generating reports, content, documents from structured data.

## Pattern 7: Analysis & Reporting Skills

For skills that analyze data and generate insights.

```
analytics-skill/
├── SKILL.md              <- Analysis workflow
├── scripts/
│   ├── aggregate.py      <- Data aggregation
│   └── visualize.py      <- Chart generation
└── references/
    ├── METRICS.md        <- KPIs and formulas
    └── BENCHMARKS.md     <- Industry standards
```

**When to use:** Performance analysis, reporting, data insights.

## Pattern Selection Guide

**Choose Pattern 1** when:
- Skill has detailed technical documentation
- Need to keep SKILL.md concise
- References are large or numerous

**Choose Pattern 2** when:
- Skill covers multiple distinct domains
- Each domain has separate knowledge base
- Users typically need one domain at a time

**Choose Pattern 3** when:
- Supporting multiple tools/frameworks
- Each variant has different steps
- User selects variant at runtime

**Choose Pattern 4** when:
- Automation is core value
- Operations are complex or error-prone
- Consistency is critical

**Choose Pattern 5** when:
- Converting between data formats
- Importing/exporting from systems
- Data validation is important

**Choose Pattern 6** when:
- Generating content from templates
- Brand consistency matters
- Multiple output formats needed

**Choose Pattern 7** when:
- Analyzing performance data
- Generating insights and reports
- Comparing against benchmarks

## Freedom Levels

**High freedom** (text instructions): Multiple valid approaches, context-dependent decisions.
- Example: "Analyze the data and identify trends"
- Use when: Creative tasks, strategic decisions

**Medium freedom** (pseudocode/parameters): Preferred pattern exists, some variation OK.
- Example: "Extract [field] from [source], validate against [schema]"
- Use when: Structured workflows with some flexibility

**Low freedom** (specific scripts): Fragile operations, consistency critical.
- Example: "Run `scripts/parse.py --input file.csv`"
- Use when: Exact operations required, error-prone steps

## Anti-Patterns

**Don't:**
- Include README.md, CHANGELOG.md, INSTALLATION_GUIDE.md
- Put version history in SKILL.md
- Duplicate info between SKILL.md and references
- Nest references more than one level deep
- Exceed 500 lines in SKILL.md
- Use second-person voice ("You should...")
- Include installation instructions (skills are auto-discovered)
- Add troubleshooting to SKILL.md (use references/)

**Do:**
- Keep SKILL.md focused on workflow
- Use imperative voice ("Run...", "Create...")
- Link to references for details
- Include trigger examples in description
- Validate inputs before processing
- Provide clear error messages
