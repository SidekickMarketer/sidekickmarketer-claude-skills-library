# Sidekick Social Audit Skill

Complete skill package for conducting forensic social media audits for Sidekick Marketer clients.

## What This Skill Does

Performs a comprehensive audit of a client's social media history, analyzing:
- **Long-term trends** (follower growth, engagement trajectory)
- **Seasonality patterns** (peak months, valleys, business cycles)
- **Format effectiveness** (carousels vs. single images, photo-first optimization)
- **Platform mix & ROI** (Instagram, Facebook, Google Business Profile)
- **Content pillar distribution** (stated strategy vs. actual execution)
- **Strategic pivots** (data-driven recommendations for next 90 days)

**Key differentiator:** Optimized for Sidekick's **photo-first service model** (designed graphics, carousels, 1 monthly Reel) rather than generic video-first advice.

---

## Quick Start

### 1. Install the Skill

Upload the `.skill` file to Claude via the Skills menu.

### 2. Set Up Client Folder

```bash
python scripts/setup_client_folder.py \
  --client-name "Your Client Name" \
  --output-dir ~/clients \
  --short-code clientcode
```

### 3. Fill Required Files

- `00_[CLIENT]_CLIENT_PROFILE.md` - Business context, deliverables
- `07_Social_Media/00_SOCIAL_STRATEGY.md` - Content pillars, KPIs
- Import historical data to `01_Content_Calendars/` and `02_Performance_Data/`

### 4. Validate Setup

```bash
python scripts/validate_folder_structure.py --path ~/clients/client-code
```

### 5. Run Audit in Claude

```
User: "Run social audit for [Client Name]"
Provide: folder path or Google Drive URL
```

### 6. Validate Report

```bash
python scripts/validate_report.py \
  --report path/to/completed/audit.md
```

---

## Package Contents

```
sidekick-social-audit/
├── SKILL.md                              # Main skill instructions
├── README.md                             # This file
├── scripts/                              # Automation scripts
│   ├── setup_client_folder.py           # Create standardized folders
│   ├── validate_folder_structure.py     # Check folder requirements
│   ├── parse_social_data.py             # Parse analytics CSVs
│   ├── calculate_engagement.py          # Standardized engagement rates
│   ├── validate_report.py               # Check completed reports
│   └── README.md                         # Scripts documentation
└── references/                           # Templates & resources
    ├── social_audit_matrix.md            # Report template
    ├── CLIENT_PROFILE_TEMPLATE.md        # Client profile template
    └── SOCIAL_STRATEGY_TEMPLATE.md       # Strategy doc template
```

---

## Expected Client Folder Structure

The skill expects clients to use this standardized structure:

```
client-[name]/
├── 00_[CLIENT]_CLIENT_PROFILE.md          # Required
└── 07_Social_Media/                       # Required
    ├── 00_SOCIAL_STRATEGY.md              # Required
    ├── 01_Content_Calendars/              # Required
    │   └── YYYY-MM_Content_Calendar.csv
    ├── 02_Performance_Data/               # Required
    │   └── Platform_Analytics_YYYY_Q#.csv
    ├── 03_Post_Archive/                   # Optional
    │   └── YYYY-MM_Platform_Posts.pdf
    └── 04_Audit_Reports/                  # Generated
```

---

## Key Features

### ✅ Standardized Analysis
- Consistent methodology across all clients
- Platform-specific engagement formulas
- Industry benchmark comparisons

### ✅ Service Model Aware
- Optimized for photo-first content strategy
- Doesn't recommend things Sidekick doesn't offer
- Focuses on scalable, template-driven solutions

### ✅ Actionable Insights
- Specific format allocation recommendations (e.g., "40% → 60% carousels")
- Technical red flags with exact fixes
- 90-day action plan with weekly tasks

### ✅ Quality Automation
- Scripts handle tedious data processing
- Validation catches missing placeholders
- Pre-delivery quality checks

---

## Use Cases

### Monthly/Quarterly Client Reviews
Run audits before strategy sessions to arrive with data-driven recommendations.

### New Client Onboarding
Establish baseline performance and identify quick wins.

### Service Tier Upgrades
Demonstrate value with comprehensive analysis to justify Growth/Professional tier upgrades.

### Internal Training
Use completed audits as case studies for team training.

---

## Requirements

### Minimum (Skill Only)
- Claude with Skills enabled
- Client folder with required files

### Recommended (Full Workflow)
- Python 3.8+ (for automation scripts)
- Google Drive or local file access
- Analytics exports (CSV format preferred)

### Optional (Enhanced Features)
- `openpyxl` for XLSX support
- `PyPDF2` + `pytesseract` for PDF extraction

---

## Tips for Best Results

### Data Quality Matters
- **More history = better trends:** 12+ months ideal
- **Consistent exports:** Use same export settings
- **Complete calendars:** Include all posts, not just top performers

### Document Strategy
- Fill out SOCIAL_STRATEGY.md completely
- Define content pillars with target percentages
- Set realistic KPI targets

### Review Before Delivery
- Always run `validate_report.py` before sending to client
- Check for unfilled {{placeholders}}
- Ensure specific numbers (not vague "many" or "several")

---

## Example Workflow

**Scenario:** Running audit for Cincinnati Music Academy

```bash
# 1. Setup (one-time)
python scripts/setup_client_folder.py \
  --client-name "Cincinnati Music Academy" \
  --output-dir ~/Google\ Drive/Clients \
  --short-code cma

# 2. Fill required docs (manual)
# - Complete CLIENT_PROFILE.md
# - Complete SOCIAL_STRATEGY.md
# - Import 12 months of content calendars
# - Import Q1-Q4 analytics

# 3. Validate
python scripts/validate_folder_structure.py \
  --path ~/Google\ Drive/Clients/client-cma \
  --verbose

# 4. Optional: Preprocess data
python scripts/parse_social_data.py \
  --search-dir ~/Google\ Drive/Clients/client-cma/07_Social_Media/02_Performance_Data/ \
  --output ~/temp/cma-data.json

python scripts/calculate_engagement.py \
  --json-file ~/temp/cma-data.json \
  --output ~/temp/cma-enriched.json

# 5. Run audit in Claude
# Provide Google Drive URL or local path

# 6. Validate completed report
python scripts/validate_report.py \
  --report ~/Google\ Drive/Clients/client-cma/07_Social_Media/04_Audit_Reports/2024-11_Social_Audit.md

# 7. Deliver to client ✅
```

---

## Troubleshooting

### "Folder structure not found"
→ Run `validate_folder_structure.py` to see what's missing
→ Ensure you're using standardized naming conventions

### "No analytics data"
→ Audit will run in qualitative-only mode
→ Export platform analytics and retry

### "Report has unfilled placeholders"
→ Run `validate_report.py` to find them
→ Manually fill missing {{variables}}

### "Script not found"
→ Ensure scripts are in `scripts/` directory
→ Make scripts executable: `chmod +x scripts/*.py`

---

## Support

For questions or issues:
1. Check `scripts/README.md` for detailed script documentation
2. Review example outputs in `/references/`
3. Contact your account manager

---

## Version History

**v3.1.0** (Current)
- Updated for standardized folder structure
- Added 5 automation scripts
- Improved validation and quality checks
- Added CLIENT_PROFILE and SOCIAL_STRATEGY templates

**v3.0.0**
- Initial packaged version
- Core audit methodology
- Report template

---

## License

Proprietary - Sidekick Marketer internal use only.

---

*Built for Sidekick Marketer by Claude*
*Last Updated: November 2024*
