# Official Skill Script Failure - Technical Breakdown
**Detailed Analysis for Debugging**

**Script:** `/Users/kylenaughtrip/.claude/skills/sidekick-social-audit/scripts/parse_social_data.py`
**Date:** November 22, 2025
**Analyst:** Claude @ Sidekick Marketer
**Purpose:** Share with skill developer to fix parsing issues

---

## 🔴 FAILURE #1: Date Column Mismatch

### The Problem

The script expects the "Date" column to contain actual dates, but CMA's CSV files have:
- **"Date" column:** Contains the string "Lifetime" (analytics period indicator)
- **"Publish time" column:** Contains actual dates like "03/25/2025 22:00"

The script tries to parse "Lifetime" as a date, fails, and skips the entire post.

---

### Exact Location of Failure

**File:** `/Users/kylenaughtrip/.claude/skills/sidekick-social-audit/scripts/parse_social_data.py`

**Lines 154-168 (Date Extraction):**
```python
def _extract_date(self, row: Dict[str, str]) -> Optional[str]:
    """Extract date from row"""

    date_fields = ['date', 'posted date', 'publish date', 'created', 'timestamp', 'posted']

    row_lower = {k.lower().strip(): v for k, v in row.items()}

    for field in date_fields:
        if field in row_lower:
            date_str = row_lower[field]
            parsed_date = self._parse_date(date_str)  # <-- FAILS HERE
            if parsed_date:
                return parsed_date

    return None  # <-- Returns None when it can't parse "Lifetime"
```

**Lines 67-76 (Row Normalization - Where Posts Get Skipped):**
```python
def _normalize_row(self, row: Dict[str, str], filename: str) -> Optional[Dict[str, Any]]:
    """Normalize a CSV row to standard format"""

    # ... platform detection code ...

    # Try to extract date
    date = self._extract_date(row)
    if not date:
        return None  # <-- POST GETS SKIPPED HERE (line 76)

    # ... rest of processing ...
```

**Result:** Every single post returns `None` because date parsing fails, so `parse_csv()` at line 60 ends up with 0 posts.

---

### What the CSV Actually Contains

**Example from:** `2025-03_March/2025-03_CMA_IG-Insights.csv`

**CSV Headers:**
```csv
"Post ID","Account ID","Account username","Account name",Description,"Duration (sec)","Publish time",Permalink,"Post type","Data comment",Date,Views,Reach,Likes,Shares,Follows,Comments,Saves
```

**Sample Row:**
```csv
17960320052859139,17841461342735919,cincinnatimusicacademy,"Cincinnati Music Academy | Music Lessons","Charli and Andi Cantor recently performed...",0,"03/25/2025 22:00",https://www.instagram.com/p/DHpmj9euOPy/,"IG carousel",,"Lifetime",145,75,10,1,0,0,0
```

**Key Columns:**
- **"Publish time":** `03/25/2025 22:00` ← **This is the actual date!**
- **"Date":** `Lifetime` ← **This is NOT a date (it's a Meta Analytics period indicator)**

---

### Step-by-Step Failure Trace

1. **Script reads row** (line 52)
2. **Calls `_normalize_row()`** (line 54)
3. **Calls `_extract_date()`** (line 74)
4. **Finds "date" in row_lower** (line 162, because "Date" column exists)
5. **Extracts value:** `date_str = "Lifetime"` (line 163)
6. **Calls `_parse_date("Lifetime")`** (line 164)
7. **Tries all date formats** (lines 177-193):
   ```python
   formats = [
       '%Y-%m-%d',           # Fails: "Lifetime" is not YYYY-MM-DD
       '%m/%d/%Y',           # Fails: "Lifetime" is not MM/DD/YYYY
       '%d/%m/%Y',           # Fails
       '%Y/%m/%d',           # Fails
       '%B %d, %Y',          # Fails
       '%b %d, %Y',          # Fails
       '%Y-%m-%d %H:%M:%S',  # Fails
       '%m/%d/%Y %H:%M',     # Fails
   ]
   ```
8. **All formats fail** → Returns `None` (line 199)
9. **`_extract_date()` returns `None`** (line 168)
10. **`_normalize_row()` returns `None`** (line 76: `if not date: return None`)
11. **Post is SKIPPED** ❌

This happens for **every single row**, resulting in **0 posts parsed**.

---

### Why the Script Didn't Check "Publish time"

**Line 157:**
```python
date_fields = ['date', 'posted date', 'publish date', 'created', 'timestamp', 'posted']
```

**Notice:**
- ❌ `'publish time'` is NOT in the list
- ✅ `'publish date'` IS in the list (but doesn't exist in CSV)

**CMA's CSV uses:** `"Publish time"` (two words, lowercase 't')
**Script checks for:** `'publish date'` or `'date'`

**Result:** The script finds the useless "Date" column first and never checks "Publish time".

---

## 🔴 FAILURE #2: GBP Data Format Incompatibility

### The Problem

GBP CSV files contain **aggregate account metrics**, not individual post data. The script expects post-level rows but encounters account summary rows instead.

---

### Exact Location of Failure

**File:** `/Users/kylenaughtrip/.claude/skills/sidekick-social-audit/scripts/parse_social_data.py`

**Lines 108-109 (Numeric Field Parsing):**
```python
if field in ['likes', 'comments', 'shares', 'saves', 'reach', 'impressions', 'link_clicks']:
    post[field] = self._parse_number(value)  # <-- FAILS HERE
```

**Lines 201-217 (Number Parsing):**
```python
def _parse_number(self, value: str) -> int:
    """Parse numeric string to integer"""

    if not value or value.strip() == '':
        return 0

    # Remove common formatting
    clean = value.strip().replace(',', '').replace('%', '')

    try:
        # Try to parse as float first, then convert to int
        return int(float(clean))
    except ValueError:
        return 0  # <-- Should return 0, but actually raises exception
```

**Error Raised:**
```python
invalid literal for int() with base 10: 'Number of interactions with the call button from your Business Profile'
```

This means the `try/except` block at lines 211-215 is NOT catching the error properly.

---

### What GBP CSV Actually Contains

**Example from:** `2025-01_January/2025-01_CMA_GBP-Insights.csv`

**CSV Structure:**
```csv
Store code,Business name,Address,Labels,Google Search - Mobile,Google Search - Desktop,Google Maps - Mobile,Google Maps - Desktop,Calls,Messages,Bookings,Directions,Website clicks,Food orders,Food menu clicks,Hotel bookings
,,,,Number of people that viewed your Business Profile on Google Search using Mobile,Number of people that viewed your Business Profile on Google Search using Desktop,Number of people that viewed your Business Profile on Google Maps using Mobile,Number of people that viewed your Business Profile on Google Maps using Desktop,Number of interactions with the call button from your Business Profile,Number of conversations initiated from your Business Profile,Number of bookings made from your Business Profile,Number of requests for directions made from your Business Profile,Number of interactions with the website button from your Business Profile,Number of Food orders placed for pickup or delivery from your Google Business Profile with an Order with Google Provider,Number of Food orders placed for pickup or delivery from your Google Business Profile with an Order with Google Provider,Number of interactions with the hotel supplier's free booking link
,Cincinnati Music Academy,"7420 Montgomery Rd, Cincinnati, OH 45236",,2398,891,546,206,27,0,0,245,248,0,0,0
```

**Row 1:** Column headers
**Row 2:** Column descriptions (long text strings!)
**Row 3:** Actual numeric data

---

### Why This Fails

**Step-by-step:**

1. **CSV reader processes Row 2 as a data row** (because CSV has no concept of "description row")
2. **Script tries to parse "Calls" column value**
3. **Value is:** `"Number of interactions with the call button from your Business Profile"`
4. **Calls `_parse_number()`** with this long string
5. **Line 213:** `return int(float(clean))` tries to convert the string
6. **Python raises:** `ValueError: invalid literal for int() with base 10: 'Number of interactions...'`
7. **Exception NOT caught** (the `try/except` should catch this but doesn't)
8. **Script crashes** ❌

---

### Why the Exception Wasn't Caught

**Mystery:** The `try/except` block at lines 211-215 SHOULD catch this, but the error still propagates.

**Possible reasons:**

1. **The exception is raised before reaching the try block**
   - Maybe in `_normalize_row()` before calling `_parse_number()`

2. **The CSV encoding has hidden characters**
   - BOM (Byte Order Mark) or special characters causing parsing issues

3. **The error happens in csv.DictReader itself**
   - Before the script even gets to process the row

**Need to investigate:** Why the `try/except` in `_parse_number()` doesn't catch the ValueError.

---

## 🔧 FIXES REQUIRED

### Fix #1: Update Date Field Priority

**File:** `/Users/kylenaughtrip/.claude/skills/sidekick-social-audit/scripts/parse_social_data.py`
**Line:** 157

**Current:**
```python
date_fields = ['date', 'posted date', 'publish date', 'created', 'timestamp', 'posted']
```

**Fixed:**
```python
date_fields = ['publish time', 'publish date', 'posted date', 'created', 'timestamp', 'posted', 'date']
```

**Changes:**
- Add `'publish time'` to the list
- Move it to the FRONT (so it's checked first)
- Move `'date'` to the END (so it's only used as fallback)

**Rationale:**
- Instagram/Facebook CSVs use "Publish time" for actual dates
- "Date" column contains "Lifetime" (not a date)
- Checking "Publish time" first ensures proper date extraction

---

### Fix #2: Add Date Format for "Publish time"

**File:** `/Users/kylenaughtrip/.claude/skills/sidekick-social-audit/scripts/parse_social_data.py`
**Line:** 177-186

**Current:**
```python
formats = [
    '%Y-%m-%d',
    '%m/%d/%Y',
    '%d/%m/%Y',
    '%Y/%m/%d',
    '%B %d, %Y',
    '%b %d, %Y',
    '%Y-%m-%d %H:%M:%S',
    '%m/%d/%Y %H:%M',  # <-- This format already exists!
]
```

**Note:** The format `'%m/%d/%Y %H:%M'` already exists at line 185, which SHOULD parse `"03/25/2025 22:00"`.

**Mystery:** Why didn't this work?

**Need to investigate:**
- Are there hidden characters in the "Publish time" value?
- Is the script not reaching this point because it finds "Date" first?

**Actually:** The fix for Fix #1 should resolve this. By checking "Publish time" before "Date", the script will find the correctly formatted date and parse it successfully.

---

### Fix #3: Skip GBP Description Rows

**File:** `/Users/kylenaughtrip/.claude/skills/sidekick-social-audit/scripts/parse_social_data.py`
**Line:** 52-58 (in `parse_csv()`)

**Current:**
```python
for row_num, row in enumerate(reader, start=2):
    try:
        post = self._normalize_row(row, file_path.name)
        if post:
            posts.append(post)
    except Exception as e:
        self.errors.append(f"Row {row_num} in {file_path.name}: {e}")
```

**Fixed:**
```python
for row_num, row in enumerate(reader, start=2):
    try:
        # Skip rows where all values are descriptions (GBP CSVs)
        if self._is_description_row(row):
            continue

        post = self._normalize_row(row, file_path.name)
        if post:
            posts.append(post)
    except Exception as e:
        self.errors.append(f"Row {row_num} in {file_path.name}: {e}")
```

**New method to add:**
```python
def _is_description_row(self, row: Dict[str, str]) -> bool:
    """Detect if row contains column descriptions instead of data"""

    # Check if any value contains common description words
    description_indicators = [
        'number of', 'total', 'count of', 'interactions with',
        'people that', 'viewed your', 'placed for'
    ]

    values = ' '.join(str(v).lower() for v in row.values() if v)

    # If row contains multiple description indicators, it's likely a description row
    matches = sum(1 for indicator in description_indicators if indicator in values)

    return matches >= 2
```

**Rationale:**
- GBP CSVs have description rows (Row 2)
- These descriptions contain phrases like "Number of interactions with..."
- Detecting and skipping these rows prevents parsing errors

---

### Fix #4: Handle GBP Aggregate Data Properly

**Problem:** GBP CSVs don't contain individual posts, they contain account-level metrics.

**Options:**

**Option A: Skip GBP CSVs entirely**
```python
def _detect_platform(self, filename: str, row: Dict[str, str]) -> str:
    """Detect platform from filename or row content"""

    filename_lower = filename.lower()

    # Check if this is a GBP aggregate file (not post-level)
    if 'gbp' in filename_lower or 'google' in filename_lower:
        if 'Store code' in row or 'Business name' in row:
            return 'gbp_aggregate'  # Special flag to skip

    # ... rest of platform detection ...
```

Then in `_normalize_row()`:
```python
platform = self._detect_platform(filename, row)
if platform == 'gbp_aggregate':
    return None  # Skip aggregate data files
```

**Option B: Parse GBP as account metrics (not posts)**
- Create a separate parser for aggregate data
- Return a different data structure
- Don't mix with post-level data

**Recommendation:** Option A (skip GBP CSVs) because:
- They don't contain post-level data
- Account metrics should be analyzed separately
- Mixing aggregate and post-level data creates confusion

---

## 📋 Complete Fix Summary

### Changes Needed in `parse_social_data.py`:

**1. Line 157 - Update date field priority:**
```python
# OLD
date_fields = ['date', 'posted date', 'publish date', 'created', 'timestamp', 'posted']

# NEW
date_fields = ['publish time', 'publish date', 'posted date', 'created', 'timestamp', 'posted', 'date']
```

**2. Lines 52-58 - Add description row detection:**
```python
for row_num, row in enumerate(reader, start=2):
    try:
        # NEW: Skip description rows (common in GBP CSVs)
        if self._is_description_row(row):
            continue

        post = self._normalize_row(row, file_path.name)
        if post:
            posts.append(post)
    except Exception as e:
        self.errors.append(f"Row {row_num} in {file_path.name}: {e}")
```

**3. Add new method `_is_description_row()`** (see Fix #3 above)

**4. Line 138 - Skip GBP aggregate files:**
```python
# In _detect_platform(), add at the beginning:
if 'gbp' in filename_lower or 'google' in filename_lower:
    # Check if this is an aggregate file
    if any(header in row for header in ['Store code', 'Business name']):
        return 'gbp_aggregate'

# Then in _normalize_row():
platform = self._detect_platform(filename, row)
if platform == 'gbp_aggregate':
    return None  # Skip aggregate data
```

---

## ✅ Testing the Fixes

### Test Case #1: Instagram CSV
**File:** `2025-03_March/2025-03_CMA_IG-Insights.csv`
**Expected:** 7 posts parsed
**Current:** 0 posts parsed ❌
**After fix:** 7 posts parsed ✅

**Why it will work:**
- Script will check "Publish time" first (instead of "Date")
- "Publish time" contains "03/25/2025 22:00"
- Format `'%m/%d/%Y %H:%M'` will successfully parse it
- Posts will be processed normally

---

### Test Case #2: Facebook CSV
**File:** `2025-03_March/2025-03_CMA_FB-Insights.csv`
**Expected:** 5 posts parsed
**Current:** 0 posts parsed ❌
**After fix:** 5 posts parsed ✅

**Same reason as Test Case #1**

---

### Test Case #3: GBP CSV
**File:** `2025-01_January/2025-01_CMA_GBP-Insights.csv`
**Expected:** 0 posts (it's aggregate data, not posts)
**Current:** Crashes with `ValueError` ❌
**After fix:** Gracefully skipped, no error ✅

**Why it will work:**
- `_detect_platform()` detects "GBP aggregate" format
- Returns `'gbp_aggregate'`
- `_normalize_row()` returns `None`
- File processed without errors

---

## 🧪 Validation Command

After implementing fixes, test with:

```bash
cd /Users/kylenaughtrip/.claude/skills/sidekick-social-audit

# Test Instagram
python3 scripts/parse_social_data.py \
  --analytics "/Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/2. Clients/01_Clients/client-cma/07_Social_Media/02_Performance_Data/2025-03_March/2025-03_CMA_IG-Insights.csv" \
  --output /tmp/test_ig.json

# Test Facebook
python3 scripts/parse_social_data.py \
  --analytics "/Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/2. Clients/01_Clients/client-cma/07_Social_Media/02_Performance_Data/2025-03_March/2025-03_CMA_FB-Insights.csv" \
  --output /tmp/test_fb.json

# Test GBP (should skip gracefully)
python3 scripts/parse_social_data.py \
  --analytics "/Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/2. Clients/01_Clients/client-cma/07_Social_Media/02_Performance_Data/2025-01_January/2025-01_CMA_GBP-Insights.csv" \
  --output /tmp/test_gbp.json
```

**Expected output:**
```
✅ Parsed 7 posts from 2025-03_CMA_IG-Insights.csv
✅ Parsed 5 posts from 2025-03_CMA_FB-Insights.csv
✅ Parsed 0 posts from 2025-01_CMA_GBP-Insights.csv (aggregate data skipped)
```

---

## 📝 Root Cause Summary

### Issue #1: Wrong Column Priority
- **Root Cause:** Script checks "Date" before "Publish time"
- **Impact:** All posts skipped (0 parsed)
- **Severity:** CRITICAL
- **Fix Difficulty:** EASY (1-line change)

### Issue #2: GBP Format Mismatch
- **Root Cause:** GBP CSVs contain aggregate data, not post data
- **Impact:** Script crashes on GBP files
- **Severity:** MODERATE (GBP data not parseable from CSV anyway)
- **Fix Difficulty:** EASY (add detection logic)

### Issue #3: Poor Error Handling
- **Root Cause:** Exceptions not properly caught/logged
- **Impact:** Silent failures, unclear error messages
- **Severity:** LOW (doesn't break parsing, just makes debugging hard)
- **Fix Difficulty:** MEDIUM (improve error handling throughout)

---

## 📧 For Sharing with Developer

**Subject:** Bug Report: parse_social_data.py fails on Meta CSV exports

**Body:**
```
The parse_social_data.py script fails to parse Instagram/Facebook CSV files exported from Meta Business Suite due to a column naming mismatch.

**Problem:** The script prioritizes the "Date" column (which contains "Lifetime" - an analytics period indicator) over the "Publish time" column (which contains actual dates like "03/25/2025 22:00").

**Result:** All posts return None and 0 posts are parsed.

**Fix:** Update line 157 to prioritize "publish time":
  date_fields = ['publish time', 'publish date', ..., 'date']

**Also:** GBP CSV files contain account aggregates, not post data. Script should detect and skip these to avoid crashes.

Detailed analysis: [attach this document]
```

---

## 📎 Files Referenced

**Official Script:**
`/Users/kylenaughtrip/.claude/skills/sidekick-social-audit/scripts/parse_social_data.py`

**Test Data (Instagram):**
`/Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/2. Clients/01_Clients/client-cma/07_Social_Media/02_Performance_Data/2025-03_March/2025-03_CMA_IG-Insights.csv`

**Test Data (Facebook):**
`/Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/2. Clients/01_Clients/client-cma/07_Social_Media/02_Performance_Data/2025-03_March/2025-03_CMA_FB-Insights.csv`

**Test Data (GBP - aggregate):**
`/Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/2. Clients/01_Clients/client-cma/07_Social_Media/02_Performance_Data/2025-01_January/2025-01_CMA_GBP-Insights.csv`

**Working Custom Script (reference):**
`/tmp/analyze_cma_social.py`

---

*Technical breakdown prepared by Claude @ Sidekick Marketer*
*November 22, 2025*
