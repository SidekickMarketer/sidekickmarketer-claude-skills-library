#!/usr/bin/env python3
"""
Validate completed audit reports for unfilled placeholders and common issues.
Returns exit code 0 if valid, 1 if issues found.
"""
import argparse, re, sys
from pathlib import Path

def validate(path):
    report_path = Path(path)

    # Handle glob patterns
    if '*' in path:
        matches = list(report_path.parent.glob(report_path.name))
        if not matches:
            print(f"❌ No files matching: {path}")
            return 1
        report_path = matches[0]  # Use first match

    if not report_path.exists():
        print(f"❌ Report not found: {report_path}")
        return 1

    with open(report_path, 'r', encoding='utf-8') as f:
        content = f.read()

    issues = []

    # 1. Check for unfilled placeholders
    placeholders = re.findall(r'\{\{([^}]+)\}\}', content)
    if placeholders:
        issues.append(f"Unfilled placeholders ({len(placeholders)}): {', '.join(set(placeholders))}")

    # 2. Check for empty sections (## Header followed by ---)
    empty_sections = re.findall(r'## ([^\n]+)\n+---', content)
    if empty_sections:
        issues.append(f"Empty sections: {', '.join(empty_sections)}")

    # 3. Check for "N/A" or "No Data" in critical fields
    na_count = len(re.findall(r'\bN/A\b|\bNo Data\b|\bInsufficient data\b', content))
    if na_count > 3:
        issues.append(f"High N/A count ({na_count}) - may indicate missing data")

    # 4. Check report has minimum expected sections
    required_sections = ['Executive Summary', 'Hall of Fame', 'Red Flags']
    missing = [s for s in required_sections if s not in content]
    if missing:
        issues.append(f"Missing sections: {', '.join(missing)}")

    # Output results
    if issues:
        print(f"❌ VALIDATION FAILED: {report_path.name}")
        for issue in issues:
            print(f"   • {issue}")
        return 1
    else:
        print(f"✅ VALIDATION PASSED: {report_path.name}")
        return 0

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Validate audit report completeness")
    p.add_argument('--report', required=True, help="Path to report (supports glob patterns)")
    args = p.parse_args()
    sys.exit(validate(args.report))
