#!/usr/bin/env python3
"""
Parse Social Data Script - FINAL VERSION
Parses analytics files (CSV/XLSX) and extracts text from PDFs into unified JSON format
PRODUCTION-READY: Recursive search, all file types, smart de-duplication, comprehensive stats
"""

import argparse
import json
import csv
import re
import sys
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any, Optional
from collections import defaultdict

# Optional dependencies - graceful fallback
try:
    import openpyxl
    XLSX_SUPPORT = True
except ImportError:
    XLSX_SUPPORT = False

try:
    import PyPDF2
    PDF_SUPPORT = True
except ImportError:
    PDF_SUPPORT = False


class SocialDataParser:
    """Production-ready social media data parser"""

    def __init__(self, verbose: bool = True):
        self.posts = []
        self.errors = []
        self.verbose = verbose
        self.stats = {
            'files_found': 0,
            'files_processed': 0,
            'files_failed': 0,
            'files_skipped': 0,
            'posts_parsed': 0,
            'posts_skipped': 0,
            'duplicates_removed': 0,
            'skip_reasons': defaultdict(int),
            'posts_by_platform': defaultdict(int),
            'date_formats_found': defaultdict(int),
            'warnings': []
        }

    def parse_csv(self, file_path: Path) -> List[Dict[str, Any]]:
        """Parse CSV analytics file"""
        posts = []
        self.stats['files_processed'] += 1

        try:
            with open(file_path, 'r', encoding='utf-8-sig', errors='replace') as f:
                # Auto-detect delimiter
                sample = f.read(1024)
                f.seek(0)

                if ',' in sample: delimiter = ','
                elif '\t' in sample: delimiter = '\t'
                elif ';' in sample: delimiter = ';'
                else: delimiter = ','

                reader = csv.DictReader(f, delimiter=delimiter)

                for row_num, row in enumerate(reader, start=2):
                    try:
                        # Skip GBP description rows
                        if self._is_description_row(row):
                            self.stats['posts_skipped'] += 1
                            self.stats['skip_reasons']['description_row'] += 1
                            continue

                        post = self._normalize_row(row, file_path.name)
                        if post:
                            posts.append(post)
                            self.stats['posts_parsed'] += 1
                            self.stats['posts_by_platform'][post['platform']] += 1
                        else:
                            self.stats['posts_skipped'] += 1
                            self.stats['skip_reasons']['normalization_failed'] += 1

                    except Exception as e:
                        self.errors.append(f"Row {row_num} in {file_path.name}: {str(e)}")
                        self.stats['posts_skipped'] += 1
                        self.stats['skip_reasons']['parse_error'] += 1

            if self.verbose and len(posts) > 0:
                print(f"✅ Parsed {len(posts)} posts from {file_path.name}")
            elif len(posts) == 0 and "gbp" not in file_path.name.lower():
                if self.verbose:
                    print(f"⚠️  Parsed 0 posts from {file_path.name} (Check date formats)")

        except Exception as e:
            self.errors.append(f"Failed to parse {file_path.name}: {e}")
            self.stats['files_failed'] += 1

        return posts

    def parse_excel(self, file_path: Path) -> List[Dict[str, Any]]:
        """Parse Excel analytics file"""
        posts = []

        if not XLSX_SUPPORT:
            self.stats['files_skipped'] += 1
            self.stats['skip_reasons']['xlsx_no_library'] += 1
            return posts

        self.stats['files_processed'] += 1

        try:
            workbook = openpyxl.load_workbook(file_path, read_only=True, data_only=True)
            sheet = workbook.active

            # Get headers from first row
            headers = []
            for cell in sheet[1]:
                headers.append(str(cell.value) if cell.value else '')

            # Process data rows
            for row_num, row in enumerate(sheet.iter_rows(min_row=2, values_only=True), start=2):
                try:
                    # Convert row to dict
                    row_dict = {headers[i]: row[i] for i in range(len(headers)) if i < len(row)}

                    if self._is_description_row(row_dict):
                        self.stats['posts_skipped'] += 1
                        self.stats['skip_reasons']['description_row'] += 1
                        continue

                    post = self._normalize_row(row_dict, file_path.name)
                    if post:
                        posts.append(post)
                        self.stats['posts_parsed'] += 1
                        self.stats['posts_by_platform'][post['platform']] += 1
                    else:
                        self.stats['posts_skipped'] += 1
                        self.stats['skip_reasons']['normalization_failed'] += 1

                except Exception as e:
                    self.errors.append(f"Row {row_num} in {file_path.name}: {str(e)}")
                    self.stats['posts_skipped'] += 1
                    self.stats['skip_reasons']['parse_error'] += 1

            workbook.close()

            if self.verbose and len(posts) > 0:
                print(f"✅ Parsed {len(posts)} posts from {file_path.name}")

        except Exception as e:
            self.errors.append(f"Failed to parse Excel {file_path.name}: {e}")
            self.stats['files_failed'] += 1

        return posts

    def parse_pdf(self, file_path: Path) -> List[Dict[str, Any]]:
        """Parse PDF: Extract text for analysis"""
        posts = []
        extracted_text = ""

        self.stats['files_processed'] += 1

        # Try to extract text if library exists
        if PDF_SUPPORT:
            try:
                with open(file_path, 'rb') as f:
                    reader = PyPDF2.PdfReader(f)
                    for page in reader.pages:
                        text = page.extract_text()
                        if text:
                            extracted_text += text + "\n"
            except Exception as e:
                self.stats['warnings'].append(f"Could not extract text from {file_path.name}: {e}")

        # Extract date from filename
        date_match = re.search(r'(\d{4})-(\d{2})', file_path.name)
        year_month = f"{date_match.group(1)}-{date_match.group(2)}" if date_match else None

        # Create entry (stub or with text)
        post = {
            'source_file': file_path.name,
            'source_type': 'pdf',
            'platform': self._detect_platform(file_path.name, {}),
            'post_type': 'PDF Archive',
            'note': 'Visual review recommended - text extracted for context'
        }

        if year_month:
            post['date'] = f"{year_month}-15"  # Mid-month approximation

        if extracted_text:
            post['caption'] = extracted_text[:500]  # First 500 chars for context
            post['_full_text'] = extracted_text  # Full text for advanced analysis

        posts.append(post)
        self.stats['posts_parsed'] += 1
        self.stats['posts_by_platform'][post['platform']] += 1

        status = "Text Extracted" if len(extracted_text) > 50 else "Stub Created"
        if self.verbose:
            print(f"✅ PDF Processed ({status}): {file_path.name}")

        return posts

    def _is_description_row(self, row: Dict[str, str]) -> bool:
        """Detect GBP secondary header rows"""
        indicators = ['number of', 'total count', 'interactions with', 'people that viewed']
        row_str = " ".join(str(v).lower() for v in row.values() if v)
        return any(ind in row_str for ind in indicators)

    def _normalize_row(self, row: Dict[str, str], filename: str) -> Optional[Dict[str, Any]]:
        """Normalize CSV/Excel row to standard format"""

        # Detect platform
        platform = self._detect_platform(filename, row)
        if platform == 'gbp_aggregate':
            return None

        # Extract date
        date = self._extract_date(row)
        if not date:
            return None

        # Initialize post
        post = {
            'date': date,
            'platform': platform,
            'source_file': filename
        }

        # Field mappings
        mappings = {
            'post_type': ['type', 'post type', 'media_type', 'format', 'media type'],
            'caption': ['caption', 'description', 'text', 'post text', 'content', 'message'],
            'likes': ['likes', 'like count', 'reactions'],
            'comments': ['comments', 'comment count'],
            'shares': ['shares', 'share count', 'reshares'],
            'saves': ['saves', 'save count', 'saved', 'bookmarks'],
            'reach': ['reach', 'accounts reached', 'unique viewers'],
            'impressions': ['impressions', 'views', 'total views'],
            'link_clicks': ['link clicks', 'clicks', 'website clicks'],
            'engagement_rate': ['engagement rate', 'engagement'],
            'permalink': ['permalink', 'post url', 'url', 'link']
        }

        row_lower = {k.lower().strip(): v for k, v in row.items() if v is not None}

        for field, variations in mappings.items():
            for variation in variations:
                if variation in row_lower:
                    value = row_lower[variation]

                    # Parse numeric fields
                    if field in ['likes', 'comments', 'shares', 'saves', 'reach', 'impressions', 'link_clicks']:
                        post[field] = self._parse_number(value)
                    elif field == 'engagement_rate':
                        post[field] = self._parse_percentage(value)
                    else:
                        post[field] = value
                    break

        # Calculate engagement rate if missing and we have reach
        if 'engagement_rate' not in post and post.get('reach', 0) > 0:
            total_eng = sum([
                post.get('likes', 0),
                post.get('comments', 0),
                post.get('shares', 0),
                post.get('saves', 0)
            ])
            post['engagement_rate'] = round((total_eng / post['reach']) * 100, 2)
            post['total_engagement'] = total_eng

        # Validation warnings
        if post.get('engagement_rate', 0) > 50:
            self.stats['warnings'].append(f"Suspicious engagement rate ({post['engagement_rate']}%) on {date} - {platform}")

        if post.get('reach', 0) == 0 and post.get('likes', 0) > 0:
            self.stats['warnings'].append(f"Missing reach data on {date} - {platform} (has {post.get('likes')} likes)")

        return post if len(post) > 3 else None

    def _detect_platform(self, filename: str, row: Dict[str, str]) -> str:
        """Detect platform from filename or row content"""
        fn = filename.lower()

        # Check for GBP aggregate files
        if 'gbp' in fn or 'google' in fn:
            if any(k in row for k in ['Store code', 'Business name', 'Total views']):
                return 'gbp_aggregate'
            return 'google_business_profile'

        # Platform keywords
        if 'instagram' in fn or 'ig' in fn or '_ig_' in fn:
            return 'instagram'
        if 'facebook' in fn or 'fb' in fn or '_fb_' in fn:
            return 'facebook'
        if 'linkedin' in fn or 'li' in fn:
            return 'linkedin'
        if 'twitter' in fn or 'x_' in fn:
            return 'twitter'

        return 'unknown'

    def _extract_date(self, row: Dict[str, str]) -> Optional[str]:
        """Extract date from row - prioritize 'Publish time'"""
        date_fields = [
            'publish time', 'publish date', 'posted date',
            'created', 'timestamp', 'posted', 'date'
        ]

        row_lower = {k.lower().strip(): v for k, v in row.items() if v}

        for field in date_fields:
            if field in row_lower:
                date_str = row_lower[field]

                # Skip Meta's "Lifetime" bug
                if "lifetime" in str(date_str).lower():
                    continue

                parsed_date = self._parse_date(date_str)
                if parsed_date:
                    return parsed_date

        return None

    def _parse_date(self, date_str: str) -> Optional[str]:
        """Parse date string to YYYY-MM-DD format"""
        if not date_str or str(date_str).strip() == '':
            return None

        date_str = str(date_str).strip()

        # Try common formats
        formats = [
            '%m/%d/%Y %H:%M',
            '%Y-%m-%d',
            '%m/%d/%Y',
            '%d/%m/%Y',
            '%Y/%m/%d',
            '%Y-%m-%d %H:%M:%S',
            '%B %d, %Y',
            '%b %d, %Y',
            '%m-%d-%Y',
            '%d-%m-%Y'
        ]

        for fmt in formats:
            try:
                dt = datetime.strptime(date_str, fmt)
                self.stats['date_formats_found'][fmt] += 1
                return dt.strftime('%Y-%m-%d')
            except ValueError:
                continue

        # Regex fallback
        match = re.search(r'(\d{4})-(\d{2})-(\d{2})', date_str)
        if match:
            return match.group(0)

        return None

    def _parse_number(self, value: str) -> int:
        """Parse number with k/m notation"""
        if not value:
            return 0

        clean = str(value).lower().strip().replace(',', '').replace(' ', '')
        multiplier = 1

        if 'k' in clean:
            multiplier = 1000
            clean = clean.replace('k', '')
        elif 'm' in clean:
            multiplier = 1000000
            clean = clean.replace('m', '')

        try:
            return int(float(clean) * multiplier)
        except:
            return 0

    def _parse_percentage(self, value: str) -> float:
        """Parse percentage string"""
        if not value:
            return 0.0

        clean = str(value).replace('%', '').strip()
        try:
            return float(clean)
        except:
            return 0.0

    def search_directory(self, directory: Path, recursive: bool = True) -> List[Dict[str, Any]]:
        """Search directory for all analytics files"""
        all_posts = []

        # Search pattern
        pattern = "**/*" if recursive else "*"

        # Find all files by type
        csv_files = list(directory.glob(f"{pattern}.csv"))
        xlsx_files = list(directory.glob(f"{pattern}.xlsx")) + list(directory.glob(f"{pattern}.xls"))
        pdf_files = list(directory.glob(f"{pattern}.pdf"))

        self.stats['files_found'] = len(csv_files) + len(xlsx_files) + len(pdf_files)

        if self.verbose:
            print(f"\n📂 Searching {directory.name}/ {'(recursive)' if recursive else '(non-recursive)'}...")
            print(f"   Found {len(csv_files)} CSV, {len(xlsx_files)} Excel, {len(pdf_files)} PDF files\n")

        # Process CSVs
        for i, csv_file in enumerate(csv_files, 1):
            if self.verbose:
                print(f"[{i}/{len(csv_files)}] Processing {csv_file.name}")
            all_posts.extend(self.parse_csv(csv_file))

        # Process Excel files
        if xlsx_files and XLSX_SUPPORT:
            for i, xlsx_file in enumerate(xlsx_files, 1):
                if self.verbose:
                    print(f"[{i}/{len(xlsx_files)}] Processing {xlsx_file.name}")
                all_posts.extend(self.parse_excel(xlsx_file))
        elif xlsx_files and not XLSX_SUPPORT:
            if self.verbose:
                print(f"⚠️  {len(xlsx_files)} Excel files found but skipped (install openpyxl)")
            self.stats['files_skipped'] += len(xlsx_files)
            self.stats['skip_reasons']['xlsx_no_library'] += len(xlsx_files)

        # Process PDFs
        if pdf_files and PDF_SUPPORT:
            for i, pdf_file in enumerate(pdf_files, 1):
                if self.verbose:
                    print(f"[{i}/{len(pdf_files)}] Processing {pdf_file.name}")
                all_posts.extend(self.parse_pdf(pdf_file))
        elif pdf_files and not PDF_SUPPORT:
            if self.verbose:
                print(f"⚠️  {len(pdf_files)} PDF files found but skipped (install PyPDF2)")
            self.stats['files_skipped'] += len(pdf_files)
            self.stats['skip_reasons']['pdf_no_library'] += len(pdf_files)

        return all_posts

    def save_json(self, posts: List[Dict[str, Any]], output_path: Path):
        """Save parsed posts to JSON with smart de-duplication"""
        unique_posts = []
        seen = set()

        # Filter and sort
        valid_posts = [p for p in posts if p.get('date')]
        valid_posts.sort(key=lambda x: (x['date'], x.get('source_type', '') != 'pdf'))

        # De-duplicate
        for p in valid_posts:
            # Create unique key
            key = f"{p['date']}_{p['platform']}"

            # For CSV duplicates, use more specific key
            if p.get('source_type') != 'pdf':
                likes = p.get('likes', 0)
                comments = p.get('comments', 0)
                key = f"{p['date']}_{p['platform']}_{likes}_{comments}"

            if key not in seen:
                seen.add(key)
                unique_posts.append(p)
            else:
                self.stats['duplicates_removed'] += 1

        # Calculate final date range
        date_range = {
            'earliest': unique_posts[0]['date'] if unique_posts else None,
            'latest': unique_posts[-1]['date'] if unique_posts else None
        }

        # Build output
        output = {
            'metadata': {
                'generated_at': datetime.now().isoformat(),
                'total_posts': len(unique_posts),
                'duplicates_removed': self.stats['duplicates_removed'],
                'date_range': date_range,
                'platforms': dict(self.stats['posts_by_platform']),
                'parsing_stats': {
                    'files_processed': self.stats['files_processed'],
                    'files_failed': self.stats['files_failed'],
                    'files_skipped': self.stats['files_skipped'],
                    'posts_parsed': self.stats['posts_parsed'],
                    'posts_skipped': self.stats['posts_skipped'],
                    'errors': len(self.errors)
                }
            },
            'posts': unique_posts
        }

        # Save
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(output, f, indent=2)

        if self.verbose:
            print(f"\n✅ Saved {len(unique_posts)} posts to {output_path}")

    def print_statistics(self):
        """Print comprehensive statistics"""
        print("\n" + "=" * 60)
        print("PARSING STATISTICS")
        print("=" * 60)
        print(f"\nFiles:")
        print(f"  Found:     {self.stats['files_found']}")
        print(f"  Processed: {self.stats['files_processed']}")
        print(f"  Failed:    {self.stats['files_failed']}")
        print(f"  Skipped:   {self.stats['files_skipped']}")

        print(f"\nPosts:")
        print(f"  Parsed:     {self.stats['posts_parsed']}")
        print(f"  Skipped:    {self.stats['posts_skipped']}")
        print(f"  Duplicates: {self.stats['duplicates_removed']}")

        print(f"\nBy Platform:")
        for platform, count in self.stats['posts_by_platform'].items():
            print(f"  {platform.title()}: {count}")

        if self.stats['skip_reasons']:
            print(f"\nSkip Reasons:")
            for reason, count in self.stats['skip_reasons'].items():
                print(f"  {reason}: {count}")

        if self.stats['warnings']:
            print(f"\n⚠️  Warnings ({len(self.stats['warnings'])}):")
            for warning in self.stats['warnings'][:5]:  # Show first 5
                print(f"  • {warning}")
            if len(self.stats['warnings']) > 5:
                print(f"  ... and {len(self.stats['warnings']) - 5} more")

        if self.errors:
            print(f"\n❌ Errors ({len(self.errors)}):")
            for error in self.errors[:3]:  # Show first 3
                print(f"  • {error}")
            if len(self.errors) > 3:
                print(f"  ... and {len(self.errors) - 3} more")

        print("\n" + "=" * 60)


def main():
    parser = argparse.ArgumentParser(
        description="Parse social media analytics into unified JSON format",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Recursive search (default)
  %(prog)s --search-dir ./social_data --output results.json

  # Non-recursive search
  %(prog)s --search-dir ./social_data --no-recursive --output results.json

  # Specific files
  %(prog)s --analytics file1.csv file2.xlsx --output results.json

  # Quiet mode
  %(prog)s --search-dir ./social_data --output results.json --quiet
        """
    )

    parser.add_argument('--analytics', nargs='+', help='Specific analytics files to parse')
    parser.add_argument('--pdfs', nargs='+', help='Specific PDF files to parse')
    parser.add_argument('--search-dir', help='Directory to search for analytics files')
    parser.add_argument('--output', required=True, help='Output JSON file path')
    parser.add_argument('--no-recursive', action='store_true', help='Disable recursive directory search')
    parser.add_argument('--quiet', action='store_true', help='Suppress progress messages')

    args = parser.parse_args()

    verbose = not args.quiet
    parser_obj = SocialDataParser(verbose=verbose)
    all_posts = []

    # Process specific files
    if args.analytics:
        for f in args.analytics:
            file_path = Path(f)
            if not file_path.exists():
                print(f"❌ File not found: {f}")
                continue

            if file_path.suffix.lower() == '.csv':
                all_posts.extend(parser_obj.parse_csv(file_path))
            elif file_path.suffix.lower() in ['.xlsx', '.xls']:
                all_posts.extend(parser_obj.parse_excel(file_path))
            else:
                print(f"⚠️  Unsupported file type: {f}")

    if args.pdfs:
        for f in args.pdfs:
            file_path = Path(f)
            if file_path.exists():
                all_posts.extend(parser_obj.parse_pdf(file_path))
            else:
                print(f"❌ File not found: {f}")

    # Search directory
    if args.search_dir:
        path = Path(args.search_dir)
        if path.exists():
            recursive = not args.no_recursive
            all_posts.extend(parser_obj.search_directory(path, recursive=recursive))
        else:
            print(f"❌ Directory not found: {args.search_dir}")
            sys.exit(1)

    # Save and report
    if all_posts:
        parser_obj.save_json(all_posts, Path(args.output))
        if verbose:
            parser_obj.print_statistics()
    else:
        print("❌ No posts found. Check file paths and date formats.")
        if verbose:
            parser_obj.print_statistics()
        sys.exit(1)


if __name__ == "__main__":
    main()
