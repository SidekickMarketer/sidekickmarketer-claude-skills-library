#!/usr/bin/env python3
"""
Parse Social Data Script
Parses analytics files (CSV/XLSX) and post PDFs into unified JSON format

Usage:
    python parse_social_data.py --analytics path/to/analytics.csv --output data.json
    python parse_social_data.py --search-dir path/to/02_Performance_Data/ --output data.json
    python parse_social_data.py --pdfs path/to/*.pdf --output data.json --ocr
"""

import argparse
import json
import csv
import re
import sys
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any, Optional


class SocialDataParser:
    """Parses social media data from various sources"""
    
    def __init__(self):
        self.posts = []
        self.errors = []
        
    def parse_csv(self, file_path: Path) -> List[Dict[str, Any]]:
        """Parse CSV analytics file"""
        
        posts = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                # Try to detect delimiter
                sample = f.read(1024)
                f.seek(0)
                
                # Check for common delimiters
                if ',' in sample:
                    delimiter = ','
                elif '\t' in sample:
                    delimiter = '\t'
                elif ';' in sample:
                    delimiter = ';'
                else:
                    delimiter = ','
                
                reader = csv.DictReader(f, delimiter=delimiter)
                
                for row_num, row in enumerate(reader, start=2):
                    try:
                        post = self._normalize_row(row, file_path.name)
                        if post:
                            posts.append(post)
                    except Exception as e:
                        self.errors.append(f"Row {row_num} in {file_path.name}: {e}")
            
            print(f"✅ Parsed {len(posts)} posts from {file_path.name}")
            
        except Exception as e:
            self.errors.append(f"Failed to parse {file_path.name}: {e}")
        
        return posts
    
    def _normalize_row(self, row: Dict[str, str], filename: str) -> Optional[Dict[str, Any]]:
        """Normalize a CSV row to standard format"""
        
        # Detect platform from filename or content
        platform = self._detect_platform(filename, row)
        
        # Try to extract date
        date = self._extract_date(row)
        if not date:
            return None
        
        # Try to extract engagement metrics
        post = {
            'date': date,
            'platform': platform,
            'source_file': filename
        }
        
        # Map common column variations
        mappings = {
            'post_type': ['type', 'post_type', 'media_type', 'format', 'post type'],
            'caption': ['caption', 'description', 'text', 'post text', 'content'],
            'likes': ['likes', 'like count', 'reactions', 'reaction count'],
            'comments': ['comments', 'comment count', 'comments count'],
            'shares': ['shares', 'share count', 'shares count'],
            'saves': ['saves', 'save count', 'saved', 'bookmarks'],
            'reach': ['reach', 'accounts reached', 'unique viewers'],
            'impressions': ['impressions', 'views', 'total views'],
            'link_clicks': ['link clicks', 'clicks', 'website clicks'],
            'engagement_rate': ['engagement rate', 'engagement', 'engagement %']
        }
        
        # Extract all available fields
        row_lower = {k.lower().strip(): v for k, v in row.items()}
        
        for field, variations in mappings.items():
            for variation in variations:
                if variation in row_lower:
                    value = row_lower[variation]
                    
                    # Clean numeric fields
                    if field in ['likes', 'comments', 'shares', 'saves', 'reach', 'impressions', 'link_clicks']:
                        post[field] = self._parse_number(value)
                    elif field == 'engagement_rate':
                        post[field] = self._parse_percentage(value)
                    else:
                        post[field] = value
                    break
        
        # Calculate engagement rate if not provided
        if 'engagement_rate' not in post and 'reach' in post and post.get('reach', 0) > 0:
            total_engagement = sum([
                post.get('likes', 0),
                post.get('comments', 0),
                post.get('shares', 0),
                post.get('saves', 0)
            ])
            post['engagement_rate'] = round((total_engagement / post['reach']) * 100, 2)
        
        return post if len(post) > 3 else None
    
    def _detect_platform(self, filename: str, row: Dict[str, str]) -> str:
        """Detect platform from filename or row content"""
        
        filename_lower = filename.lower()
        
        if 'instagram' in filename_lower or 'ig' in filename_lower:
            return 'instagram'
        elif 'facebook' in filename_lower or 'fb' in filename_lower:
            return 'facebook'
        elif 'google' in filename_lower or 'gbp' in filename_lower or 'gmb' in filename_lower:
            return 'google_business_profile'
        elif 'linkedin' in filename_lower:
            return 'linkedin'
        elif 'twitter' in filename_lower or 'x.com' in filename_lower:
            return 'twitter'
        
        # Try to detect from row content
        row_str = ' '.join(str(v) for v in row.values()).lower()
        
        if 'instagram' in row_str:
            return 'instagram'
        elif 'facebook' in row_str:
            return 'facebook'
        
        return 'unknown'
    
    def _extract_date(self, row: Dict[str, str]) -> Optional[str]:
        """Extract date from row"""
        
        date_fields = ['date', 'posted date', 'publish date', 'created', 'timestamp', 'posted']
        
        row_lower = {k.lower().strip(): v for k, v in row.items()}
        
        for field in date_fields:
            if field in row_lower:
                date_str = row_lower[field]
                parsed_date = self._parse_date(date_str)
                if parsed_date:
                    return parsed_date
        
        return None
    
    def _parse_date(self, date_str: str) -> Optional[str]:
        """Parse date string to YYYY-MM-DD format"""
        
        if not date_str or date_str.strip() == '':
            return None
        
        # Try common date formats
        formats = [
            '%Y-%m-%d',
            '%m/%d/%Y',
            '%d/%m/%Y',
            '%Y/%m/%d',
            '%B %d, %Y',
            '%b %d, %Y',
            '%Y-%m-%d %H:%M:%S',
            '%m/%d/%Y %H:%M',
        ]
        
        for fmt in formats:
            try:
                dt = datetime.strptime(date_str.strip(), fmt)
                return dt.strftime('%Y-%m-%d')
            except ValueError:
                continue
        
        # Try to extract YYYY-MM-DD pattern
        match = re.search(r'(\d{4})-(\d{2})-(\d{2})', date_str)
        if match:
            return match.group(0)
        
        return None
    
    def _parse_number(self, value: str) -> int:
        """Parse number from string (handles commas, K, M suffixes)"""
        
        if isinstance(value, (int, float)):
            return int(value)
        
        if not value or value.strip() == '':
            return 0
        
        # Remove common formatting
        value = str(value).replace(',', '').replace(' ', '').strip()
        
        # Handle K/M suffixes
        if value.endswith('K') or value.endswith('k'):
            return int(float(value[:-1]) * 1000)
        elif value.endswith('M') or value.endswith('m'):
            return int(float(value[:-1]) * 1000000)
        
        try:
            return int(float(value))
        except ValueError:
            return 0
    
    def _parse_percentage(self, value: str) -> float:
        """Parse percentage from string"""
        
        if isinstance(value, (int, float)):
            return float(value)
        
        if not value or value.strip() == '':
            return 0.0
        
        # Remove % sign and convert
        value = str(value).replace('%', '').strip()
        
        try:
            return float(value)
        except ValueError:
            return 0.0
    
    def parse_pdf(self, file_path: Path, use_ocr: bool = False) -> List[Dict[str, Any]]:
        """Parse PDF post archive (placeholder - requires PDF libraries)"""
        
        # Note: Full PDF parsing would require PyPDF2 and pytesseract
        # For now, this is a placeholder that extracts basic info
        
        posts = []
        
        try:
            # Extract date from filename if possible
            date_match = re.search(r'(\d{4})-(\d{2})', file_path.name)
            if date_match:
                year_month = f"{date_match.group(1)}-{date_match.group(2)}"
                
                posts.append({
                    'source_file': file_path.name,
                    'source_type': 'pdf',
                    'date_range': year_month,
                    'note': 'PDF parsing requires manual review or full OCR setup'
                })
                
                print(f"⚠️  {file_path.name}: PDF detected but not fully parsed")
                print(f"   Install PyPDF2 and pytesseract for full PDF extraction")
            
        except Exception as e:
            self.errors.append(f"Failed to process PDF {file_path.name}: {e}")
        
        return posts
    
    def search_directory(self, directory: Path) -> List[Dict[str, Any]]:
        """Search directory for analytics files and parse them"""
        
        all_posts = []
        
        # Find all CSV and XLSX files
        csv_files = list(directory.glob("*.csv"))
        xlsx_files = list(directory.glob("*.xlsx"))
        
        print(f"\n📂 Searching {directory.name}...")
        print(f"   Found {len(csv_files)} CSV files, {len(xlsx_files)} XLSX files\n")
        
        # Parse CSV files
        for csv_file in csv_files:
            posts = self.parse_csv(csv_file)
            all_posts.extend(posts)
        
        # Note about XLSX files
        if xlsx_files:
            print(f"⚠️  XLSX files found but not parsed (install openpyxl for XLSX support)")
            print(f"   Convert to CSV or install: pip install openpyxl\n")
        
        return all_posts
    
    def save_json(self, posts: List[Dict[str, Any]], output_path: Path):
        """Save parsed posts to JSON"""
        
        # Sort by date
        posts_sorted = sorted(posts, key=lambda x: x.get('date', ''))
        
        output = {
            'metadata': {
                'generated_at': datetime.now().isoformat(),
                'total_posts': len(posts_sorted),
                'date_range': {
                    'start': posts_sorted[0].get('date') if posts_sorted else None,
                    'end': posts_sorted[-1].get('date') if posts_sorted else None
                }
            },
            'posts': posts_sorted
        }
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(output, f, indent=2)
        
        print(f"\n✅ Saved {len(posts_sorted)} posts to {output_path}")
        
        if self.errors:
            print(f"\n⚠️  {len(self.errors)} errors occurred during parsing:")
            for error in self.errors[:5]:  # Show first 5 errors
                print(f"   {error}")
            if len(self.errors) > 5:
                print(f"   ... and {len(self.errors) - 5} more")


def main():
    parser = argparse.ArgumentParser(
        description="Parse social media analytics files into unified JSON format"
    )
    parser.add_argument(
        '--analytics',
        nargs='+',
        help='One or more analytics CSV files to parse'
    )
    parser.add_argument(
        '--search-dir',
        help='Directory to search for analytics files'
    )
    parser.add_argument(
        '--pdfs',
        nargs='+',
        help='One or more PDF files to parse (requires OCR libraries)'
    )
    parser.add_argument(
        '--ocr',
        action='store_true',
        help='Use OCR for PDF text extraction (requires pytesseract)'
    )
    parser.add_argument(
        '--output',
        required=True,
        help='Output JSON file path'
    )
    
    args = parser.parse_args()
    
    if not args.analytics and not args.search_dir and not args.pdfs:
        print("❌ Error: Must provide --analytics, --search-dir, or --pdfs")
        sys.exit(1)
    
    # Parse data
    data_parser = SocialDataParser()
    all_posts = []
    
    # Parse analytics files
    if args.analytics:
        for file_path in args.analytics:
            path = Path(file_path)
            if path.exists():
                posts = data_parser.parse_csv(path)
                all_posts.extend(posts)
            else:
                print(f"⚠️  File not found: {file_path}")
    
    # Search directory
    if args.search_dir:
        search_path = Path(args.search_dir)
        if search_path.exists() and search_path.is_dir():
            posts = data_parser.search_directory(search_path)
            all_posts.extend(posts)
        else:
            print(f"❌ Directory not found: {args.search_dir}")
            sys.exit(1)
    
    # Parse PDFs
    if args.pdfs:
        for file_path in args.pdfs:
            path = Path(file_path)
            if path.exists():
                posts = data_parser.parse_pdf(path, args.ocr)
                all_posts.extend(posts)
            else:
                print(f"⚠️  File not found: {file_path}")
    
    # Save results
    if all_posts:
        data_parser.save_json(all_posts, Path(args.output))
    else:
        print("\n❌ No posts were successfully parsed")
        sys.exit(1)


if __name__ == "__main__":
    main()
