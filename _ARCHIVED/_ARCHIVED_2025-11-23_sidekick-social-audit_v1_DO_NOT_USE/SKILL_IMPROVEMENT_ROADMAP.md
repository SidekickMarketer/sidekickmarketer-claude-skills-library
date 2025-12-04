# Sidekick Social Audit Skill - Improvement Roadmap

**Date:** November 22, 2025
**Based on:** CMA (Cincinnati Music Academy) debugging case study
**Skill Location:** `/Users/kylenaughtrip/.claude/skills/sidekick-social-audit/`

---

## Executive Summary

The CMA social audit revealed critical compatibility issues with Meta Business Suite CSV exports that caused the official `parse_social_data.py` script to fail silently, returning "0 posts parsed" despite 106 valid posts in 24 CSV files.

**Impact:**
- 100% data loss for CMA client
- Required custom parser development
- Delayed audit delivery
- Reduced confidence in skill reliability

**Root Causes:**
1. Date column naming assumptions too rigid
2. No handling of GBP aggregate data format
3. Silent failures without error reporting
4. No fallback mechanisms

**Recommended Priority:**
🔴 **HIGH** - Fix date parsing (affects all Meta exports)
🟡 **MEDIUM** - Add GBP format support (affects 26-35% of SOW)
🟢 **LOW** - Enhanced error reporting (quality of life)

---

## Critical Fixes (HIGH Priority)

### Fix #1: Flexible Date Column Detection

**Current Behavior:**
```python
# Line 157 in parse_social_data.py
date_fields = ['date', 'posted date', 'publish date', 'created', 'timestamp', 'posted']
```

**Problem:**
- Meta exports use "Publish time" column
- "Date" column exists but contains "Lifetime" (not a date)
- Script checks "date" first, finds "Lifetime", fails to parse, skips post

**Recommended Fix:**
```python
# Prioritize columns more likely to contain actual timestamps
date_fields = [
    'publish time',      # Meta Business Suite primary field
    'publish date',      # Alternative naming
    'posted date',       # Facebook variation
    'created',           # Generic timestamp
    'created time',      # Variation
    'timestamp',         # Generic
    'posted',            # Short form
    'date'               # Fallback (may contain non-date values)
]
```

**Testing:**
- Verify with CMA CSV files (contains "Publish time")
- Test with standard exports (contains "Date" with actual dates)
- Validate backward compatibility

**Impact:**
- Fixes 106 posts not being parsed in CMA case
- Improves compatibility with all Meta exports
- No breaking changes for existing clients

---

### Fix #2: Make Date Parsing Optional

**Current Behavior:**
```python
# Line 76 in parse_social_data.py
date = self._extract_date(row)
if not date:
    return None  # Skips entire post
```

**Problem:**
- One missing/unparseable date kills entire post analysis
- Loses all engagement metrics even when available
- Too strict for audit purposes (engagement data more critical than dates)

**Recommended Fix:**
```python
date = self._extract_date(row)
if not date:
    # Try to extract from filename as fallback
    date = self._extract_date_from_filename(file_path)

if not date:
    # Use month/year from file path if available
    date = self._extract_period_from_path(file_path)

# If still no date, use 'Unknown' but DON'T skip the post
if not date:
    date = 'Unknown'
    self.logger.warning(f"No date found for row, using 'Unknown': {row.get('Description', '')[:50]}")

# Continue processing with engagement data
```

**Add Helper Method:**
```python
def _extract_date_from_filename(self, file_path: str) -> Optional[str]:
    """Extract date from filename patterns like 2025-01_CMA_IG-Insights.csv"""
    import re
    filename = os.path.basename(file_path)

    # Pattern: YYYY-MM_
    match = re.search(r'(\d{4})-(\d{2})', filename)
    if match:
        year, month = match.groups()
        return f"{year}-{month}-01"  # Use first of month

    return None
```

**Impact:**
- Posts with metrics but no date still get analyzed
- Date becomes informational, not critical
- Maintains audit value even with incomplete data

---

### Fix #3: Enhanced Date Parsing Flexibility

**Current Behavior:**
```python
# Line 189 in parse_social_data.py
def _parse_date(self, date_str: str) -> Optional[str]:
    """Parse date string into standardized format"""

    formats = [
        '%Y-%m-%d',
        '%m/%d/%Y',
        '%d/%m/%Y',
        '%Y-%m-%d %H:%M:%S',
        '%m/%d/%Y %H:%M:%S'
    ]
```

**Problem:**
- Doesn't include Meta's format: "03/25/2025 22:00" (space separator, no seconds)
- Fails on valid dates due to missing format

**Recommended Fix:**
```python
def _parse_date(self, date_str: str) -> Optional[str]:
    """Parse date string into standardized format"""

    if not date_str or not isinstance(date_str, str):
        return None

    # Check for non-date values
    non_date_values = ['lifetime', 'n/a', 'null', 'none', '']
    if date_str.lower().strip() in non_date_values:
        return None

    formats = [
        '%Y-%m-%d',
        '%m/%d/%Y',
        '%d/%m/%Y',
        '%Y-%m-%d %H:%M:%S',
        '%m/%d/%Y %H:%M:%S',
        '%m/%d/%Y %H:%M',        # Meta format (no seconds)
        '%d/%m/%Y %H:%M',        # European variant
        '%Y-%m-%d %H:%M',        # ISO without seconds
        '%Y/%m/%d %H:%M:%S',     # Alternative separator
        '%Y/%m/%d %H:%M'         # Alternative separator, no seconds
    ]

    for fmt in formats:
        try:
            dt = datetime.strptime(date_str.strip(), fmt)
            return dt.strftime('%Y-%m-%d')
        except ValueError:
            continue

    # Log unrecognized format for debugging
    self.logger.debug(f"Unrecognized date format: '{date_str}'")
    return None
```

**Impact:**
- Handles Meta's "03/25/2025 22:00" format
- Rejects "Lifetime" early (performance improvement)
- Better debugging with logged failures

---

## Important Enhancements (MEDIUM Priority)

### Fix #4: GBP Aggregate Data Support

**Current Behavior:**
- Crashes on GBP CSV files with ValueError
- Tries to parse description row as numeric data

**Problem:**
GBP exports have different structure:
```csv
Calls,Messages,Bookings
Number of interactions with the call button...,Number of conversations...,Number of bookings...
27,0,0
```

**Recommended Fix:**
```python
def _is_description_row(self, row: Dict[str, str]) -> bool:
    """
    Detect if row contains column descriptions instead of data.
    Common in GBP aggregate exports.
    """
    description_indicators = [
        'number of',
        'total',
        'count of',
        'interactions with',
        'times your',
        'how many'
    ]

    # Combine all row values into one string
    values = ' '.join(str(v).lower() for v in row.values() if v)

    # If 2+ indicators present, likely a description row
    matches = sum(1 for indicator in description_indicators if indicator in values)
    return matches >= 2

def _parse_post(self, row: Dict[str, str], file_path: str) -> Optional[Dict]:
    """Parse a single post from CSV row"""

    # Skip description rows (common in GBP exports)
    if self._is_description_row(row):
        self.logger.debug("Skipping description row")
        return None

    # Continue with normal parsing...
```

**Alternative: Separate GBP Handler**
```python
def _is_gbp_aggregate_format(self, file_path: str, first_rows: List[Dict]) -> bool:
    """Detect if CSV is GBP aggregate data (not post-level)"""
    if len(first_rows) < 2:
        return False

    # Check if row 2 looks like descriptions
    second_row = first_rows[1]
    if self._is_description_row(second_row):
        return True

    return False

def _parse_gbp_aggregate(self, file_path: str) -> Dict:
    """Parse GBP aggregate account metrics"""
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

        # Skip description row
        data_row = rows[1] if len(rows) > 1 else rows[0]

        return {
            'type': 'gbp_aggregate',
            'calls': int(data_row.get('Calls', 0) or 0),
            'messages': int(data_row.get('Messages', 0) or 0),
            'bookings': int(data_row.get('Bookings', 0) or 0),
            'direction_requests': int(data_row.get('Direction requests', 0) or 0),
            'website_clicks': int(data_row.get('Website clicks', 0) or 0)
        }
```

**Impact:**
- GBP CSV files no longer crash
- Can extract account-level metrics for qualitative analysis
- Proper handling of 26-35% of social posting effort

---

### Fix #5: Enhanced Error Reporting

**Current Behavior:**
- Silent failures
- Returns "0 posts parsed" with no explanation
- No visibility into what went wrong

**Recommended Fix:**
```python
class SocialDataParser:
    def __init__(self):
        self.stats = {
            'files_processed': 0,
            'files_failed': 0,
            'posts_parsed': 0,
            'posts_skipped': 0,
            'skip_reasons': defaultdict(int),
            'errors': []
        }

    def _parse_post(self, row: Dict[str, str], file_path: str) -> Optional[Dict]:
        """Parse a single post from CSV row"""

        # Track reason for skipping
        date = self._extract_date(row)
        if not date:
            self.stats['posts_skipped'] += 1
            self.stats['skip_reasons']['no_date'] += 1
            self.logger.debug(f"Skipped post - no date. Columns: {list(row.keys())}")
            return None

        # ... rest of parsing

    def generate_report(self) -> str:
        """Generate parsing statistics report"""
        report = []
        report.append(f"\n{'='*60}")
        report.append("PARSING STATISTICS")
        report.append(f"{'='*60}")
        report.append(f"Files processed: {self.stats['files_processed']}")
        report.append(f"Files failed: {self.stats['files_failed']}")
        report.append(f"Posts successfully parsed: {self.stats['posts_parsed']}")
        report.append(f"Posts skipped: {self.stats['posts_skipped']}")

        if self.stats['skip_reasons']:
            report.append(f"\nSkip Reasons:")
            for reason, count in self.stats['skip_reasons'].items():
                report.append(f"  - {reason}: {count}")

        if self.stats['errors']:
            report.append(f"\nErrors:")
            for error in self.stats['errors'][:10]:  # Show first 10
                report.append(f"  - {error}")

        return '\n'.join(report)
```

**Impact:**
- Clear visibility into parsing success/failure
- Easier debugging for future clients
- Identifies data quality issues early

---

## Future Enhancements (LOW Priority)

### Enhancement #1: Excel File Support

**Problem:**
- Jun-Oct 2025 CMA data only available in Excel format
- openpyxl library required but installation failed
- Missing 5 months of recent data

**Recommended Approach:**
```python
def _parse_excel_file(self, file_path: str) -> List[Dict]:
    """Parse Excel file if openpyxl available"""
    try:
        import openpyxl
    except ImportError:
        self.logger.warning("openpyxl not installed, skipping Excel file")
        return []

    workbook = openpyxl.load_workbook(file_path, read_only=True)
    sheet = workbook.active

    # Convert to dict format similar to CSV
    headers = [cell.value for cell in sheet[1]]
    posts = []

    for row in sheet.iter_rows(min_row=2, values_only=True):
        post_dict = dict(zip(headers, row))
        posts.append(post_dict)

    return posts
```

**Impact:**
- Expands data coverage significantly
- Handles clients who only export to Excel
- Optional dependency (degrades gracefully)

---

### Enhancement #2: PDF Report Parsing

**Problem:**
- Some clients have data only in PDF format
- Currently no way to extract metrics

**Recommended Approach:**
- Use PyPDF2 or pdfplumber for text extraction
- Regex patterns to extract metrics
- Lower confidence but better than nothing

**Impact:**
- Last-resort data extraction
- Better coverage for historical data

---

### Enhancement #3: Platform Auto-Detection

**Current Behavior:**
- Platform determined from filename ("IG" or "FB")
- Brittle if naming changes

**Recommended Fix:**
```python
def _detect_platform(self, row: Dict[str, str], file_path: str) -> str:
    """Auto-detect platform from column names and content"""

    columns_lower = [col.lower() for col in row.keys()]

    # Instagram indicators
    if 'saves' in columns_lower or 'reel plays' in columns_lower:
        return 'Instagram'

    # Facebook indicators
    if 'reactions' in columns_lower and 'shares' in columns_lower:
        return 'Facebook'

    # GBP indicators
    if 'calls' in columns_lower or 'direction requests' in columns_lower:
        return 'Google Business Profile'

    # Fallback to filename
    filename = os.path.basename(file_path).lower()
    if 'ig' in filename or 'instagram' in filename:
        return 'Instagram'
    elif 'fb' in filename or 'facebook' in filename:
        return 'Facebook'
    elif 'gbp' in filename or 'google' in filename:
        return 'Google Business Profile'

    return 'Unknown'
```

**Impact:**
- More robust platform detection
- Works even with renamed files
- Better error messages

---

## Implementation Plan

### Phase 1: Critical Fixes (Week 1)
**Priority:** Fix CMA-blocking issues
1. ✅ Fix #1: Flexible date column detection
2. ✅ Fix #2: Make date parsing optional
3. ✅ Fix #3: Enhanced date format support

**Testing:**
- Re-run on CMA CSV files (should parse 106 posts)
- Validate with other clients
- Ensure backward compatibility

**Success Criteria:**
- CMA files parse successfully
- No regressions on existing clients
- Clear error messages on failures

---

### Phase 2: GBP Support (Week 2)
**Priority:** Handle aggregate data formats
1. ✅ Fix #4: GBP description row detection
2. ✅ Fix #4 (alt): Separate GBP aggregate handler
3. 🔄 Fix #5: Enhanced error reporting

**Testing:**
- Parse CMA GBP CSV files
- Extract account-level metrics
- Validate against Meta UI

**Success Criteria:**
- GBP files don't crash
- Aggregate metrics extracted correctly
- Posts vs aggregate clearly differentiated

---

### Phase 3: Quality of Life (Week 3)
**Priority:** Better developer/user experience
1. 🔄 Fix #5: Complete error reporting system
2. 🔄 Enhancement #3: Platform auto-detection
3. 📝 Documentation updates

**Testing:**
- Test with intentionally broken data
- Verify error messages are helpful
- Update README with new capabilities

**Success Criteria:**
- Parsing report shows clear statistics
- Errors are actionable
- Documentation covers new features

---

### Phase 4: Advanced Features (Future)
**Priority:** Nice-to-have expansions
1. ⏳ Enhancement #1: Excel file support
2. ⏳ Enhancement #2: PDF parsing
3. ⏳ Multi-format reporting

**Dependencies:**
- openpyxl installation resolution
- PDF library selection
- Client demand validation

---

## Testing Strategy

### Test Suite Requirements

**Test Case 1: Standard Meta Export**
- File: Contains "Date" column with actual dates
- Expected: All posts parsed successfully
- Validates: Backward compatibility

**Test Case 2: CMA-Style Export**
- File: Contains "Date" = "Lifetime", "Publish time" = actual dates
- Expected: All posts parsed using Publish time
- Validates: Fix #1, Fix #2, Fix #3

**Test Case 3: GBP Aggregate Data**
- File: Contains description row with text like "Number of interactions..."
- Expected: Skips description row, parses data row as aggregate metrics
- Validates: Fix #4

**Test Case 4: Missing Dates**
- File: No date columns at all
- Expected: Extracts date from filename, still parses engagement metrics
- Validates: Fix #2 fallback mechanism

**Test Case 5: Mixed Formats**
- Multiple files with different date formats
- Expected: All parsed correctly, statistics show success/skip rates
- Validates: Fix #5 error reporting

---

## Rollout Plan

### Step 1: Create Test Branch
```bash
cd /Users/kylenaughtrip/.claude/skills/sidekick-social-audit
git checkout -b feature/flexible-date-parsing
```

### Step 2: Implement Critical Fixes
- Update parse_social_data.py with Fix #1, #2, #3
- Add test cases
- Run on CMA data

### Step 3: Validate Changes
```bash
# Test with CMA data
python scripts/parse_social_data.py \
  --input "/path/to/cma/07_Social_Media/02_Performance_Data/" \
  --output "/tmp/test_output.json"

# Should now show:
# ✅ Files processed: 24
# ✅ Posts parsed: 106
# ✅ Instagram: 52
# ✅ Facebook: 54
```

### Step 4: Merge and Deploy
```bash
git add scripts/parse_social_data.py
git commit -m "feat: flexible date parsing for Meta exports

- Add 'publish time' to date field priority
- Make date parsing optional with fallback
- Support Meta's 'm/d/Y H:M' format
- Fixes CMA parsing failure (106 posts recovered)

Resolves: #CMA-001"

git push origin feature/flexible-date-parsing
# Create PR for review
```

---

## Success Metrics

### Before Improvements:
- CMA posts parsed: **0 / 106 (0%)**
- GBP files processed: **0 / 9 (0%)**
- Error visibility: **None** (silent failure)
- Client confidence: **Low** (custom script needed)

### After Phase 1:
- CMA posts parsed: **106 / 106 (100%)** ✅
- Date formats supported: **10+** (vs 5)
- Backward compatibility: **Maintained**
- Client confidence: **High**

### After Phase 2:
- GBP files processed: **9 / 9 (100%)** ✅
- Aggregate metrics extracted: **5+**
- Crash rate: **0%** (vs 100%)

### After Phase 3:
- Error clarity: **10/10** (detailed reports)
- Debug time: **< 5 min** (vs 2+ hours)
- Platform detection accuracy: **100%**

---

## Lessons Learned

### What Worked Well:
1. ✅ Custom parser proved concepts quickly
2. ✅ Detailed debugging revealed exact issues
3. ✅ Test-driven approach with real client data
4. ✅ Comprehensive documentation for handoff

### What Could Be Better:
1. ⚠️ Official script should have better error messages
2. ⚠️ Date parsing too fragile for real-world exports
3. ⚠️ No test suite for CSV format variations
4. ⚠️ Silent failures hide issues from users

### Recommendations for Future Skills:
1. 📝 Include validation mode that reports issues without failing
2. 📝 Test with multiple real client exports before launch
3. 📝 Make dependencies optional with graceful degradation
4. 📝 Provide example data for testing
5. 📝 Document expected CSV column names explicitly

---

## References

### Related Documents:
- `debugging/README.md` - Overview of debugging process
- `debugging/2025-11_Official_Script_Failure_Analysis.md` - Detailed technical breakdown
- `debugging/working_parser_cma.py` - Proven working alternative
- `debugging/comprehensive_parser_cma.py` - Advanced discovery parser

### Client Reports:
- CMA 2025-11_CMA_Social_Audit.md (qualitative analysis)
- CMA 2025-11_CMA_Quantitative_Performance_Analysis.md (hard data)
- CMA 2025-11_Complete_Analysis_Summary.md (final accounting)

### Official Skill Files:
- `/Users/kylenaughtrip/.claude/skills/sidekick-social-audit/scripts/parse_social_data.py`
- `/Users/kylenaughtrip/.claude/skills/sidekick-social-audit/scripts/calculate_engagement.py`
- `/Users/kylenaughtrip/.claude/skills/sidekick-social-audit/references/social_audit_matrix.md`

---

**Document Status:** COMPLETE
**Next Action:** Implement Phase 1 critical fixes
**Owner:** Kyle @ Sidekick Marketer
**Last Updated:** November 22, 2025
