# Sidekick Social Audit Scripts

This directory contains Python scripts that support the social audit skill.

## Scripts Overview

### 1. `setup_client_folder.py`
**Purpose:** Automate creation of standardized client folder structure

**Usage:**
```bash
python setup_client_folder.py \
  --client-name "Cincinnati Music Academy" \
  --output-dir ./clients \
  --short-code cma
```

**What it does:**
- Creates all numbered folders (01-90)
- Generates CLIENT_PROFILE.md from template
- Generates SOCIAL_STRATEGY.md from template  
- Creates README files in key directories
- Creates START_HERE.md with onboarding checklist

**When to use:** When onboarding a new client

---

### 2. `validate_folder_structure.py`
**Purpose:** Check if client folder meets audit requirements

**Usage:**
```bash
python validate_folder_structure.py --path ./client-cma --verbose
```

**What it does:**
- Verifies required folders exist
- Checks for CLIENT_PROFILE.md
- Checks for SOCIAL_STRATEGY.md
- Inventories content calendars and analytics files
- Reports missing or misconfigured elements

**When to use:** Before running social audit skill

---

### 3. `parse_social_data.py`
**Purpose:** Parse analytics CSVs into unified JSON format

**Usage:**
```bash
# Parse specific files
python parse_social_data.py \
  --analytics path/to/Instagram_Analytics.csv \
  --output data.json

# Auto-discover files in directory
python parse_social_data.py \
  --search-dir ./client-cma/07_Social_Media/02_Performance_Data/ \
  --output data.json
```

**What it does:**
- Reads CSV/XLSX analytics files
- Normalizes different export formats
- Detects platform (Instagram, Facebook, GBP)
- Extracts engagement metrics
- Outputs unified JSON structure

**When to use:** To preprocess analytics data for faster audit analysis

**Note:** XLSX support requires `openpyxl`: `pip install openpyxl`

---

### 4. `calculate_engagement.py`
**Purpose:** Calculate standardized engagement rates across platforms

**Usage:**
```bash
# Calculate single post
python calculate_engagement.py \
  --platform instagram \
  --likes 150 \
  --comments 12 \
  --saves 45 \
  --reach 2000

# Enrich JSON file
python calculate_engagement.py \
  --json-file data.json \
  --output enriched.json

# Print formula guide
python calculate_engagement.py --formulas
```

**What it does:**
- Applies platform-specific engagement formulas
- Classifies rates (excellent/good/average/poor)
- Enriches JSON files with calculated rates
- Provides industry benchmarks

**When to use:** To ensure consistent engagement calculations

---

### 5. `validate_report.py`
**Purpose:** Check completed audit reports for quality issues

**Usage:**
```bash
python validate_report.py --report path/to/2024-11_Social_Audit.md

# Strict mode (warnings become errors)
python validate_report.py --report audit.md --strict
```

**What it does:**
- Finds unfilled {{placeholders}}
- Checks for required sections
- Detects vague language ("many", "several")
- Finds TODO markers
- Validates table formatting
- Checks for broken links

**When to use:** Before delivering report to client

---

## Installation

### Basic (Core scripts)
No additional dependencies required - uses Python standard library only.

### Full Feature Set
For PDF parsing and XLSX support:

```bash
pip install openpyxl PyPDF2 pytesseract
```

---

## Typical Workflow

### New Client Setup
```bash
# 1. Create folder structure
python scripts/setup_client_folder.py \
  --client-name "New Client LLC" \
  --output-dir ~/clients \
  --short-code newclient

# 2. Fill in CLIENT_PROFILE.md and SOCIAL_STRATEGY.md
# (Manual step)

# 3. Import historical data
# (Manual step - upload calendars/analytics)

# 4. Validate setup
python scripts/validate_folder_structure.py --path ~/clients/client-newclient
```

### Running Audit
```bash
# 1. Optional: Preprocess analytics
python scripts/parse_social_data.py \
  --search-dir ~/clients/client-cma/07_Social_Media/02_Performance_Data/ \
  --output ~/temp/cma-data.json

# 2. Optional: Calculate engagement rates
python scripts/calculate_engagement.py \
  --json-file ~/temp/cma-data.json \
  --output ~/temp/cma-data-enriched.json

# 3. Run social audit skill in Claude
# (Provide folder path/URL)

# 4. Validate completed report
python scripts/validate_report.py \
  --report ~/clients/client-cma/07_Social_Media/04_Audit_Reports/2024-11_Social_Audit.md
```

---

## Tips

### File Naming Conventions
Scripts expect these formats:
- Content calendars: `YYYY-MM_Content_Calendar.csv`
- Analytics: `Platform_Analytics_YYYY_Q#.csv` or `Platform_Analytics_YYYY-MM.csv`
- Post archives: `YYYY-MM_Platform_Posts.pdf`

### Debugging
All scripts support `--help` flag:
```bash
python scripts/setup_client_folder.py --help
```

### JSON Output
Most validation scripts support `--json` for programmatic use:
```bash
python scripts/validate_folder_structure.py --path ./client --json
```

---

## Future Enhancements

Potential additions:
- `detect_seasonality.py` - Statistical pattern detection
- `generate_charts.py` - Auto-generate performance charts
- `classify_post_format.py` - Auto-categorize post formats
- `extract_posts_from_pdf.py` - Full PDF OCR extraction

---

*For issues or questions, contact your account manager.*
