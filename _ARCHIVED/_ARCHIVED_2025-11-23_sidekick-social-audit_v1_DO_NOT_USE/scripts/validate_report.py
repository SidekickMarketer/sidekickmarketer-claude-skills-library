#!/usr/bin/env python3
"""
Validate Report Script
Checks completed social audit reports for missing placeholders and quality issues

Usage:
    python validate_report.py --report path/to/audit_report.md
    python validate_report.py --report path/to/audit_report.md --strict
"""

import argparse
import re
import sys
from pathlib import Path
from typing import List, Dict, Tuple


class ReportValidator:
    """Validates completed audit reports"""
    
    def __init__(self, report_path: Path, strict: bool = False):
        self.report_path = report_path
        self.strict = strict
        self.errors = []
        self.warnings = []
        self.info = []
        
        try:
            with open(report_path, 'r', encoding='utf-8') as f:
                self.content = f.read()
        except Exception as e:
            self.errors.append(f"❌ Failed to read report: {e}")
            self.content = ""
    
    def validate(self) -> bool:
        """Run all validation checks"""
        
        if not self.content:
            return False
        
        # Run checks
        self._check_placeholders()
        self._check_required_sections()
        self._check_data_quality()
        self._check_formatting()
        
        return len(self.errors) == 0
    
    def _check_placeholders(self):
        """Check for unfilled {{placeholder}} syntax"""
        
        # Find all remaining placeholders
        placeholders = re.findall(r'\{\{([^}]+)\}\}', self.content)
        
        if placeholders:
            self.errors.append(f"❌ {len(placeholders)} unfilled placeholder(s) found:")
            
            # Group by type
            placeholder_counts = {}
            for p in placeholders:
                placeholder_counts[p] = placeholder_counts.get(p, 0) + 1
            
            for placeholder, count in sorted(placeholder_counts.items()):
                self.errors.append(f"   • {{{{{placeholder}}}}} ({count}x)")
    
    def _check_required_sections(self):
        """Check that all required sections are present"""
        
        required_sections = [
            "Executive Summary",
            "The Macro View",
            "The \"Hall of Fame\"",
            "The Engine Room",
            "Sidekick \"Red Flags\"",
            "The Strategic Pivot",
            "90-Day Action Plan",
            "Measurement Framework"
        ]
        
        missing_sections = []
        
        for section in required_sections:
            # Check for section header (with or without ## prefix)
            if section not in self.content:
                missing_sections.append(section)
        
        if missing_sections:
            self.errors.append(f"❌ Missing required section(s):")
            for section in missing_sections:
                self.errors.append(f"   • {section}")
    
    def _check_data_quality(self):
        """Check for data quality issues"""
        
        # Check for vague phrases that should have specific numbers
        vague_phrases = [
            "many",
            "several",
            "some",
            "a lot",
            "numerous",
            "various",
            "multiple",
            "frequently"
        ]
        
        found_vague = []
        for phrase in vague_phrases:
            pattern = r'\b' + phrase + r'\b'
            if re.search(pattern, self.content, re.IGNORECASE):
                found_vague.append(phrase)
        
        if found_vague:
            if self.strict:
                self.errors.append(f"❌ Vague language detected (use specific numbers):")
            else:
                self.warnings.append(f"⚠️  Vague language detected (consider replacing with specific numbers):")
            
            for phrase in found_vague[:5]:  # Show first 5
                if self.strict:
                    self.errors.append(f"   • \"{phrase}\"")
                else:
                    self.warnings.append(f"   • \"{phrase}\"")
        
        # Check for TODO markers
        if "TODO" in self.content or "TK" in self.content:
            self.errors.append("❌ TODO/TK markers found - content incomplete")
        
        # Check for example/placeholder text
        example_phrases = [
            "[example]",
            "[placeholder]",
            "[insert ",
            "[add ",
            "lorem ipsum"
        ]
        
        for phrase in example_phrases:
            if phrase.lower() in self.content.lower():
                self.errors.append(f"❌ Example/placeholder text found: \"{phrase}\"")
    
    def _check_formatting(self):
        """Check for formatting issues"""
        
        # Check for empty tables
        table_pattern = r'\|[^\n]*\|'
        tables = re.findall(table_pattern, self.content)
        
        for table in tables:
            # Check if table row has only dashes and pipes (empty data)
            if re.match(r'^[\|\-\:\s]+$', table):
                continue  # This is a separator row
            
            # Check if cells are empty
            cells = [cell.strip() for cell in table.split('|')[1:-1]]
            if all(cell == '' for cell in cells):
                self.warnings.append("⚠️  Empty table row detected")
                break
        
        # Check for broken links
        link_pattern = r'\[([^\]]+)\]\(([^\)]+)\)'
        links = re.findall(link_pattern, self.content)
        
        for link_text, link_url in links:
            if not link_url or link_url.strip() == '':
                self.errors.append(f"❌ Broken link: [{link_text}]()")
        
        # Check for excessive line breaks
        if '\n\n\n\n' in self.content:
            self.warnings.append("⚠️  Excessive line breaks detected (>3 consecutive)")
    
    def _check_hall_of_fame(self):
        """Check Hall of Fame section for completeness"""
        
        # Find Hall of Fame section
        hof_pattern = r'## 2\. The "Hall of Fame".*?(?=##|\Z)'
        hof_match = re.search(hof_pattern, self.content, re.DOTALL)
        
        if not hof_match:
            return
        
        hof_content = hof_match.group(0)
        
        # Check for at least 3 posts
        post_pattern = r'### 🏆 Post #\d+'
        posts = re.findall(post_pattern, hof_content)
        
        if len(posts) < 3:
            self.warnings.append(f"⚠️  Only {len(posts)} Hall of Fame posts (recommend 5-10)")
        
        # Check that each post has required fields
        required_fields = ['Date:', 'Metric:', 'Format:', 'Why it\'s legendary:', 'Reboot Action:']
        
        for post_num in range(1, len(posts) + 1):
            post_section = re.search(
                f'### 🏆 Post #{post_num}:.*?(?=### 🏆|##|\Z)',
                hof_content,
                re.DOTALL
            )
            
            if post_section:
                post_content = post_section.group(0)
                
                for field in required_fields:
                    if field not in post_content:
                        self.warnings.append(
                            f"⚠️  Post #{post_num} missing field: {field}"
                        )
    
    def _check_metrics(self):
        """Check that metrics look realistic"""
        
        # Check for suspiciously round numbers
        round_numbers = re.findall(r'\b(100|1000|10000)%\b', self.content)
        
        if round_numbers:
            self.info.append(
                f"ℹ️  Very round percentages found ({len(round_numbers)}x) - verify accuracy"
            )
        
        # Check for engagement rates > 20% (suspiciously high)
        high_engagement = re.findall(r'(\d+(?:\.\d+)?)%.*?engagement', self.content, re.IGNORECASE)
        
        for rate in high_engagement:
            try:
                if float(rate) > 20:
                    self.warnings.append(
                        f"⚠️  Unusually high engagement rate: {rate}% - verify calculation"
                    )
            except ValueError:
                pass
    
    def print_report(self):
        """Print validation report"""
        
        print("\n" + "="*60)
        print(f"REPORT VALIDATION: {self.report_path.name}")
        print("="*60 + "\n")
        
        # Critical errors
        if self.errors:
            print("🔴 CRITICAL ISSUES (Must Fix Before Delivery):")
            for error in self.errors:
                print(f"  {error}")
            print()
        
        # Warnings
        if self.warnings:
            print("🟡 WARNINGS (Should Review):")
            for warning in self.warnings:
                print(f"  {warning}")
            print()
        
        # Info
        if self.info:
            print("ℹ️  NOTES:")
            for info in self.info:
                print(f"  {info}")
            print()
        
        # Overall status
        print("="*60)
        if not self.errors and not self.warnings:
            print("✅ RESULT: READY FOR DELIVERY")
            print("   Report meets all quality standards!")
        elif not self.errors:
            print("⚠️  RESULT: READY WITH WARNINGS")
            print("   Review warnings before delivery")
        else:
            print("❌ RESULT: NOT READY")
            print("   Fix critical issues before client delivery")
        print("="*60 + "\n")
    
    def get_summary(self) -> Dict[str, int]:
        """Get validation summary"""
        return {
            'errors': len(self.errors),
            'warnings': len(self.warnings),
            'info': len(self.info)
        }


def main():
    parser = argparse.ArgumentParser(
        description="Validate completed social audit reports"
    )
    parser.add_argument(
        '--report',
        required=True,
        help='Path to completed audit report (.md file)'
    )
    parser.add_argument(
        '--strict',
        action='store_true',
        help='Strict mode: treat warnings as errors'
    )
    parser.add_argument(
        '--json',
        action='store_true',
        help='Output results as JSON'
    )
    
    args = parser.parse_args()
    
    # Validate report exists
    report_path = Path(args.report)
    
    if not report_path.exists():
        print(f"❌ Report not found: {report_path}")
        sys.exit(1)
    
    # Run validation
    validator = ReportValidator(report_path, args.strict)
    is_valid = validator.validate()
    
    # Output results
    if args.json:
        import json
        summary = validator.get_summary()
        summary['valid'] = is_valid
        summary['path'] = str(report_path)
        print(json.dumps(summary, indent=2))
    else:
        validator.print_report()
    
    # Exit code
    sys.exit(0 if is_valid else 1)


if __name__ == "__main__":
    main()
