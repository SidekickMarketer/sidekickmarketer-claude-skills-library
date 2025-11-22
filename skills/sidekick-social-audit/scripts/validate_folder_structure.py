#!/usr/bin/env python3
"""
Validate Folder Structure Script
Checks if client folder meets Sidekick social audit requirements

Usage:
    python validate_folder_structure.py --path /path/to/client-folder
    python validate_folder_structure.py --path ./client-cma --verbose
"""

import argparse
import sys
from pathlib import Path
from typing import List, Tuple, Dict


class FolderValidator:
    """Validates client folder structure for social audit readiness"""
    
    def __init__(self, client_path: Path, verbose: bool = False):
        self.client_path = Path(client_path)
        self.verbose = verbose
        self.errors = []
        self.warnings = []
        self.info = []
        
    def validate(self) -> bool:
        """Run all validation checks"""
        
        if not self.client_path.exists():
            self.errors.append(f"❌ Path does not exist: {self.client_path}")
            return False
        
        if not self.client_path.is_dir():
            self.errors.append(f"❌ Path is not a directory: {self.client_path}")
            return False
        
        # Run checks
        self._check_client_profile()
        self._check_social_media_folder()
        self._check_social_strategy()
        self._check_content_calendars()
        self._check_performance_data()
        self._check_post_archive()
        self._check_file_naming_conventions()
        
        return len(self.errors) == 0
    
    def _check_client_profile(self):
        """Check for CLIENT_PROFILE.md file"""
        
        # Look for file matching pattern: 00_*_CLIENT_PROFILE.md
        profiles = list(self.client_path.glob("00_*_CLIENT_PROFILE.md"))
        
        if len(profiles) == 0:
            self.errors.append("❌ Missing: 00_*_CLIENT_PROFILE.md")
        elif len(profiles) > 1:
            self.warnings.append(f"⚠️  Multiple CLIENT_PROFILE files found: {len(profiles)}")
        else:
            self.info.append(f"✅ Found: {profiles[0].name}")
            
            # Check if file has content
            if profiles[0].stat().st_size < 100:
                self.warnings.append("⚠️  CLIENT_PROFILE.md appears empty or incomplete")
    
    def _check_social_media_folder(self):
        """Check for 07_Social_Media directory and structure"""
        
        social_dir = self.client_path / "07_Social_Media"
        
        if not social_dir.exists():
            self.errors.append("❌ Missing: 07_Social_Media/ directory")
            return
        
        self.info.append("✅ Found: 07_Social_Media/")
        
        # Check required subdirectories
        required_subdirs = [
            "01_Content_Calendars",
            "02_Performance_Data",
            "04_Audit_Reports"
        ]
        
        for subdir in required_subdirs:
            subdir_path = social_dir / subdir
            if not subdir_path.exists():
                self.errors.append(f"❌ Missing: 07_Social_Media/{subdir}/")
            else:
                self.info.append(f"✅ Found: 07_Social_Media/{subdir}/")
        
        # Check optional subdirectory
        post_archive = social_dir / "03_Post_Archive"
        if not post_archive.exists():
            self.warnings.append("⚠️  Optional: 07_Social_Media/03_Post_Archive/ not found")
        else:
            self.info.append("✅ Found: 07_Social_Media/03_Post_Archive/")
    
    def _check_social_strategy(self):
        """Check for SOCIAL_STRATEGY.md file"""
        
        strategy_path = self.client_path / "07_Social_Media" / "00_SOCIAL_STRATEGY.md"
        
        if not strategy_path.exists():
            self.warnings.append("⚠️  Missing: 07_Social_Media/00_SOCIAL_STRATEGY.md")
            self.warnings.append("   → Strategy will be inferred from execution")
        else:
            self.info.append("✅ Found: 07_Social_Media/00_SOCIAL_STRATEGY.md")
            
            # Check if file has content
            if strategy_path.stat().st_size < 200:
                self.warnings.append("⚠️  SOCIAL_STRATEGY.md appears empty or incomplete")
    
    def _check_content_calendars(self):
        """Check for content calendar files"""
        
        calendars_dir = self.client_path / "07_Social_Media" / "01_Content_Calendars"
        
        if not calendars_dir.exists():
            return
        
        # Look for CSV files
        csv_files = list(calendars_dir.glob("*.csv"))
        xlsx_files = list(calendars_dir.glob("*.xlsx"))
        
        total_files = len(csv_files) + len(xlsx_files)
        
        if total_files == 0:
            self.errors.append("❌ No content calendar files found in 01_Content_Calendars/")
        else:
            self.info.append(f"✅ Found {total_files} content calendar file(s)")
            
            # Check naming convention
            properly_named = 0
            for csv_file in csv_files:
                # Check if matches YYYY-MM_*.csv pattern
                name = csv_file.stem
                if self._is_valid_date_prefix(name):
                    properly_named += 1
                elif self.verbose:
                    self.warnings.append(f"⚠️  Non-standard name: {csv_file.name}")
            
            if properly_named < len(csv_files):
                self.warnings.append(
                    f"⚠️  {len(csv_files) - properly_named}/{len(csv_files)} calendar files "
                    f"don't follow YYYY-MM naming convention"
                )
    
    def _check_performance_data(self):
        """Check for analytics files"""
        
        data_dir = self.client_path / "07_Social_Media" / "02_Performance_Data"
        
        if not data_dir.exists():
            return
        
        # Look for CSV/XLSX files
        csv_files = list(data_dir.glob("*.csv"))
        xlsx_files = list(data_dir.glob("*.xlsx"))
        
        total_files = len(csv_files) + len(xlsx_files)
        
        if total_files == 0:
            self.warnings.append("⚠️  No analytics files found in 02_Performance_Data/")
            self.warnings.append("   → Audit will be qualitative-only")
        else:
            self.info.append(f"✅ Found {total_files} analytics file(s)")
            
            # Check for platform-specific files
            platforms_found = set()
            for file in csv_files + xlsx_files:
                name_lower = file.name.lower()
                if 'instagram' in name_lower or 'ig' in name_lower:
                    platforms_found.add('Instagram')
                if 'facebook' in name_lower or 'fb' in name_lower:
                    platforms_found.add('Facebook')
                if 'google' in name_lower or 'gbp' in name_lower or 'gmb' in name_lower:
                    platforms_found.add('Google Business Profile')
            
            if platforms_found:
                self.info.append(f"   Platforms detected: {', '.join(sorted(platforms_found))}")
    
    def _check_post_archive(self):
        """Check for post archive PDFs (optional)"""
        
        archive_dir = self.client_path / "07_Social_Media" / "03_Post_Archive"
        
        if not archive_dir.exists():
            return
        
        pdf_files = list(archive_dir.glob("*.pdf"))
        
        if len(pdf_files) == 0:
            self.info.append("ℹ️  No PDF files in 03_Post_Archive/ (optional)")
        else:
            self.info.append(f"✅ Found {len(pdf_files)} post archive PDF(s)")
    
    def _check_file_naming_conventions(self):
        """Check overall file naming compliance"""
        
        calendars_dir = self.client_path / "07_Social_Media" / "01_Content_Calendars"
        data_dir = self.client_path / "07_Social_Media" / "02_Performance_Data"
        
        issues = []
        
        # Check calendars
        if calendars_dir.exists():
            for file in calendars_dir.glob("*"):
                if file.is_file() and file.suffix in ['.csv', '.xlsx']:
                    if not self._is_valid_date_prefix(file.stem):
                        issues.append(file.name)
        
        if issues and self.verbose:
            self.info.append(f"ℹ️  Files with non-standard naming: {len(issues)}")
    
    def _is_valid_date_prefix(self, filename: str) -> bool:
        """Check if filename starts with YYYY-MM format"""
        
        parts = filename.split('_')
        if len(parts) == 0:
            return False
        
        first_part = parts[0]
        
        # Check YYYY-MM format
        if len(first_part) == 7 and first_part[4] == '-':
            try:
                year = int(first_part[:4])
                month = int(first_part[5:7])
                return 2000 <= year <= 2100 and 1 <= month <= 12
            except ValueError:
                return False
        
        return False
    
    def print_report(self):
        """Print validation report"""
        
        print("\n" + "="*60)
        print(f"VALIDATION REPORT: {self.client_path.name}")
        print("="*60 + "\n")
        
        # Critical errors
        if self.errors:
            print("🔴 CRITICAL ISSUES (Must Fix):")
            for error in self.errors:
                print(f"  {error}")
            print()
        
        # Warnings
        if self.warnings:
            print("🟡 WARNINGS (Should Fix):")
            for warning in self.warnings:
                print(f"  {warning}")
            print()
        
        # Info (only in verbose mode or if all clear)
        if self.verbose or (not self.errors and not self.warnings):
            print("✅ STATUS:")
            for info in self.info:
                print(f"  {info}")
            print()
        
        # Overall status
        print("="*60)
        if not self.errors and not self.warnings:
            print("✅ RESULT: READY FOR AUDIT")
            print("   All requirements met!")
        elif not self.errors:
            print("⚠️  RESULT: READY WITH WARNINGS")
            print("   Audit can proceed, but address warnings for best results")
        else:
            print("❌ RESULT: NOT READY")
            print("   Fix critical issues before running audit")
        print("="*60 + "\n")
    
    def get_summary(self) -> Dict[str, int]:
        """Get validation summary counts"""
        return {
            'errors': len(self.errors),
            'warnings': len(self.warnings),
            'info': len(self.info)
        }


def main():
    parser = argparse.ArgumentParser(
        description="Validate client folder structure for social audit"
    )
    parser.add_argument(
        '--path',
        required=True,
        help='Path to client folder'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Show detailed information'
    )
    parser.add_argument(
        '--json',
        action='store_true',
        help='Output results as JSON'
    )
    
    args = parser.parse_args()
    
    # Run validation
    validator = FolderValidator(args.path, args.verbose)
    is_valid = validator.validate()
    
    # Output results
    if args.json:
        import json
        summary = validator.get_summary()
        summary['valid'] = is_valid
        summary['path'] = str(validator.client_path)
        print(json.dumps(summary, indent=2))
    else:
        validator.print_report()
    
    # Exit code
    sys.exit(0 if is_valid else 1)


if __name__ == "__main__":
    main()
