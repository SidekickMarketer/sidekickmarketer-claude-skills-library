---
name: sidekick-social-audit
description: Rigorous forensic audit of client social media history analyzing long-term trends, seasonality, platform mix, and format effectiveness within Sidekick's photo-first service model. Use when conducting social media audits, performance analysis, or strategy pivots for any Sidekick Marketer client. Works with standardized client folder structure (Google Drive or local paths).
---

# Sidekick Marketer: Full-History Social Audit

## Objective
Perform a forensic audit of a client's social media history. Move beyond "vanity metrics" to identify the specific mechanics driving business results **within Sidekick's photo-first service model**.

**Scope:** Review the **ENTIRE** available history to understand trajectory, but weight *technical* analysis (formats/algorithms) toward the last 6-12 months.

**Service Model Context:** Sidekick operates a photo-first content strategy optimized for small businesses:
- High-quality designed graphics and carousels
- 1 monthly recap Reel (photo montage)
- No daily Stories or video-first strategy
- Focus on scalable, template-driven content

## Input Requirements

**User must provide ONE of:**
- `google_drive_folder_url: "https://drive.google.com/drive/folders/[id]"` 
- `client_folder_path: "/path/to/client-folder/"`

**Optional:**
- `client_name: "[Client Name]"` (if not provided, infer from folder name or CLIENT_PROFILE.md)

## Expected Folder Structure

This skill expects clients to use Sidekick's standardized folder structure:

```
client-[name]/
├── 00_[CLIENT]_CLIENT_PROFILE.md
└── 07_Social_Media/
    ├── 00_SOCIAL_STRATEGY.md
    ├── 01_Content_Calendars/
    │   └── YYYY-MM_Content_Calendar.csv
    ├── 02_Performance_Data/
    │   └── Platform_Analytics_YYYY_Q#.csv
    ├── 03_Post_Archive/
    │   └── YYYY-MM_Platform_Posts.pdf
    └── 04_Audit_Reports/
```

**If structure is non-standard:** Use `scripts/validate_folder_structure.py` to check setup, then attempt adaptive discovery.

## Phase 1: Archeology (Data Ingest)

### Step 1: Validate Folder Structure

**Run validation script:**
```bash
python scripts/validate_folder_structure.py --path {{client_folder_path}}
```

**If validation passes:**
- Proceed with standardized file paths
- All expected files are present

**If validation fails:**
- Review validation output for missing files/folders
- Attempt adaptive discovery (search by keywords)
- Document gaps in final report Appendix

### Step 2: Access the Client Folder

**For Google Drive URLs:**
```
1. Extract folder ID from URL
2. Use google_drive_fetch to view folder structure
3. Use google_drive_search to find files within 07_Social_Media/
```

**For local paths:**
```
1. Use view tool to scan directory structure
2. Use view to read specific files
```

### Step 3: Load Client Profile

**Read:** `00_[CLIENT]_CLIENT_PROFILE.md`

**Extract:**
- Client name (if not provided by user)
- Business type and target audience
- Current service deliverables
- Client start date

**If file is missing:**
- Attempt to infer client name from folder name
- Flag in report: "⚠️ Client profile missing. Recommend creating one."

### Step 4: Load Social Strategy

**Read:** `07_Social_Media/00_SOCIAL_STRATEGY.md`

**Extract:**
- Content pillar distribution with target percentages
- Posting frequency commitments by platform
- KPI targets (engagement rate, reach growth, conversions)

**If file is missing:**
- Flag in report: "⚠️ No documented strategy found"
- Infer strategy from actual execution
- Recommend creating strategy document

### Step 5: Inventory Available Data

**Scan subdirectories:**

**01_Content_Calendars/:**
- List all CSV files matching `YYYY-MM_Content_Calendar.csv`
- Identify date range (earliest to latest month)
- Count total posts

**02_Performance_Data/:**
- List all analytics files (CSV, XLSX)
- Identify platforms covered (Instagram, Facebook, GBP)
- Check for quarterly vs. monthly exports

**03_Post_Archive/:**
- List all PDF files
- Note if PDFs are available for analysis

**Output summary:**
```
Data Inventory:
✅ Content Calendars: 12 months (Jan 2024 - Dec 2024)
✅ Instagram Analytics: Q1-Q4 2024
✅ Facebook Analytics: Q1-Q4 2024
✅ GBP Analytics: Monthly Jan-Dec 2024
⚠️ Post Archive PDFs: Only 6 months available
```

### Step 6: Data Freshness Check

**Calculate:**
- Earliest data date
- Latest data date
- Months of data available

**If most recent data is >3 months old:**
- Flag in report: "⚠️ Analysis based on data through [DATE]. Recommend exporting current month before implementing changes."

## Phase 2: The Macro Analysis (The "Timeline")

Analyze the **full history** available to understand long-term trajectory:

### Growth Trajectory

**Calculate year-over-year (or period-over-period) changes:**
- Follower growth: Start vs. End
- Average engagement rate: Early period vs. Recent period
- Post volume: Has consistency improved?

**Categorize:**
- 📈 **Trending Up:** Growth >15% YoY
- ➡️ **Flat:** Growth -5% to +15% YoY
- 📉 **Trending Down:** Growth <-5% YoY

**Analysis points:**
- What changed between high and low periods?
- Did posting frequency impact growth?
- External factors (seasonality, campaigns, etc.)?

### Seasonality Detection

**Use:** `scripts/detect_seasonality.py` (if available) OR manual pattern analysis

**Identify:**
- Peak months (highest engagement/reach)
- Valley months (lowest engagement/reach)
- Business-specific patterns (e.g., "Back-to-school surge")

**Document implications:**
- Should we adjust posting frequency during valleys?
- Can we amplify successful seasonal content?
- Are there untapped seasonal opportunities?

### The "Hall of Fame"

**Sort all posts by total engagement:**
- Total engagement = likes + comments + shares + saves
- Identify Top 5-10 posts from entire history

**For each Hall of Fame post:**
- **Date:** When was it posted?
- **Metric:** Exact numbers (e.g., "5,000 views, 200 saves")
- **Theme/Format:** What was it about? (carousel, single image, topic)
- **Why it worked:** Your analysis of the success factors
- **Reboot potential:** Can this concept be refreshed and reposted?

**Key insight:** Look for "Old Gold" concepts from 1-2 years ago that could be rebooted with current formats.

## Phase 3: The Technical Deep Dive (The "Mechanics")

Analyze the **last 6-12 months** of content for current algorithm fit:

### A. Format Forensics (Photo-First Analysis)

**Within Sidekick's service model, categorize posts:**
1. **Static Single Image** (1 photo with caption)
2. **Carousels** (2-10 slides)
3. **Monthly Recap Reel** (photo montage - service deliverable)
4. **Text-Only** (rare, but note if present)

**For each format, calculate:**
- Average engagement rate
- Percentage of total feed
- Best-performing examples
- Worst-performing examples

**Analysis questions:**
- ✅ Do carousels outperform single images?
- ✅ Are longer carousels (8-10 slides) better than short ones (2-3)?
- ✅ Is the monthly Reel driving engagement or just a formality?
- ✅ Do posts with faces outperform product/location shots?
- ✅ Do text overlays impact performance?

**What NOT to flag:**
- ❌ "Need more Reels" (not part of service model)
- ❌ "Need daily Stories" (not part of service model)
- ❌ "Should post videos more often" (not scalable for this service)

**What TO flag:**
- ✅ "Carousels get 2.5x more engagement - increase from 20% to 50% of feed"
- ✅ "Single images with text overlays perform 40% better"
- ✅ "Faces in photos get 3x more engagement than product shots"

### B. Platform Mix & ROI Analysis

**Calculate volume distribution:**
- Instagram: X posts/month (% of total)
- Facebook: X posts/month (% of total)
- Google Business Profile: X posts/month (% of total)

**For each platform:**
- Volume (% of total posts)
- Average engagement rate
- Business ROI (inquiries, bookings, if tracked)
- Platform health (growing, stable, declining)

**Strategic questions:**
- Are we over-investing in a dying platform?
- Is there a winner being under-utilized?
- Should we reallocate effort based on ROI?

**Example findings:**
- "60% of effort on Facebook, but only 5% engagement rate" → Reduce
- "Instagram drives 80% of inquiries with 40% of posts" → Increase

### C. Content Pillar Distribution

**Tag posts by theme using content calendar data:**
- Review "Pillar" column in content calendars
- Categorize each post into documented pillars
- Calculate actual distribution

**Compare actual vs. stated strategy:**
```
Stated:  30% Student Success | 25% Instructor | 20% Educational | 15% Community | 10% Promotional
Actual:  10% Student Success | 60% Promotional | 30% Other
```

**Balance assessment:**
- Is the feed 90% promotional? (Red flag - audience fatigue)
- Is there enough value content? (Educational, inspirational)
- Are human stories featured enough? (Students, staff, community)

**For each pillar:**
- Target % vs. Actual %
- Performance (engagement rate vs. overall average)
- Analysis (is this pillar working? Over/under-represented?)

### D. Visual & Creative Patterns

**If post archive PDFs are available:**

Use `view` tool to examine sample posts for visual patterns:
- Brand consistency (colors, fonts, layouts)
- Photo quality (professional vs. casual)
- Text overlay usage and effectiveness
- Human presence (faces vs. objects)

**If analytics include saves/shares:**
- High saves = utility content (educational, how-to)
- High shares = emotional content (inspirational, relatable)
- High comments = conversation starters (questions, controversial)

## Phase 4: The Report

**Load template:** `references/social_audit_matrix.md`

**Before filling:**
1. Calculate `{{start_date}}` = earliest file date found
2. Calculate `{{end_date}}` = latest file date found
3. Calculate `{{data_months}}` = number of months analyzed
4. Set `{{report_date}}` = today's date

**Replace ALL {{placeholders}} with actual data:**
- Use specific numbers (not "many" or "some")
- Use exact percentages (e.g., "43.2%", not "about 40%")
- Include dates for Hall of Fame posts
- Fill all tables completely

**Report Writing Guidelines:**
- Use exact numbers and specific recommendations (e.g., "Shift carousel mix from 20% → 60%")
- Explain mechanism behind each finding (e.g., "High saves = utility content")
- Stay within photo-first service model constraints
- Prioritize by expected impact; be direct about what's broken
- Celebrate what IS working before critiquing

**Tone:**
- Direct, confident, data-driven
- No fluff or vague advice
- Call out what's not working
- Celebrate wins

## Phase 5: Deliver the Report

**Output the completed report:**
```markdown
[Paste entire filled social_audit_matrix.md content]
```

**Final checklist:**
- ✅ All {{placeholders}} replaced with real data
- ✅ Specific numbers in every recommendation
- ✅ "Hall of Fame" posts identified with dates and metrics
- ✅ Format forensics table complete with percentages
- ✅ Strategic pivot section is actionable (not vague)
- ✅ Red flags are technical and fixable
- ✅ 90-day action plan has specific tasks
- ✅ Report is ready to send to client

**Save report to:**
`07_Social_Media/04_Audit_Reports/YYYY-MM_Social_Audit.md`

---

## Handling Edge Cases

### Missing Strategy Documentation
**If 00_SOCIAL_STRATEGY.md doesn't exist:**
- Infer content pillars from actual posts (group by theme)
- Document: "No written strategy found - strategy inferred from execution"
- Recommend creating strategy document going forward

### Incomplete Analytics Data
**If analytics are partial or missing:**
- Perform qualitative-only analysis on available posts
- Document: "Quantitative analysis limited due to data gaps"
- Recommend setting up proper analytics exports

### Non-Standard File Naming
**If files don't match expected patterns:**
- Use adaptive search (search for keywords: "calendar", "analytics", "performance")
- Document actual structure in Appendix
- Suggest standardization for future audits

### Mixed Date Ranges
**If content calendars and analytics don't align:**
- Use the overlap period for quantitative analysis
- Note discrepancies in Data Quality section
- Use full calendar history for qualitative patterns

---

## Example Execution Flow

**User says:** "Run social audit for Cincinnati Music Academy"
**User provides:** `google_drive_folder_url: "https://drive.google.com/drive/folders/1abc123"`

**You do:**
1. Validate folder structure with `scripts/validate_folder_structure.py`
2. Use `google_drive_fetch` to access folder
3. Read `00_CMA_CLIENT_PROFILE.md` for client context
4. Read `07_Social_Media/00_SOCIAL_STRATEGY.md` for documented strategy
5. Inventory files in `01_Content_Calendars/`, `02_Performance_Data/`, `03_Post_Archive/`
6. Analyze full history for macro trends (Phase 2)
7. Analyze last 12 months for format performance (Phase 3)
8. Fill `references/social_audit_matrix.md` with findings
9. Output completed report
10. Save to `07_Social_Media/04_Audit_Reports/`

**Do NOT:**
- Skip validation step
- Make assumptions without data
- Recommend video-first strategies
- Recommend things outside Sidekick's service model
- Give vague advice like "post more consistently"

**DO:**
- Use actual numbers from the data
- Identify specific winning posts to replicate
- Call out what's broken with technical fixes
- Give exact percentages for format reallocation
- Stay within photo-first service constraints
