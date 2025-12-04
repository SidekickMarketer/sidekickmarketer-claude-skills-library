---
name: sidekick-content-calendar
description: Generates monthly content calendars from approved strategies with dates, pillars, topics, formats, and caption outlines. References past posts to avoid duplicates and leverage top performers. Use when (1) creating first month's calendar for new client, (2) generating next month's content plan, (3) rebuilding calendar after strategy update. Requires channel strategy docs and optionally past post data.
---

# Sidekick Content Calendar Generator

Transform approved social media strategies into per-channel monthly content calendars with specific dates, formats, pillars, topics, caption outlines, and visual directions.

## Output Structure

```
07_Marketing_Channels/Social_Media/
├── Instagram/
│   └── Content_Calendars/
│       ├── YYYY-MM_IG_Calendar.csv
│       └── YYYY-MM_IG_Brief.md
├── Facebook/
│   └── Content_Calendars/
│       ├── YYYY-MM_FB_Calendar.csv
│       └── YYYY-MM_FB_Brief.md
├── GBP/
│   └── Content_Calendars/
│       ├── YYYY-MM_GBP_Calendar.csv
│       └── YYYY-MM_GBP_Brief.md
```

## Quick Start

Generate calendar structure with placeholder topics:

```bash
python scripts/generate_calendar.py --client-folder "{{client_folder}}" --month "2025-02" --platform instagram
python scripts/generate_calendar.py --client-folder "{{client_folder}}" --month "2025-02" --platform facebook
python scripts/generate_calendar.py --client-folder "{{client_folder}}" --month "2025-02" --platform gbp
```

This creates per-channel:
- `YYYY-MM_[PLATFORM]_Calendar.csv` - Post schedule with [TBD] placeholders
- `YYYY-MM_[PLATFORM]_Brief.md` - Overview with pillar/format distribution

Then fill in the topics, captions, and visuals using the phases below.

## Service Model Constraints

Sidekick operates a **photo-first** content strategy:
- 50-60% Carousels
- 30-35% Single Images
- 5-10% Monthly Recap Reel
- No daily Stories or video-first content

## Phase 1: Load Strategy & Context

### Step 1: Load Strategy Documents

```bash
# Load master strategy for cross-channel elements:
Read 07_Marketing_Channels/Social_Media/00_MASTER_STRATEGY.md

# Load channel-specific strategy for the platform:
Read 07_Marketing_Channels/Social_Media/Instagram/00_IG_STRATEGY.md    # For Instagram calendar
Read 07_Marketing_Channels/Social_Media/Facebook/00_FB_STRATEGY.md    # For Facebook calendar
Read 07_Marketing_Channels/Social_Media/GBP/00_GBP_STRATEGY.md        # For GBP calendar
```

Extract from master strategy:
- Content pillars with target percentages
- Brand voice guidelines
- Quarterly themes

Extract from channel strategy:
- Platform-specific posting frequency
- Format mix targets for this channel
- Best posting times
- Hashtag strategy (IG/FB) or none (GBP)
- Channel-specific KPIs

### Step 2: Calculate Monthly Requirements

From posting frequency in strategy:
```
Example calculation:
- Instagram: 5 posts/week × 4 weeks = 20 posts
- Facebook: 4 posts/week × 4 weeks = 16 posts
- GBP: 2 posts/week × 4 weeks = 8 posts
Total: 44 posts
```

### Step 3: Calculate Pillar Distribution

Apply pillar percentages to total posts:
```
Example for 44 posts:
- Student Success (30%): 13 posts
- Educational (25%): 11 posts
- Community (20%): 9 posts
- Instructor (15%): 7 posts
- Promotional (10%): 4 posts
```

### Step 4: Calculate Format Distribution

Apply photo-first targets per platform:
```
Example for 20 Instagram posts:
- Carousels (55%): 11 posts
- Single Images (35%): 7 posts
- Monthly Reel (10%): 2 posts
```

## Phase 1B: Load Past Performance (Avoid Duplicates)

This phase prevents topic repetition and leverages historical performance data.

### Step 4B.1: Load Audit Report (If Available)

```bash
# Check for recent audit report:
Read [client_folder]/07_Social_Media/04_Audit_Reports/[most_recent]_Social_Audit_COMPLETE.md

# Or check for metrics summary:
Read [client_folder]/07_Social_Media/04_Audit_Reports/metrics_summary.json
```

Extract from audit:
- **Top 5 performing posts** (topics, formats, pillars that worked)
- **Bottom 5 performers** (topics/formats to avoid or improve)
- **Best performing pillar** (lean into this)
- **Best performing format** (prioritize this format)
- **Engagement rate by day** (optimize posting days)

### Step 4B.2: Load Past 3 Months of Calendars

```bash
# Load recent content calendars to avoid topic duplication:
Read [client_folder]/07_Social_Media/01_Content_Calendars/[YYYY-MM-1]_*.csv
Read [client_folder]/07_Social_Media/01_Content_Calendars/[YYYY-MM-2]_*.csv
Read [client_folder]/07_Social_Media/01_Content_Calendars/[YYYY-MM-3]_*.csv

# Or check platform-specific calendars:
Read [client_folder]/07_Social_Media/Instagram/Content_Calendars/[recent].csv
```

Build a **"Recently Used Topics"** list:
- All topics from past 3 months
- Note which pillars have been heavy/light
- Flag any topics that appeared multiple times

### Step 4B.3: Load Performance Data (If Available)

```bash
# Check for performance insights CSVs:
List [client_folder]/07_Social_Media/02_Performance_Data/[YYYY-MM]/

# Load Instagram insights:
Read [client_folder]/07_Social_Media/02_Performance_Data/[YYYY-MM]/*_IG-Insights.csv

# Load Facebook insights:
Read [client_folder]/07_Social_Media/02_Performance_Data/[YYYY-MM]/*_FB-Insights.csv

# Load GBP insights:
Read [client_folder]/07_Social_Media/02_Performance_Data/[YYYY-MM]/*_GBP-Insights.csv
```

**CSV Column Reference (Agency Analytics Export Format):**

| Platform | Caption Column | Key Metrics Columns |
|----------|---------------|---------------------|
| Instagram | `Description` | `Reach`, `Likes`, `Comments`, `Shares`, `Saves`, `Post type` |
| Facebook | `Title` or `Description` | `Reach`, `Reactions`, `Comments`, `Shares`, `Post type` |
| GBP | `Post text` or `Summary` | `Views`, `Clicks`, `Calls`, `Impressions` |

**Sort by engagement to find top/bottom performers:**
- Instagram: Sort by `Saves` + `Shares` (high-intent actions)
- Facebook: Sort by `Shares` + `Comments`
- GBP: Sort by `Clicks` + `Calls`

Extract performance patterns:
- **High engagement posts:** What topics/formats drove saves, shares, comments?
- **Low engagement posts:** What fell flat?
- **Day/time patterns:** When did posts perform best? (check `Publish time` column)

### Step 4B.4: Create "Do More / Do Less" Summary

Based on loaded data, create actionable guidance:

| Do More (Top Performers) | Do Less (Underperformers) |
|--------------------------|---------------------------|
| Instructor spotlights on Saturdays | Generic "happy Monday" posts |
| Carousel tips (17%+ engagement) | Link posts without value |
| Student milestone celebrations | Promotional posts without story |
| [Client-specific insights] | [Client-specific insights] |

### Step 4B.5: Create "Already Covered" Exclusion List

Topics to NOT repeat this month:
```
Example exclusion list:
- "Meet Austin Atkinson" (done in October)
- "5 Practice Tips" carousel (done in November)
- "Why Learn Piano" (done twice in Q3)
- [Any topic used in past 90 days]
```

**Note:** If no past data exists (new client), skip this phase and rely on strategy + topic banks.

## Phase 2: Date & Theme Planning

### Step 5: Map Calendar Dates

Generate all dates in target month and identify posting days:
- Monday: High priority (IG + FB)
- Tuesday: Medium (IG + GBP)
- Wednesday: High (IG + FB)
- Thursday: Medium (IG + GBP)
- Friday: High (IG + FB)
- Saturday: Optional (light content)
- Sunday: Rest or prep

### Step 6: Identify Special Content Opportunities

Load `references/holiday_calendar.md`

Check for:
- Federal holidays
- Industry-specific dates
- Local events (from user input)
- Seasonal themes from strategy
- Client anniversaries

### Step 7: Block Avoid Dates

If `avoid_dates` provided, remove from posting schedule.

### Step 8: Assign Weekly Themes

Align with quarterly strategy theme:
```
February Example:
- Week 1: "New Year, New Skills"
- Week 2: "Valentine's Week"
- Week 3: "Mid-Winter Push"
- Week 4: "Month End Wins"
```

## Phase 3: Content Slot Assignment

### Step 9: Create Posting Schedule Grid

Assign post slots to dates by platform priority.

### Step 10: Distribute Pillars Across Calendar

Pillar placement rules:
- No pillar appears >2 consecutive days
- Promotional content spread throughout (not clustered)
- Student Success on high-engagement days (Mon, Wed)
- Educational content early in week
- Community content mid-to-end of week

### Step 11: Assign Formats to Slots

| Format | Best Days | Best Pillars |
|--------|-----------|--------------|
| Carousel | Mon, Wed, Fri | Educational, Tips, Before/After |
| Single Image | Any day | Testimonials, Quotes, Announcements |
| Monthly Reel | Last week | Recap, Highlights |

## Phase 4: Topic & Caption Development

### Step 12: Generate Topic Ideas

Load `references/topic_banks.md` for industry-specific inspiration.

**Cross-reference with Phase 1B data:**
1. Check "Already Covered" exclusion list—do NOT reuse these topics
2. Reference "Do More" list—prioritize similar topics/formats to top performers
3. Avoid patterns from "Do Less" list

For each pillar allocation, generate specific topics ensuring:
- **No duplicates from past 3 months** (check exclusion list)
- Variety (no repeated angles within this month)
- Seasonal relevance
- Special date alignment
- **Lean into proven performers** (similar formats/angles to past wins)

### Step 13: Create Caption Outlines

**Single Image format:**
```
Hook: [attention-grabber] | Body: [2-3 sentences] | CTA: [action]
```

**Carousel format:**
```
Hook: [curiosity driver] | Slides: 1-[intro], 2-X-[points], Final-[CTA] | Body: [context] | CTA: [save/share]
```

### Step 14: Add Visual Direction

For each post, specify:
- Photo type (candid, posed, graphic, before/after)
- Subject (student, instructor, product, location)
- Mood (warm, energetic, calm, professional)
- Key elements (faces, text overlay needs)

### Step 15: Assign Hashtags

Load `references/hashtag_banks.md`

Platform-specific sets:
- Instagram: 5-10 hashtags (branded + niche + local)
- Facebook: 1-3 hashtags
- GBP: No hashtags

## Phase 5: Validation & Output

### Step 16: Balance Check

Validate distributions:
- Pillar percentages within ±5% of targets
- Format percentages within ±10% of targets
- No empty date slots
- No back-to-back promotional posts

### Step 16B: Date Validation (REQUIRED)

**Before generating CSV, validate ALL dates match their actual day of week.**

```python
from datetime import datetime

def validate_dates(rows):
    errors = []
    for row in rows:
        date_obj = datetime.strptime(row['Date'], '%Y-%m-%d')
        actual_day = date_obj.strftime('%A')
        if row['Day'] != actual_day:
            errors.append(f"{row['Date']}: Listed '{row['Day']}' should be '{actual_day}'")
    return errors

# If ANY errors exist, fix before export
```

**Reference Calendar Generation:**
```python
import calendar
cal = calendar.TextCalendar()
print(cal.formatmonth(2026, 1))  # January 2026
```

Or use: https://www.timeanddate.com/calendar/

> ⚠️ **Common Error:** Off-by-one day mistakes when manually counting. ALWAYS validate programmatically.

### Step 17: Generate CSV

Load `references/calendar_template.md` for structure.

Create `YYYY-MM_[PLATFORM]_Calendar.csv` with columns:
- Date, Day, Format, Pillar, Topic
- Caption_Outline, Visual_Direction, Alt_Text, Hashtags, Status

### Step 18: Generate Supporting Documents

**YYYY-MM_[PLATFORM]_Brief.md:**
- Total posts count
- Monthly theme
- Weekly themes
- Pillar distribution table
- Special content notes
- Format distribution breakdown

### Step 19: Save Outputs

Per-channel folder structure:
```
07_Marketing_Channels/Social_Media/Instagram/Content_Calendars/YYYY-MM_IG_Calendar.csv
07_Marketing_Channels/Social_Media/Instagram/Content_Calendars/YYYY-MM_IG_Brief.md

07_Marketing_Channels/Social_Media/Facebook/Content_Calendars/YYYY-MM_FB_Calendar.csv
07_Marketing_Channels/Social_Media/Facebook/Content_Calendars/YYYY-MM_FB_Brief.md

07_Marketing_Channels/Social_Media/GBP/Content_Calendars/YYYY-MM_GBP_Calendar.csv
07_Marketing_Channels/Social_Media/GBP/Content_Calendars/YYYY-MM_GBP_Brief.md
```

## Quality Standards

Every calendar must include:
- Complete post for every slot
- Pillar distribution within ±5%
- Caption outline for every post
- Visual direction for every post
- **Alt text for every post** (descriptive, keyword-rich for accessibility + SEO)
- Platform-appropriate hashtags
- **Topics informed by past performance data (when available)**
- **Validated dates** (all Day values match actual calendar day for Date)

Every calendar must avoid:
- Empty date slots
- Generic topics ("post about business")
- Pillar imbalances >10%
- Repeated topics in same week
- **Duplicate topics from past 3 months** (check exclusion list from Phase 1B)
- **Formats/angles that underperformed historically**
- **Date/day mismatches** (always run Step 16B validation)

## References

### Skill References
- `../_shared/channel_benchmarks.md` - **Research-backed engagement data, posting times, and platform specs (2024-2025)**
- `references/calendar_template.md` - CSV structure and format examples
- `references/topic_banks.md` - Industry-specific topic ideas
- `references/holiday_calendar.md` - Key dates throughout year
- `references/hashtag_banks.md` - Hashtag sets by industry/platform

### Client Data Sources (Phase 1B)

**Performance Data (contains actual caption text + metrics):**
```
[client_folder]/07_Social_Media/02_Performance_Data/
├── YYYY-MM_Month/
│   ├── *_IG-Insights.csv    ← Instagram posts with `Description` column
│   ├── *_FB-Insights.csv    ← Facebook posts with `Title`/`Description` columns
│   └── *_GBP-Insights.csv   ← GBP posts with `Post text` column
```

**Audit Reports:**
- `[client_folder]/07_Social_Media/04_Audit_Reports/*_Social_Audit_COMPLETE.md` - Analyzed top/bottom performers

**Past Calendars (for topic deduplication):**
- `[client_folder]/07_Social_Media/01_Content_Calendars/YYYY-MM_*.csv`
