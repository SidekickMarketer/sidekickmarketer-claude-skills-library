---
name: sidekick-content-writer
description: Generates platform-optimized social media captions from calendar entries with proper hooks, CTAs, and hashtags. References past top-performing captions for style guidance. Use when (1) writing captions for monthly calendar batch, (2) creating single post for specific topic, (3) generating A/B caption variations. Requires per-channel content calendar.
---

# Sidekick Content Writer

Transform per-channel content calendar entries into polished, ready-to-post social media captions that match the client's brand voice, follow platform best practices, and drive engagement.

## Input/Output Structure

```
07_Marketing_Channels/Social_Media/
├── Instagram/
│   └── Content_Calendars/
│       ├── YYYY-MM_IG_Calendar.csv      ← INPUT
│       └── YYYY-MM_IG_Captions.md       ← OUTPUT
├── Facebook/
│   └── Content_Calendars/
│       ├── YYYY-MM_FB_Calendar.csv      ← INPUT
│       └── YYYY-MM_FB_Captions.md       ← OUTPUT
├── GBP/
│   └── Content_Calendars/
│       ├── YYYY-MM_GBP_Calendar.csv     ← INPUT
│       └── YYYY-MM_GBP_Captions.md      ← OUTPUT
```

## Service Model Constraints

Sidekick operates a **photo-first**, caption-driven approach:
- Visuals support the message
- Consistent brand voice across all content
- Scalable, template-driven writing patterns

## Phase 1: Load Context

### Step 1: Load Calendar Entries

```bash
# From per-channel CSV files:
Read 07_Marketing_Channels/Social_Media/Instagram/Content_Calendars/YYYY-MM_IG_Calendar.csv
Read 07_Marketing_Channels/Social_Media/Facebook/Content_Calendars/YYYY-MM_FB_Calendar.csv
Read 07_Marketing_Channels/Social_Media/GBP/Content_Calendars/YYYY-MM_GBP_Calendar.csv

# Parse all columns
# Filter by date_range if specified

# For single post:
Use provided post details directly
```

### Step 2: Load Brand Voice

From strategy or voice guide, extract:
- Tone attributes (e.g., "Warm, Expert, Approachable")
- Personality description
- Language level (casual/professional)
- Do's and Don'ts
- Emoji usage guidelines

### Step 3: Load Pillar Context

For each pillar being written, review:
- Pillar description from strategy
- Target audience for this pillar
- Goal (educate, inspire, convert)

## Phase 1B: Load Past Performance (Caption Intelligence)

Reference historical caption performance to inform writing style.

### Step 3B.1: Load Top Performing Posts

```bash
# Check audit report for top performers:
Read [client_folder]/07_Social_Media/04_Audit_Reports/[most_recent]_Social_Audit_COMPLETE.md

# Or load performance data CSVs (past 3 months):
Read [client_folder]/07_Social_Media/02_Performance_Data/[YYYY-MM]/*_IG-Insights.csv
Read [client_folder]/07_Social_Media/02_Performance_Data/[YYYY-MM]/*_FB-Insights.csv
Read [client_folder]/07_Social_Media/02_Performance_Data/[YYYY-MM]/*_GBP-Insights.csv
```

**CSV Column Reference (Agency Analytics Export Format):**

| Platform | Caption Column | Sort By (Top Performers) |
|----------|---------------|--------------------------|
| Instagram | `Description` | `Saves` + `Shares` (high-intent) |
| Facebook | `Title` or `Description` | `Shares` + `Comments` |
| GBP | `Post text` or `Summary` | `Clicks` + `Calls` |

**To find top performers:**
1. Load CSV files from past 2-3 months
2. Sort by engagement columns (Saves, Shares, Comments)
3. Extract the `Description` column from top 10 posts
4. Analyze caption patterns

Extract from top 5-10 performers:
- **Hook patterns** - What opening styles drove engagement? (first line of `Description`)
- **Caption length** - Shorter or longer captions?
- **CTA style** - Which calls-to-action got response? (last line of `Description`)
- **Tone** - Casual, inspiring, educational?
- **Emoji usage** - More or less?

### Step 3B.2: Identify Caption Patterns That Work

Build a "What Works" reference:

| Element | Top Performer Pattern | Example |
|---------|----------------------|---------|
| Hook style | Question-based | "What's the #1 mistake...?" |
| Length | 150-200 chars | Concise but complete |
| CTA | Soft engagement | "Drop a 🎵 if you agree" |
| Emoji | 1-2 per post | Start or end only |
| Tone | Celebratory | "We're so proud of..." |

### Step 3B.3: Note Patterns to Avoid

From underperforming posts:
- Generic openings that fell flat
- CTAs that got no response
- Caption lengths that underperformed
- Tone mismatches

**Note:** If no past data exists (new client), skip this phase and rely on brand voice guide + templates.

## Phase 2: Caption Generation

### Step 4: Process Each Calendar Entry

For each post, read:
- Date, Platform, Format, Pillar, Topic
- Caption_Outline, Visual_Direction, Hashtags

Apply in order:
1. Platform-specific character limits
2. Format-specific structure
3. Brand voice guidelines
4. Pillar-appropriate tone

### Step 5: Apply Platform Rules

Load `references/platform_specs.md`

| Platform | Ideal Length | Hashtags | Emoji | Tone |
|----------|--------------|----------|-------|------|
| Instagram | 125-200 chars (single), 300-500+ chars (carousel/educational) | 5-10 | Moderate | Conversational |
| Facebook | 40-80 chars (optimal) | 1-3 | Light | Community |
| GBP | 80-150 words | None | Minimal | Professional |

> **Note:** Niche/educational accounts (music schools, coaches) benefit from longer Instagram captions (300-500+ chars) for storytelling and proof content. GBP posts should front-load local SEO keywords.

### Step 6: Apply Format Rules

**Single Image:**
- Short, punchy caption
- Story-focused or value-quick
- Single clear CTA

**Carousel:**
- Longer caption acceptable
- Reference slides ("swipe through")
- Save/Share CTA emphasis

**Reel:**
- Very short (50-100 chars)
- High energy language
- Watch/Follow CTA

### Step 7: Apply Pillar Voice

Load `references/caption_templates.md` for pillar-specific patterns.

| Pillar | Tone | Key Words | CTA Style |
|--------|------|-----------|-----------|
| Student Success | Celebratory | "achieved", "journey" | "Your turn" |
| Educational | Helpful | "here's how", "mistake" | "Save this" |
| Behind-the-Scenes | Authentic | "meet", "day in life" | "Say hi" |
| Community | Warm | "grateful", "together" | "Tag a friend" |
| Promotional | Enthusiastic | "limited", "now open" | Clear action |

## Phase 3: Caption Structure

### Step 8: Write Hook

Load `references/hook_bank.md` for inspiration.

Hook appears in first line (visible before "...more"):
- Question hooks: "What's the #1 mistake..."
- Statement hooks: "This changed everything..."
- Story hooks: "3 months ago, Sarah couldn't..."

### Step 9: Write Body

Deliver value, story, or information:
- 2-4 sentences for single images
- Context for carousels ("swipe to see...")
- Keep paragraphs short (1-2 sentences each)

### Step 10: Write CTA

Load `references/cta_bank.md` for options.

Every post needs a clear call-to-action:
- Engagement: "Drop a [emoji] if..."
- Save: "Save this for later"
- Action: "Link in bio to..."
- Share: "Tag someone who needs this"

### Step 11: Add Hashtags

Use pre-assigned hashtags from calendar or generate:
- Instagram: 5-10 (branded + niche + local)
- Facebook: 1-3
- GBP: None

## Phase 4: Quality & Refinement

### Step 12: Voice Check

For each caption, verify:
- [ ] Matches brand tone attributes
- [ ] Uses appropriate vocabulary
- [ ] Follows emoji guidelines
- [ ] Feels authentic to client

### Step 13: Platform Optimization

**Instagram:**
- Hook in first line
- Line breaks for readability
- Hashtags at end

**Facebook:**
- Shorter is better
- Question-style hooks
- Minimal hashtags

**GBP:**
- Business-focused
- Clear contact/CTA
- No hashtags

### Step 14: Generate Variations (If Requested)

For high-priority posts, create A/B options:
- Different hook styles (question vs. statement)
- Different CTA approaches (direct vs. soft)
- Different lengths (short vs. expanded)

## Phase 5: Output

### Step 15: Format Output

Organize for easy copy/paste:

```markdown
# [CLIENT] - [MONTH] Captions

## Week 1

### Monday, [DATE]

---
**INSTAGRAM - Carousel - Educational**
Topic: [Topic]

[COMPLETE CAPTION - READY TO COPY]

Hashtags: [hashtag set]

---
**FACEBOOK - Single Image**
Topic: [Topic]

[COMPLETE CAPTION - READY TO COPY]

Hashtags: [hashtag set]
```

### Step 16: Save Output

Per-channel folder structure:
```
07_Marketing_Channels/Social_Media/Instagram/Content_Calendars/YYYY-MM_IG_Captions.md
07_Marketing_Channels/Social_Media/Facebook/Content_Calendars/YYYY-MM_FB_Captions.md
07_Marketing_Channels/Social_Media/GBP/Content_Calendars/YYYY-MM_GBP_Captions.md
```

Each file contains ready-to-copy captions organized by week and date.

## Quality Standards

Every caption must:
- Have a hook in the first line
- Match client brand voice
- Include a clear CTA
- Use appropriate platform length
- Have platform-appropriate hashtags
- Be ready to copy/paste

Every caption must avoid:
- Generic openings ("Check this out!")
- Mismatched tone
- Missing CTAs
- Wrong length for platform

## Batch Processing Tips

For full month (44+ posts):
1. Group by platform first
2. Then group by pillar
3. Write in batches (maintains voice consistency)
4. Review 2-3 captions after each batch

Time estimates:
- 44 posts: 30-45 minutes
- 12 posts (1 week): 10-15 minutes
- 4 posts (1 day): 5 minutes

## References

### Skill References
- `../_shared/channel_benchmarks.md` - **Research-backed engagement data, posting times, and platform specs (2024-2025)**
- `references/caption_templates.md` - Templates by pillar and format
- `references/hook_bank.md` - Opening hook examples by style
- `references/cta_bank.md` - Call-to-action options by goal
- `references/platform_specs.md` - Platform character limits and rules

### Client Data Sources (Phase 1B)

**Performance Data (contains actual caption text + metrics):**
```
[client_folder]/07_Social_Media/02_Performance_Data/
├── YYYY-MM_Month/
│   ├── *_IG-Insights.csv    ← Instagram captions in `Description` column
│   ├── *_FB-Insights.csv    ← Facebook captions in `Title`/`Description` columns
│   └── *_GBP-Insights.csv   ← GBP captions in `Post text` column
```

**Key columns for caption analysis:**
- `Description` / `Title` - The actual caption text
- `Publish time` - When posted
- `Post type` - Format (carousel, image, reel, etc.)
- `Saves`, `Shares`, `Comments` - Engagement metrics for sorting

**Audit Reports:**
- `[client_folder]/07_Social_Media/04_Audit_Reports/*_Social_Audit_COMPLETE.md` - Pre-analyzed top performers
