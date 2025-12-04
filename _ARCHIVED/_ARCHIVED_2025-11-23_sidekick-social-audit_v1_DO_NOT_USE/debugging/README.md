# Sidekick Social Audit - CMA Debugging Documentation

**Date:** November 22, 2025
**Client:** Cincinnati Music Academy (CMA)
**Issue:** Official skill script failed to parse CMA's social media CSV files

---

## Overview

This folder contains debugging documentation and working alternative parsers created when the official `parse_social_data.py` script failed to parse CMA's social media data exports from Meta Business Suite.

## What Happened

**Expected Behavior:**
- Official script should parse Instagram/Facebook CSV exports
- Extract engagement metrics (likes, comments, shares, reach)
- Generate performance analysis

**Actual Behavior:**
- Script returned "0 posts parsed" despite 24 valid CSV files
- All GBP CSV files crashed with ValueError

## Root Causes

### Issue #1: Date Column Mismatch

**Official Script Assumption:**
- Looks for dates in column named "Date"
- Script: `date_fields = ['date', 'posted date', 'publish date', ...]`

**CMA's CSV Reality:**
- "Date" column contains "Lifetime" (not a date)
- Actual dates in "Publish time" column: "03/25/2025 22:00"

**Result:**
- Script tries to parse "Lifetime" as date → fails
- Returns None → entire post skipped
- 106 posts missed

**Code Location:**
- File: `/Users/kylenaughtrip/.claude/skills/sidekick-social-audit/scripts/parse_social_data.py`
- Lines: 154-168 (_extract_date method)

### Issue #2: GBP CSV Format Incompatibility

**Official Script Assumption:**
- CSV files contain post-level data (one row per post)

**CMA's GBP CSV Reality:**
- Row 1: Column headers
- Row 2: Column descriptions (long text strings)
- Row 3: Aggregate account metrics (total calls, clicks, etc.)

**Result:**
- Script tries to convert "Number of interactions with the call button..." to int
- ValueError crash
- 0 GBP posts analyzed

---

## Files in This Folder

### 1. `2025-11_Official_Script_Failure_Analysis.md`

**Purpose:** Detailed technical breakdown for sharing with skill developer

**Contains:**
- Line-by-line code analysis
- Step-by-step failure trace (11 steps)
- 4 specific fixes needed
- Test cases
- Email template

**When to use:** Share with developer to fix official script

### 2. `working_parser_cma.py`

**Purpose:** Simple working parser that successfully analyzed 106 posts

**How it works:**
- Hardcoded list of known CSV files
- Uses filename for month context (not date parsing)
- Platform detection from filename (IG/FB)
- Extracts metrics directly from known columns
- Calculates engagement rates

**Metrics extracted:**
- Instagram: likes, comments, shares, saves, reach
- Facebook: reactions, comments, shares, reach
- Engagement rate: (total engagement / reach) × 100

**Output:**
- Hall of Fame: Top 15 posts by total engagement
- Format performance: Carousel vs Single Image vs Reel
- Month-over-month trends

**Run command:**
```bash
python3 /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My\ Drive/01_Sidekick\ Marketer/3.\ AI_Automation/01_Claude_Skills/skills/sidekick-social-audit/debugging/working_parser_cma.py
```

### 3. `comprehensive_parser_cma.py`

**Purpose:** Advanced parser using glob to find ALL CSV files recursively

**How it works:**
- Pattern 1: `07_Social_Media/02_Performance_Data/**/*Insights.csv`
- Pattern 2: `05_Reports_Analytics/**/*Insights*.csv`
- Automatically discovers all CSV files
- Handles Instagram, Facebook, and GBP formats
- GBP support (clicks, calls, impressions)

**Advantages over working_parser:**
- No hardcoded file list
- Finds files in any subfolder
- Handles GBP data (with different metrics)
- Saves JSON output: `/tmp/cma_complete_data.json`

**Run command:**
```bash
python3 /Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My\ Drive/01_Sidekick\ Marketer/3.\ AI_Automation/01_Claude_Skills/skills/sidekick-social-audit/debugging/comprehensive_parser_cma.py
```

**Output:**
- Terminal: Summary statistics
- JSON file: `/tmp/cma_complete_data.json` (full dataset)

---

## Results Achieved

### Data Successfully Parsed:
- **106 total posts** (52 Instagram, 54 Facebook, 0 GBP)
- **5 months** of data (Jan-May 2025)
- **15 CSV files** successfully processed
- **9 GBP CSV files** skipped (incompatible format)

### Key Findings:
- Instagram 3× better than Facebook (13.8% vs 4.5% engagement)
- Carousels 18% better than single images (16.3% vs 13.8%)
- Testimonials best content type (22.5% engagement)
- Promotional content underperforms by 51%

### Reports Generated:
1. **2025-11_CMA_Social_Audit.md** (23KB) - Qualitative strategic analysis
2. **2025-11_CMA_Quantitative_Performance_Analysis.md** (15KB) - Hard data
3. **2025-11_Data_Inventory_and_Analysis_Coverage.md** - Transparency report
4. **2025-11_Complete_Analysis_Summary.md** - Final accounting

---

## How to Use This for Other Clients

### If Official Script Works:
✅ Use official script - it's more comprehensive and maintained

### If Official Script Returns "0 posts parsed":
1. Check CSV "Date" column - does it contain actual dates?
2. If not, check for "Publish time" or similar column
3. Use `working_parser_cma.py` as template
4. Update file paths and column names for new client

### For Comprehensive Discovery:
1. Use `comprehensive_parser_cma.py` as template
2. Update `base_path` to new client folder
3. Update glob patterns if needed
4. Run to discover all CSV files automatically

---

## Recommendations for Skill Improvement

### Fix #1: Expand Date Field Priority
```python
# Current:
date_fields = ['date', 'posted date', 'publish date', 'created', 'timestamp', 'posted']

# Recommended:
date_fields = ['publish time', 'publish date', 'posted date', 'created', 'timestamp', 'posted', 'date']
#             ^^^^^^^^^^^^^^ Add and prioritize
```

### Fix #2: Add Description Row Detection (GBP)
```python
def _is_description_row(self, row: Dict[str, str]) -> bool:
    """Detect if row contains column descriptions instead of data"""
    description_indicators = ['number of', 'total', 'count of', 'interactions with']
    values = ' '.join(str(v).lower() for v in row.values() if v)
    matches = sum(1 for indicator in description_indicators if indicator in values)
    return matches >= 2
```

### Fix #3: Make Date Parsing Optional
```python
# Current: Skips post if no date
if not date:
    return None

# Recommended: Use filename/path for context
if not date:
    date = self._extract_date_from_filename(file_path)
```

### Fix #4: Add Verbose Error Reporting
```python
# Add debug logging:
if not parsed_date:
    self.logger.debug(f"Failed to parse date '{date_str}' in row {row_num}")
    self.logger.debug(f"Available columns: {list(row.keys())}")
```

---

## Contact & Support

**Created by:** Claude @ Sidekick Marketer
**Client:** Cincinnati Music Academy
**Date:** November 22, 2025

**For questions or improvements:**
- Reference CMA debugging case study
- Use working parsers as templates
- See failure analysis for detailed technical breakdown

---

## Quick Reference

**Official Script Location:**
```
/Users/kylenaughtrip/.claude/skills/sidekick-social-audit/scripts/parse_social_data.py
```

**Custom Parsers Location:**
```
/Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/3. AI_Automation/01_Claude_Skills/skills/sidekick-social-audit/debugging/
```

**Test Data:**
```
/Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/2. Clients/01_Clients/client-cma/07_Social_Media/02_Performance_Data/
```

**JSON Output:**
```
/tmp/cma_complete_data.json
```
