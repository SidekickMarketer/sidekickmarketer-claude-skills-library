#!/usr/bin/env python3
"""
Build Client Profile from Notion Exports + Web Sources
Extracts, consolidates, and generates a comprehensive 20-section unified client profile.
"""
import argparse
import json
import re
import os
import urllib.request
import urllib.error
import ssl
from html.parser import HTMLParser
from pathlib import Path
from datetime import datetime
from collections import defaultdict
from typing import Dict, List, Any, Optional


class SimpleHTMLTextExtractor(HTMLParser):
    """Extract text content from HTML, stripping tags."""

    def __init__(self):
        super().__init__()
        self.text_parts = []
        self.skip_tags = {'script', 'style', 'nav', 'header', 'footer', 'noscript'}
        self.current_skip = False

    def handle_starttag(self, tag, attrs):
        if tag in self.skip_tags:
            self.current_skip = True

    def handle_endtag(self, tag):
        if tag in self.skip_tags:
            self.current_skip = False

    def handle_data(self, data):
        if not self.current_skip:
            text = data.strip()
            if text:
                self.text_parts.append(text)

    def get_text(self):
        return '\n'.join(self.text_parts)


class WebFetcher:
    """Fetch and extract content from web pages."""

    def __init__(self):
        # Create SSL context that doesn't verify (for simplicity)
        self.ssl_context = ssl.create_default_context()
        self.ssl_context.check_hostname = False
        self.ssl_context.verify_mode = ssl.CERT_NONE

    def fetch_url(self, url: str) -> Optional[str]:
        """Fetch URL and return text content."""
        try:
            # Add headers to look like a browser
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
            }
            request = urllib.request.Request(url, headers=headers)

            with urllib.request.urlopen(request, timeout=15, context=self.ssl_context) as response:
                html = response.read().decode('utf-8', errors='replace')

            # Extract text from HTML
            parser = SimpleHTMLTextExtractor()
            parser.feed(html)
            return parser.get_text()

        except Exception as e:
            print(f"  ⚠️  Could not fetch {url}: {e}")
            return None

    def fetch_website(self, base_url: str) -> Dict[str, str]:
        """Fetch main pages from a website."""
        results = {}

        # Normalize URL
        if not base_url.startswith('http'):
            base_url = 'https://' + base_url
        base_url = base_url.rstrip('/')

        # Pages to try fetching
        pages = {
            'home': '',
            'about': '/about',
            'about-us': '/about-us',
            'services': '/services',
            'contact': '/contact',
            'team': '/team',
            'our-story': '/our-story',
        }

        print(f"  🌐 Fetching: {base_url}")

        for page_name, path in pages.items():
            url = base_url + path
            content = self.fetch_url(url)
            if content and len(content) > 100:
                results[f"[web:{page_name}]"] = content
                print(f"     ✓ {page_name}")

        return results

class ProfileBuilder:
    """Extracts and consolidates client data from multiple source files."""

    # Extraction patterns for each profile section
    EXTRACTION_PATTERNS = {
        # === Section 1: Business Core ===
        'client_name': [
            r'(?:client|company|business)\s*(?:name)?[:\s]+([A-Z][^,\n]{2,50})',
            r'^#\s*([A-Z][^-\n]{2,50})',  # H1 headers often contain client name
        ],
        'legal_name': [
            r'(?:legal name|registered as|incorporated as)[:\s]+([^\n]{5,100})',
            r'(?:llc|inc|corp|ltd)[^\n]*([A-Z][^,\n]{2,80})',
        ],
        'dba': [
            r'(?:dba|doing business as|trade name)[:\s]+([^\n]{3,80})',
        ],
        'industry': [
            r'(?:industry|sector|vertical)[:\s]+([^\n,]{3,50})',
            r'(?:we are a|we\'re a)\s+([^\n,]{3,50})\s+(?:company|business|agency)',
        ],
        'website': [
            r'(?:website|url|site)[:\s]+(https?://[^\s\n]+)',
            r'(https?://(?:www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}[^\s\n]*)',
        ],
        'location': [
            r'(?:location|address|based in|headquarters)[:\s]+([^\n]{5,100})',
            r'(\d+[^,\n]+,\s*[A-Z][a-z]+,?\s*[A-Z]{2}\s*\d{5})',  # US address pattern
        ],
        'service_area': [
            r'(?:service area|serves?|coverage)[:\s]+([^\n]{5,150})',
            r'(?:serving|located in)\s+([^\n]{5,100})',
        ],
        'founded_year': [
            r'(?:founded|established|since)[:\s]*(\d{4})',
            r'(\d{4})[^\n]*(?:founded|started|opened)',
            # Prose patterns for founding year
            r'founded\s+(?:by\s+)?[A-Z][a-z]+\s+[A-Z][a-z]+.*?in\s+(\d{4})',
            r'since\s+(\d{4})',
            r'(?:opened|started|began)\s+(?:in\s+)?(\d{4})',
        ],
        'company_size': [
            r'(?:employees?|team size|staff)[:\s]*(\d+(?:-\d+)?)',
            r'(\d+(?:-\d+)?)\s*(?:employees?|people|team members)',
            # Prose patterns for team size (e.g., "over 30 instructors")
            r'(?:over\s+)?(\d+)\+?\s*(?:instructors?|teachers?|faculty)',
            r'(?:team of|staff of)\s*(\d+)',
            r'(\d+)\s*(?:person|member)\s*team',
        ],
        'hours_of_operation': [
            r'(?:hours?|open)[:\s]+([^\n]{5,100})',
            r'((?:Mon|Monday)[^\n]*\d{1,2}(?::\d{2})?\s*(?:am|pm)[^\n]{0,50})',
            r'(\d{1,2}(?::\d{2})?\s*(?:am|pm)\s*[-–]\s*\d{1,2}(?::\d{2})?\s*(?:am|pm))',
        ],

        # === Section 2: Contacts ===
        'contact_primary': [
            r'(?:primary contact|owner|ceo|founder)[:\s]+([^\n(]{3,50})',
            r'(?:contact)[:\s]+([A-Z][a-z]+\s+[A-Z][a-z]+)',
            # Prose patterns for ownership
            r'(?:owned by|co-owners?|current owners?)[:\s]*([A-Z][a-z]+\s+[A-Z][a-z]+)',
            r'([A-Z][a-z]+\s+[A-Z][a-z]+)\s+(?:is the|as)\s+(?:owner|co-owner)',
            r'(?:joined|took over|purchased by)\s+([A-Z][a-z]+\s+[A-Z][a-z]+)',
        ],
        'contact_secondary': [
            # Multiple owners pattern - captures second person in "X and Y"
            r'(?:owned by|co-owners?)[^\n]*?and\s+([A-Z][a-z]+\s+[A-Z][a-z]+)',
            r'([A-Z][a-z]+\s+[A-Z][a-z]+)\s+(?:and|&)\s+[A-Z][a-z]+\s+[A-Z][a-z]+\s+(?:are|as)\s+(?:owners?|co-owners?)',
        ],
        'contact_primary_email': [
            r'(?:email|e-mail)[:\s]+([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})',
            # Email with name context
            r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})',
        ],
        'contact_primary_phone': [
            r'(?:phone|tel|mobile)[:\s]*(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})',
            r'(\d{3}[-.\s]?\d{3}[-.\s]?\d{4})',
        ],
        'decision_maker': [
            r'(?:decision maker|approver|stakeholder)[:\s]+([^\n]{3,50})',
        ],
        'billing_contact': [
            r'(?:billing|accounts payable|ap contact)[:\s]+([^\n]{3,50})',
        ],

        # === Section 3: Target Audience ===
        'target_audience': [
            r'(?:target audience|icp|ideal customer)[:\s]+([^\n]{10,500})',
            r'(?:who we serve|our customers)[:\s]+([^\n]{10,500})',
        ],
        'demographics': [
            r'(?:demographics?|age range|income)[:\s]+([^\n]{10,200})',
        ],
        'psychographics': [
            r'(?:psychographics?|values|lifestyle|interests)[:\s]+([^\n]{10,300})',
        ],

        # === Section 4: Brand Voice ===
        'brand_tone': [
            r'(?:tone|voice)[:\s]+([^\n]{5,200})',
            r'(?:brand personality)[:\s]+([^\n]{5,200})',
        ],
        'brand_words_use': [
            r'(?:words? to use|preferred terms?|say this)[:\s]+([^\n]{10,200})',
        ],
        'brand_words_avoid': [
            r'(?:words? to avoid|don\'t say|never use)[:\s]+([^\n]{10,200})',
        ],

        # === Section 5: Products & Services ===
        'primary_service': [
            r'(?:primary service|main offering|core service)[:\s]+([^\n]{5,100})',
        ],

        # === Section 6: SOW/Deliverables ===
        'instagram_posts': [
            r'(?:instagram)[^\n]*?(\d+)\s*(?:posts?|per month|/month|monthly)',
            r'(\d+)\s*(?:ig|instagram)\s*posts?',
        ],
        'facebook_posts': [
            r'(?:facebook|fb)[^\n]*?(\d+)\s*(?:posts?|per month|/month|monthly)',
            r'(\d+)\s*(?:fb|facebook)\s*posts?',
        ],
        'gbp_posts': [
            r'(?:gbp|google business)[^\n]*?(\d+)\s*(?:posts?|per month|/month|monthly)',
            r'(\d+)\s*gbp\s*posts?',
        ],
        'contract_start': [
            r'(?:start date|begins?|effective)[:\s]*(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})',
        ],
        'contract_end': [
            r'(?:end date|expires?|through)[:\s]*(\d{1,2}[/-]\d{1,2}[/-]\d{2,4})',
        ],
        'monthly_retainer': [
            r'(?:retainer|monthly fee|price)[:\s]*\$?([\d,]+)',
        ],

        # === Section 10: Seasonality & Calendar ===
        'peak_season': [
            r'(?:peak|busy|high)\s*(?:season|time|period)[:\s]+([^\n]{5,100})',
            r'((?:back.to.school|summer camp|enrollment)\s+(?:push|campaign|season)[^\n]{0,50})',
            r'((?:Q[1-4]|January|August|September)[^\n]*(?:peak|busy|enrollment)[^\n]{0,50})',
        ],
        'slow_season': [
            r'(?:slow|off|quiet)\s*(?:season|time|period)[:\s]+([^\n]{5,100})',
        ],
        'key_events': [
            r'((?:recital|concert|showcase|open house)[^\n]{5,100})',
            r'((?:New Year|back.to.school|summer)[^\n]*(?:push|campaign|promotion)[^\n]{0,50})',
        ],

        # === Section 11: Visual Brand ===
        'brand_colors': [
            r'(?:brand colors?|primary color|colors?)[:\s]+([^\n]{5,100})',
            r'(#[0-9A-Fa-f]{6})',  # Hex codes
        ],
        'logo_usage': [
            r'(?:logo|logomark|brand mark)[:\s]+([^\n]{5,150})',
        ],

        # === Section 12: Account Access ===
        'instagram_handle': [
            r'(?:instagram|ig)[:\s]*@?([a-zA-Z0-9._]{1,30})',
            r'instagram\.com/([a-zA-Z0-9._]+)',
        ],
        'facebook_page': [
            r'(?:facebook|fb)[:\s]*(https?://[^\s]+facebook\.com/[^\s]+)',
            r'facebook\.com/([a-zA-Z0-9.]+)',
        ],
        'gbp_listing': [
            r'(?:google business|gbp|google my business)[:\s]+(https?://[^\s]+)',
        ],
        'linkedin': [
            r'(?:linkedin)[:\s]*(https?://[^\s]+linkedin\.com/[^\s]+)',
        ],
        'twitter': [
            r'(?:twitter|x\.com)[:\s]*@?([a-zA-Z0-9_]{1,15})',
        ],
        'youtube': [
            r'(?:youtube)[:\s]*(https?://[^\s]+youtube\.com/[^\s]+)',
        ],
        'tiktok': [
            r'(?:tiktok)[:\s]*@?([a-zA-Z0-9._]{1,30})',
        ],

        # === Section 14: Business Model & Revenue ===
        'average_transaction': [
            r'(?:average|avg)\s*(?:transaction|sale|order)[:\s]*\$?([\d,]+)',
            r'(?:ticket size|order value)[:\s]*\$?([\d,]+)',
        ],
        'customer_ltv': [
            r'(?:lifetime value|ltv|clv)[:\s]*\$?([\d,]+)',
        ],
        'lead_source': [
            r'(?:lead source|where.*(?:come from|find us))[:\s]+([^\n]{10,200})',
            r'(?:referrals?|word of mouth)[:\s]*(\d+)%',
        ],

        # === Section 15: Origin Story ===
        'founder_name': [
            r'(?:founder|owner|started by)[:\s]+([A-Z][a-z]+\s+[A-Z][a-z]+)',
        ],
        'why_started': [
            r'(?:why.*start|mission|purpose)[:\s]+([^\n]{20,500})',
        ],

        # === Section 16: Local Presence & Reputation ===
        'google_rating': [
            r'(?:google)\s*(?:rating|reviews?)[:\s]*(\d\.?\d?)\s*(?:stars?)?',
            r'(\d\.?\d?)\s*(?:stars?)?\s*(?:on\s*)?google',
        ],
        'google_review_count': [
            r'(?:google)[^\n]*?(\d+)\s*reviews?',
            r'(\d+)\s*(?:google\s*)?reviews?',
        ],
        'yelp_rating': [
            r'(?:yelp)\s*(?:rating)?[:\s]*(\d\.?\d?)',
        ],

        # === Section 17: Marketing History ===
        'previous_agency': [
            r'(?:previous|past|former)\s*(?:agency|vendor|marketing)[:\s]+([^\n]{5,100})',
        ],
        'past_ad_spend': [
            r'(?:ad spend|advertising budget|marketing budget)[:\s]*\$?([\d,]+)',
        ],

        # === Section 18: Content Bank ===
        'has_testimonials': [
            r'(?:testimonials?|reviews?)[:\s]+([^\n]{10,200})',
        ],
        'faq_item': [
            r'(?:faq|frequently asked|common question)[:\s]+([^\n]{10,200})',
        ],

        # === Section 19: Email & CRM ===
        'email_platform': [
            r'(?:email\s*(?:platform|tool|service)|mailchimp|klaviyo|activecampaign|constant contact)[:\s]*([^\n]{3,50})',
        ],
        'email_list_size': [
            r'(?:list size|subscribers?|email list)[:\s]*(\d[\d,]*)',
            r'(\d[\d,]*)\s*(?:subscribers?|contacts?|emails?)',
        ],
        'crm_platform': [
            r'(?:crm|hubspot|salesforce|pipedrive)[:\s]*([^\n]{3,50})',
        ],

        # === Section 20: Relationship Notes ===
        'communication_preference': [
            r'(?:prefer(?:red)?|best)\s*(?:contact|communication|way to reach)[:\s]+([^\n]{5,100})',
        ],
        'meeting_cadence': [
            r'(?:meeting|call|check-in)\s*(?:cadence|frequency|schedule)[:\s]+([^\n]{5,100})',
        ],
    }

    def __init__(self, client_folder: str, additional_folders: List[str] = None, urls: List[str] = None):
        self.client_folder = Path(client_folder)
        self.client_name = self.client_folder.name.replace('client-', '').upper()
        self.source_dir = self.client_folder / "notion_export"

        # Audit files go to archive subfolder to keep client root clean
        self.audit_dir = self.client_folder / "90_Archive" / "Profile_Build"
        self.audit_dir.mkdir(parents=True, exist_ok=True)

        # Additional folders to scan (beyond notion_export)
        self.additional_folders = []
        if additional_folders:
            for folder in additional_folders:
                folder_path = Path(folder)
                if folder_path.exists() and folder_path.is_dir():
                    self.additional_folders.append(folder_path)
                else:
                    print(f"  ⚠️  Skipping invalid folder: {folder}")

        # URLs to fetch (client website, social profiles, etc.)
        self.urls = urls or []
        self.web_content = {}  # source_name -> content

        # Storage for extracted data
        self.extracted = defaultdict(list)  # field -> [{value, source, line, confidence}]
        self.conflicts = []
        self.gaps = []

    def scan_files(self) -> List[Path]:
        """Find all processable files from client folder and additional folders.

        Scans the ENTIRE client folder recursively, not just notion_export.
        Creates a complete file manifest to ensure nothing is missed.
        """
        # Supported extensions we can process
        processable_extensions = {'.md', '.txt', '.csv', '.json'}

        # Extensions we acknowledge but can't process (logged for transparency)
        unprocessable_extensions = {'.pdf', '.doc', '.docx', '.xlsx', '.xls', '.png', '.jpg', '.jpeg', '.gif', '.mp4', '.mov'}

        files = []
        skipped_files = []
        unprocessable_files = []

        # Skip patterns - folders/files to ignore
        skip_patterns = {
            '__pycache__', '.git', 'node_modules', '.DS_Store',
            '_extraction_audit.md', '_conflicts.md', '_gaps.md',  # Skip our output files
            '_file_manifest.md',  # Skip manifest output
            '90_Archive',  # Skip archived files - outdated data
        }

        # Scan ENTIRE client folder (not just notion_export)
        all_files_found = []
        if self.client_folder.exists():
            for f in self.client_folder.rglob('*'):
                if f.is_file():
                    all_files_found.append(f)

        # Scan additional folders
        for folder in self.additional_folders:
            for f in folder.rglob('*'):
                if f.is_file() and f not in all_files_found:
                    all_files_found.append(f)

        # Categorize all files
        for f in all_files_found:
            # Check if should skip
            if any(skip in str(f) for skip in skip_patterns):
                skipped_files.append((f, 'system/output file'))
                continue

            ext = f.suffix.lower()

            if ext in processable_extensions:
                files.append(f)
            elif ext in unprocessable_extensions:
                unprocessable_files.append((f, f'format not supported ({ext})'))
            elif ext:
                skipped_files.append((f, f'unknown extension ({ext})'))
            else:
                skipped_files.append((f, 'no extension'))

        # Store for manifest generation
        self.file_manifest = {
            'total_found': len(all_files_found),
            'processable': files,
            'unprocessable': unprocessable_files,
            'skipped': skipped_files,
        }

        return sorted(files)

    def _generate_file_manifest(self):
        """Generate a manifest of ALL files found - nothing missed."""
        manifest = f"""# File Manifest - Complete Inventory
**Client:** {self.client_name}
**Generated:** {datetime.now().isoformat()}

This manifest shows EVERY file found in the client folder to ensure nothing is missed.

---

## Summary

| Category | Count |
|----------|-------|
| **Total Files Found** | {self.file_manifest['total_found']} |
| **Files Processed** | {len(self.file_manifest['processable'])} |
| **Unprocessable (need manual review)** | {len(self.file_manifest['unprocessable'])} |
| **Skipped (system files)** | {len(self.file_manifest['skipped'])} |

---

## ✅ Files Processed

These files were successfully scanned for client data:

"""
        for f in self.file_manifest['processable']:
            rel = self._get_relative_path(f)
            manifest += f"- `{rel}`\n"

        manifest += """

---

## ⚠️ Unprocessable Files (REVIEW MANUALLY)

These files exist but couldn't be processed automatically. **Review them manually** to ensure no data is missed:

"""
        if self.file_manifest['unprocessable']:
            for f, reason in self.file_manifest['unprocessable']:
                rel = self._get_relative_path(f)
                manifest += f"- [ ] `{rel}` - {reason}\n"
        else:
            manifest += "*None*\n"

        manifest += """

---

## ⏭️ Skipped Files

These files were intentionally skipped (system files, output files, etc.):

"""
        if self.file_manifest['skipped']:
            for f, reason in self.file_manifest['skipped']:
                rel = self._get_relative_path(f)
                manifest += f"- `{rel}` - {reason}\n"
        else:
            manifest += "*None*\n"

        with open(self.audit_dir / "_file_manifest.md", 'w') as f:
            f.write(manifest)

    def _get_relative_path(self, filepath: Path) -> str:
        """Get relative path for display, handling client folder and additional folders."""
        # Try client folder first (most common case now)
        try:
            return str(filepath.relative_to(self.client_folder))
        except ValueError:
            pass

        # Try additional folders
        for folder in self.additional_folders:
            try:
                return f"[{folder.name}]/{filepath.relative_to(folder)}"
            except ValueError:
                pass

        # Fallback to filename
        return filepath.name

    def fetch_web_content(self):
        """Fetch content from provided URLs."""
        if not self.urls:
            return

        print("")
        print("🌐 Fetching web content...")

        fetcher = WebFetcher()

        for url in self.urls:
            # Determine URL type
            if 'facebook.com' in url or 'fb.com' in url:
                source_name = '[web:facebook]'
                content = fetcher.fetch_url(url)
            elif 'instagram.com' in url:
                source_name = '[web:instagram]'
                content = fetcher.fetch_url(url)
            elif 'linkedin.com' in url:
                source_name = '[web:linkedin]'
                content = fetcher.fetch_url(url)
            elif 'google.com/maps' in url or 'goo.gl' in url:
                source_name = '[web:gbp]'
                content = fetcher.fetch_url(url)
            else:
                # Assume it's the main website - fetch multiple pages
                pages = fetcher.fetch_website(url)
                self.web_content.update(pages)
                continue

            if content:
                self.web_content[source_name] = content
                print(f"  ✓ {source_name}")

    def extract_from_web_content(self, source: str, content: str) -> Dict[str, List[dict]]:
        """Extract data from web page content."""
        extractions = defaultdict(list)

        # Apply all extraction patterns
        for field, patterns in self.EXTRACTION_PATTERNS.items():
            for pattern in patterns:
                try:
                    matches = re.finditer(pattern, content, re.IGNORECASE | re.MULTILINE)
                    for match in matches:
                        value = match.group(1).strip()
                        if len(value) >= 3:
                            extractions[field].append({
                                'value': value,
                                'source': source,
                                'line': 0,  # No line numbers for web
                                'pattern': pattern[:30] + '...',
                                'confidence': self._calculate_confidence(field, value) * 0.9  # Slightly lower confidence for web
                            })
                except re.error:
                    continue

        # Also extract section-style content
        self._extract_sections(content, source, extractions)

        return extractions

    def extract_from_file(self, filepath: Path) -> Dict[str, List[dict]]:
        """Extract all possible data points from a single file."""
        try:
            with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()
        except Exception as e:
            print(f"  ⚠️  Could not read {filepath.name}: {e}")
            return {}

        rel_path = self._get_relative_path(filepath)
        extractions = defaultdict(list)

        # Apply all extraction patterns
        for field, patterns in self.EXTRACTION_PATTERNS.items():
            for pattern in patterns:
                try:
                    matches = re.finditer(pattern, content, re.IGNORECASE | re.MULTILINE)
                    for match in matches:
                        value = match.group(1).strip()
                        if len(value) >= 3:  # Minimum viable data
                            # Calculate line number
                            line_num = content[:match.start()].count('\n') + 1

                            extractions[field].append({
                                'value': value,
                                'source': rel_path,
                                'line': line_num,
                                'pattern': pattern[:30] + '...',
                                'confidence': self._calculate_confidence(field, value)
                            })
                except re.error:
                    continue

        # Also extract structured sections (headers with content)
        self._extract_sections(content, rel_path, extractions)

        return extractions

    def _calculate_confidence(self, field: str, value: str) -> float:
        """Score confidence of extraction (0-1)."""
        confidence = 0.5

        # Length bonus
        if len(value) > 20:
            confidence += 0.1
        if len(value) > 50:
            confidence += 0.1

        # Specificity bonus
        if field == 'website' and 'http' in value:
            confidence += 0.3
        if field == 'location' and re.search(r'\d{5}', value):  # Has ZIP
            confidence += 0.2

        return min(confidence, 1.0)

    def _extract_sections(self, content: str, source: str, extractions: dict):
        """Extract content under specific headers."""
        section_mappings = {
            # Section 3: Target Audience
            r'##?\s*(?:target\s*)?audience': 'target_audience_section',
            r'##?\s*(?:ideal\s*customer|icp)': 'target_audience_section',
            r'##?\s*customer\s*(?:segments?|personas?)': 'customer_segments_section',
            r'##?\s*customer\s*journey': 'customer_journey_section',
            r'##?\s*(?:pain\s*points?|objections?)': 'objections_section',
            # Section 4: Brand Voice
            r'##?\s*brand\s*(?:voice|tone|personality)': 'brand_voice_section',
            r'##?\s*(?:messaging|taglines?)': 'brand_voice_section',
            # Section 5: Products & Services
            r'##?\s*(?:products?|services?|offerings?)': 'products_section',
            r'##?\s*(?:what\s*we\s*(?:do|offer)|our\s*services)': 'products_section',
            # Section 6: Content Pillars
            r'##?\s*content\s*pillars?': 'content_pillars_section',
            r'##?\s*content\s*(?:strategy|themes?)': 'content_pillars_section',
            # Section 7: SOW/Deliverables
            r'##?\s*(?:sow|scope|deliverables)': 'sow_section',
            r'##?\s*(?:contract|agreement|services\s*included)': 'sow_section',
            # Section 8: KPIs & Goals
            r'##?\s*(?:kpis?|goals?|metrics?|objectives?)': 'kpis_section',
            r'##?\s*(?:targets?|benchmarks?)': 'kpis_section',
            # Section 9: Competitors
            r'##?\s*competitors?': 'competitors_section',
            r'##?\s*(?:competitive\s*analysis|landscape)': 'competitors_section',
            # Section 10: Seasonality
            r'##?\s*(?:seasonality|calendar|events?)': 'seasonality_section',
            r'##?\s*(?:key\s*dates?|holidays?|blackout)': 'seasonality_section',
            # Section 11: Visual Brand
            r'##?\s*(?:visual|brand)\s*(?:guidelines?|identity|assets?)': 'visual_brand_section',
            r'##?\s*(?:colors?|typography|fonts?)': 'visual_brand_section',
            # Section 12: Account Access
            r'##?\s*(?:account\s*access|credentials?|logins?)': 'account_access_section',
            r'##?\s*(?:social\s*(?:media\s*)?accounts?|platforms?)': 'account_access_section',
            # Section 13: Guidelines & Constraints
            r'##?\s*(?:guidelines?|constraints?|rules?)': 'guidelines_section',
            r'##?\s*(?:approval|legal|compliance)': 'guidelines_section',
            r'##?\s*(?:do\s*not|avoid|prohibited)': 'guidelines_section',
            # Section 14: Business Model & Revenue
            r'##?\s*(?:business\s*model|revenue|how.*make\s*money)': 'business_model_section',
            r'##?\s*(?:lead\s*sources?|where.*leads?\s*come)': 'lead_sources_section',
            r'##?\s*(?:pricing|price\s*points?)': 'pricing_section',
            # Section 15: Origin Story
            r'##?\s*(?:origin|founder|our\s*story|about\s*us)': 'origin_story_section',
            r'##?\s*(?:history|milestones?|timeline)': 'milestones_section',
            r'##?\s*(?:mission|vision|why\s*we)': 'mission_section',
            # Section 16: Local Presence & Reputation
            r'##?\s*(?:reviews?|reputation|ratings?)': 'reviews_section',
            r'##?\s*(?:community|local\s*(?:presence|involvement))': 'community_section',
            r'##?\s*(?:partnerships?|sponsors?)': 'partnerships_section',
            # Section 17: Marketing History
            r'##?\s*(?:marketing\s*history|past\s*marketing|previous)': 'marketing_history_section',
            r'##?\s*(?:what.*worked|successes?)': 'what_worked_section',
            r'##?\s*(?:what.*(?:failed|flopped)|lessons?\s*learned)': 'what_flopped_section',
            # Section 18: Content Bank & Assets
            r'##?\s*(?:content\s*(?:bank|library|assets?)|assets?)': 'content_bank_section',
            r'##?\s*(?:photos?|images?|video)': 'media_assets_section',
            r'##?\s*(?:testimonials?|case\s*stud)': 'testimonials_section',
            r'##?\s*(?:faqs?|frequently\s*asked|common\s*questions?)': 'faq_section',
            # Section 19: Email & CRM
            r'##?\s*(?:email\s*(?:marketing)?|newsletter)': 'email_section',
            r'##?\s*(?:crm|customer\s*relationship|lead\s*management)': 'crm_section',
            # Section 20: Relationship Notes
            r'##?\s*(?:relationship|client\s*(?:notes?|preferences?))': 'relationship_section',
            r'##?\s*(?:communication|contact\s*preferences?)': 'communication_section',
            r'##?\s*(?:working\s*style|how\s*to\s*work)': 'working_style_section',
        }

        for pattern, field in section_mappings.items():
            match = re.search(
                f'({pattern}[^\n]*\n)(.*?)(?=\n##|\n#|\\Z)',
                content,
                re.IGNORECASE | re.DOTALL
            )
            if match:
                header = match.group(1).strip()
                section_content = match.group(2).strip()
                if len(section_content) > 20:
                    line_num = content[:match.start()].count('\n') + 1
                    extractions[field].append({
                        'value': section_content[:2000],  # Cap at 2000 chars
                        'source': source,
                        'line': line_num,
                        'header': header,
                        'confidence': 0.8
                    })

    def consolidate(self):
        """Merge extracted data, handling duplicates and conflicts."""
        consolidated = {}

        for field, items in self.extracted.items():
            if not items:
                self.gaps.append(field)
                continue

            # Sort by confidence, then by recency (newer files first)
            sorted_items = sorted(items, key=lambda x: (-x['confidence'], x['source']))

            # Check for conflicts (significantly different values)
            unique_values = list(set(item['value'][:100].lower() for item in items))
            if len(unique_values) > 1 and len(items) > 1:
                self.conflicts.append({
                    'field': field,
                    'values': [{'value': i['value'][:200], 'source': i['source']} for i in items[:5]]
                })

            # Take highest confidence value
            best = sorted_items[0]
            consolidated[field] = {
                'value': best['value'],
                'source': best['source'],
                'confidence': best['confidence'],
                'alternatives': len(items) - 1
            }

        return consolidated

    def build(self) -> dict:
        """Run full extraction and consolidation pipeline."""
        files = self.scan_files()

        if not files and not self.urls:
            print(f"❌ No files found and no URLs provided")
            print(f"   Place Notion markdown exports in: {self.source_dir}")
            print(f"   Or provide URLs with --urls")
            return None

        # Show what we're scanning
        source_count = len([f for f in files if self.source_dir.exists() and str(f).startswith(str(self.source_dir))])
        additional_count = len(files) - source_count

        print(f"📂 Processing {len(files)} files + {len(self.urls)} URLs:")
        if self.source_dir.exists() and source_count > 0:
            print(f"   • notion_export/: {source_count} files")
        if self.additional_folders:
            for folder in self.additional_folders:
                folder_count = len([f for f in files if str(f).startswith(str(folder))])
                print(f"   • {folder.name}/: {folder_count} files")
        if self.urls:
            print(f"   • web URLs: {len(self.urls)}")
        print("=" * 60)

        # Extract from all files
        for filepath in files:
            rel = self._get_relative_path(filepath)
            print(f"  📄 {rel}")
            file_extractions = self.extract_from_file(filepath)

            for field, items in file_extractions.items():
                self.extracted[field].extend(items)

        # Fetch and extract from web content
        self.fetch_web_content()
        if self.web_content:
            print("")
            print("📊 Extracting from web pages...")
            for source, content in self.web_content.items():
                print(f"  🌐 {source}")
                web_extractions = self.extract_from_web_content(source, content)
                for field, items in web_extractions.items():
                    self.extracted[field].extend(items)

        # Consolidate
        consolidated = self.consolidate()

        # Generate outputs
        self._generate_profile(consolidated)
        self._generate_extraction_audit(consolidated)
        self._generate_conflicts_report()
        self._generate_gaps_report()
        self._generate_file_manifest()

        print("\n" + "=" * 60)
        print("✅ PROFILE BUILD COMPLETE")
        print(f"   📄 Profile: {self.client_folder}/00_{self.client_name}_CLIENT_PROFILE.md")
        print(f"   📊 Audit: {self.audit_dir}/_extraction_audit.md")
        print(f"   📁 File Manifest: {self.audit_dir}/_file_manifest.md")
        if self.conflicts:
            print(f"   ⚠️  Conflicts: {self.audit_dir}/_conflicts.md ({len(self.conflicts)} items)")
        if self.gaps:
            print(f"   ❓ Gaps: {self.audit_dir}/_gaps.md ({len(self.gaps)} fields)")
        if self.file_manifest['unprocessable']:
            print(f"   ⚠️  REVIEW MANUALLY: {len(self.file_manifest['unprocessable'])} files couldn't be auto-processed")

        return consolidated

    def _generate_profile(self, data: dict):
        """Generate the comprehensive 13-section profile markdown."""
        def get_val(field, default="[NOT FOUND]"):
            return data.get(field, {}).get('value', default)

        def get_source(field):
            return data.get(field, {}).get('source', '-')

        today = datetime.now().strftime('%Y-%m-%d')
        client_display = self.client_name.replace('-', ' ').title()

        profile = f"""# {client_display} - Client Profile
**For Use by Claude Skills & Automation**

**Created:** {today}
**Last Updated:** {today}
**Status:** Active Client
**Generated By:** sidekick-profile-builder

---

## 1. Business Core

| Field | Value | Source |
|-------|-------|--------|
| **Client Name** | {get_val('client_name', client_display)} | {get_source('client_name') or 'inferred'} |
| **Legal Name** | {get_val('legal_name')} | {get_source('legal_name')} |
| **DBA** | {get_val('dba')} | {get_source('dba')} |
| **Industry** | {get_val('industry')} | {get_source('industry')} |
| **Website** | {get_val('website')} | {get_source('website')} |
| **Address** | {get_val('location')} | {get_source('location')} |
| **Service Area** | {get_val('service_area')} | {get_source('service_area')} |
| **Founded** | {get_val('founded_year')} | {get_source('founded_year')} |
| **Company Size** | {get_val('company_size')} | {get_source('company_size')} |
| **Hours** | {get_val('hours_of_operation')} | {get_source('hours_of_operation')} |

---

## 2. Contacts

| Role | Name | Email | Phone | Source |
|------|------|-------|-------|--------|
| **Primary Contact** | {get_val('contact_primary')} | {get_val('contact_primary_email')} | {get_val('contact_primary_phone')} | {get_source('contact_primary')} |
| **Secondary Contact** | {get_val('contact_secondary')} | - | - | {get_source('contact_secondary')} |
| **Decision Maker** | {get_val('decision_maker')} | - | - | {get_source('decision_maker')} |
| **Billing Contact** | {get_val('billing_contact')} | - | - | {get_source('billing_contact')} |

**Contact Preferences:** [NEEDS MANUAL INPUT - e.g., Email preferred, response within 24hrs]

---

## 3. Target Audience

### Demographics
{get_val('demographics', '[NEEDS MANUAL INPUT]')}

### Psychographics
{get_val('psychographics', '[NEEDS MANUAL INPUT]')}

### Audience Segments
{get_val('customer_segments_section', get_val('target_audience_section', get_val('target_audience', '[NEEDS MANUAL INPUT]')))}

### Customer Journey
{get_val('customer_journey_section', '[NEEDS MANUAL INPUT]')}

### Common Objections
{get_val('objections_section', '[NEEDS MANUAL INPUT]')}

**Source:** {get_source('target_audience_section') or get_source('target_audience') or 'not found'}

---

## 4. Brand Voice

### Tone & Personality
{get_val('brand_voice_section', get_val('brand_tone', '[NEEDS MANUAL INPUT]'))}

### Words to Use
{get_val('brand_words_use', '[NEEDS MANUAL INPUT]')}

### Words to Avoid
{get_val('brand_words_avoid', '[NEEDS MANUAL INPUT]')}

### Brand Voice Examples
[NEEDS MANUAL INPUT - Copy examples of on-brand messaging]

**Source:** {get_source('brand_voice_section') or get_source('brand_tone') or 'not found'}

---

## 5. Products & Services

{get_val('products_section', '[NEEDS MANUAL INPUT]')}

| Service/Product | Priority | Seasonality | Price Point | Landing Page |
|-----------------|----------|-------------|-------------|--------------|
| {get_val('primary_service', '[Service 1]')} | Primary | Year-round | - | - |
| [Service 2] | Secondary | - | - | - |
| [Service 3] | Tertiary | - | - | - |

**Source:** {get_source('products_section') or get_source('primary_service') or 'not found'}

---

## 6. Content Pillars

{get_val('content_pillars_section', '[NEEDS MANUAL INPUT]')}

| Pillar | Purpose | % of Mix | Topics | Best Format |
|--------|---------|----------|--------|-------------|
| Promo | Drive conversions | 20% | - | - |
| Proof | Build trust | 30% | - | - |
| People | Humanize brand | 20% | - | - |
| Tips | Provide value | 20% | - | - |
| Fun | Engagement | 10% | - | - |

**Source:** {get_source('content_pillars_section') or 'not found'}

---

## 7. SOW/Deliverables

### Contract Overview
| Field | Value |
|-------|-------|
| **Contract Start** | {get_val('contract_start')} |
| **Contract End** | {get_val('contract_end')} |
| **Monthly Retainer** | ${get_val('monthly_retainer')} |
| **Ad Budget** | [NEEDS INPUT - separate from retainer] |

### Social Media Deliverables
| Platform | Posts/Month | Format | Notes |
|----------|-------------|--------|-------|
| Instagram | {get_val('instagram_posts', '?')} | - | - |
| Facebook | {get_val('facebook_posts', '?')} | - | - |
| GBP | {get_val('gbp_posts', '?')} | - | - |

### Other Services
{get_val('sow_section', '[NEEDS MANUAL INPUT]')}

**Source:** {get_source('sow_section') or 'not found'}

---

## 8. KPIs & Goals

### Business Goals
{get_val('kpis_section', '[NEEDS MANUAL INPUT]')}

### Platform Metrics

| Platform | Metric | Baseline | Target | Stretch |
|----------|--------|----------|--------|---------|
| Instagram | Engagement Rate | - | - | - |
| Facebook | Avg Clicks/Post | - | - | - |
| GBP | Monthly Views | - | - | - |
| Google | Reviews Count | - | - | - |

### Success Definition
[NEEDS MANUAL INPUT - What does success look like for this client?]

**Source:** {get_source('kpis_section') or 'not found'}

---

## 9. Competitors

{get_val('competitors_section', '[NEEDS MANUAL INPUT]')}

| Competitor | Website | Strengths | Weaknesses | Our Differentiation |
|------------|---------|-----------|------------|---------------------|
| [Competitor 1] | - | - | - | - |
| [Competitor 2] | - | - | - | - |
| [Competitor 3] | - | - | - | - |

**Source:** {get_source('competitors_section') or 'not found'}

---

## 10. Seasonality & Calendar

{get_val('seasonality_section', '[NEEDS MANUAL INPUT]')}

### Business Seasons
| Season | Peak/Low | Notes |
|--------|----------|-------|
| Q1 (Jan-Mar) | - | - |
| Q2 (Apr-Jun) | - | - |
| Q3 (Jul-Sep) | - | - |
| Q4 (Oct-Dec) | - | - |

### Key Events & Holidays
[NEEDS MANUAL INPUT - Important dates for content]

### Blackout Periods
[NEEDS MANUAL INPUT - Times to avoid certain content]

**Source:** {get_source('seasonality_section') or 'not found'}

---

## 11. Visual Brand

{get_val('visual_brand_section', '')}

### Brand Colors
{get_val('brand_colors', '[NEEDS MANUAL INPUT]')}

| Color | Hex | Usage |
|-------|-----|-------|
| Primary | - | - |
| Secondary | - | - |
| Accent | - | - |

### Typography
[NEEDS MANUAL INPUT - Fonts and usage]

### Logo Usage
{get_val('logo_usage', '[NEEDS MANUAL INPUT]')}

### Image Style
[NEEDS MANUAL INPUT - Photography/graphic style]

**Source:** {get_source('visual_brand_section') or get_source('brand_colors') or 'not found'}

---

## 12. Account Access

{get_val('account_access_section', '')}

| Platform | Handle/URL | Followers | Eng. Rate | Notes |
|----------|------------|-----------|-----------|-------|
| Instagram | {get_val('instagram_handle', '-')} | - | - | - |
| Facebook | {get_val('facebook_page', '-')} | - | - | - |
| GBP | {get_val('gbp_listing', '-')} | N/A | N/A | - |
| LinkedIn (Company) | {get_val('linkedin', '-')} | - | - | - |
| LinkedIn (Founder) | - | - | - | - |
| Twitter/X | {get_val('twitter', '-')} | - | - | - |
| YouTube | {get_val('youtube', '-')} | - | - | - |
| TikTok | {get_val('tiktok', '-')} | - | - | - |

**Credentials Location:** [1Password/LastPass/etc.]

**Source:** {get_source('account_access_section') or 'inferred from content'}

---

## 13. Guidelines & Constraints

{get_val('guidelines_section', '[NEEDS MANUAL INPUT]')}

### Legal/Compliance Requirements
[NEEDS MANUAL INPUT - Industry regulations, disclaimers required]

### Approval Workflow
[NEEDS MANUAL INPUT - Who approves content? Turnaround time?]

### Topics to Avoid
[NEEDS MANUAL INPUT - Sensitive subjects, competitors not to mention]

### Community Management
|| Field | Value |
||-------|-------|
|| **Response Time** | [NEEDS INPUT - e.g., within 24 hours] |
|| **Who Handles DMs/Comments** | [NEEDS INPUT - client / agency / both] |
|| **Negative Review Protocol** | [NEEDS INPUT - respond / ignore / escalate] |

**Source:** {get_source('guidelines_section') or 'not found'}

---

## 14. Business Model & Revenue

{get_val('business_model_section', '')}

### Revenue Streams
[NEEDS MANUAL INPUT - How do they make money?]

### Key Financial Metrics
| Metric | Value |
|--------|-------|
| **Average Transaction Value** | {get_val('average_transaction', '[NEEDS INPUT]')} |
| **Customer Lifetime Value** | {get_val('customer_ltv', '[NEEDS INPUT]')} |

### Lead Sources
{get_val('lead_sources_section', get_val('lead_source', '[NEEDS MANUAL INPUT - Where do leads come from?]'))}

**Source:** {get_source('business_model_section') or get_source('lead_source') or 'not found'}

---

## 15. Origin Story

{get_val('origin_story_section', '')}

### Founder Background
| Field | Value |
|-------|-------|
| **Founder Name** | {get_val('founder_name', '[NEEDS INPUT]')} |
| **Year Founded** | {get_val('founded_year', '[NEEDS INPUT]')} |

### The "Why" Story
{get_val('mission_section', get_val('why_started', '[NEEDS MANUAL INPUT - Why did they start this business?]'))}

### Key Milestones
{get_val('milestones_section', '[NEEDS MANUAL INPUT]')}

**Source:** {get_source('origin_story_section') or get_source('founder_name') or 'not found'}

---

## 16. Local Presence & Reputation

{get_val('reviews_section', '')}

### Review Status
| Platform | Rating | # Reviews |
|----------|--------|-----------|
| **Google** | {get_val('google_rating', '-')} | {get_val('google_review_count', '-')} |
| **Yelp** | {get_val('yelp_rating', '-')} | - |
| **Facebook** | - | - |

### Community Involvement
{get_val('community_section', '[NEEDS MANUAL INPUT - Sponsorships, local partnerships, etc.]')}

### Local Partnerships
{get_val('partnerships_section', '[NEEDS MANUAL INPUT]')}

**Source:** {get_source('reviews_section') or get_source('google_rating') or 'not found'}

---

## 17. Marketing History

{get_val('marketing_history_section', '')}

### Past Marketing Efforts
[NEEDS MANUAL INPUT - What have they tried before?]

### What's Worked Before
{get_val('what_worked_section', '[NEEDS MANUAL INPUT]')}

### What Flopped
{get_val('what_flopped_section', '[NEEDS MANUAL INPUT]')}

### Previous Agencies/Vendors
{get_val('previous_agency', '[NEEDS MANUAL INPUT - Who did they work with before? Why did they leave?]')}

### Historical Ad Spend
{get_val('past_ad_spend', '[NEEDS MANUAL INPUT]')}

**Source:** {get_source('marketing_history_section') or get_source('previous_agency') or 'not found'}

---

## 18. Content Bank & Assets

{get_val('content_bank_section', '')}

### Photo Library
{get_val('media_assets_section', '[NEEDS MANUAL INPUT - What photos/videos exist?]')}

### Testimonials & Social Proof
{get_val('testimonials_section', get_val('has_testimonials', '[NEEDS MANUAL INPUT]'))}

### FAQs & Common Questions
{get_val('faq_section', get_val('faq_item', '[NEEDS MANUAL INPUT - What do customers always ask?]'))}

### Staff Bios
[NEEDS MANUAL INPUT - Key team members for content]

### Content Creation Capability
|| Capability | Status |
||------------|--------|
|| Client can shoot photos | [ ] Yes / [ ] No |
|| Client can shoot video | [ ] Yes / [ ] No |
|| Professional photographer | [ ] Available / [ ] Not available |
|| Existing photo library | [NEEDS INPUT - quantity, quality] |

### UGC Sources
[NEEDS MANUAL INPUT - Customer/employee accounts that create content]

**Source:** {get_source('content_bank_section') or get_source('testimonials_section') or 'not found'}

---

## 19. Email & CRM

{get_val('email_section', '')}

### Email Marketing
| Field | Value |
|-------|-------|
| **Platform** | {get_val('email_platform', '[NEEDS INPUT]')} |
| **List Size** | {get_val('email_list_size', '[NEEDS INPUT]')} |

### CRM System
| Field | Value |
|-------|-------|
| **Platform** | {get_val('crm_platform', '[NEEDS INPUT]')} |

{get_val('crm_section', '')}

### Integration Opportunities
[NEEDS MANUAL INPUT - How can we connect systems?]

**Source:** {get_source('email_section') or get_source('email_platform') or 'not found'}

---

## 20. Relationship Notes

{get_val('relationship_section', '')}

### Communication Preferences
| Preference | Detail |
|------------|--------|
| **Preferred Method** | {get_val('communication_preference', '[NEEDS INPUT]')} |
| **Meeting Cadence** | {get_val('meeting_cadence', '[NEEDS INPUT]')} |

{get_val('communication_section', '')}

### Working Style
{get_val('working_style_section', '[NEEDS MANUAL INPUT - How do they like to work?]')}

### What Makes Them Happy
[NEEDS MANUAL INPUT - Document over time]

### Pet Peeves / Avoid
[NEEDS MANUAL INPUT - Document over time]

### Internal Notes
> [Any context that helps the team work better with this client]

**Source:** {get_source('relationship_section') or get_source('communication_preference') or 'not found'}

---

## Build Metadata

| Metric | Value |
|--------|-------|
| Files Processed | {len(self.scan_files())} |
| Fields Extracted | {len(data)} |
| Conflicts Detected | {len(self.conflicts)} |
| Gaps Remaining | {len(self.gaps)} |
| Build Date | {today} |

---

**Review the `_conflicts.md` and `_gaps.md` files to complete this profile.**
"""

        output_path = self.client_folder / f"00_{self.client_name}_CLIENT_PROFILE.md"
        with open(output_path, 'w') as f:
            f.write(profile)

    def _generate_extraction_audit(self, data: dict):
        """Generate detailed audit of what was extracted and from where."""
        audit = f"""# Extraction Audit Report
**Client:** {self.client_name}
**Generated:** {datetime.now().isoformat()}
**Files Processed:** {len(self.scan_files())}

---

## Extraction Summary

| Field | Value Preview | Source | Confidence | Alternatives |
|-------|---------------|--------|------------|--------------|
"""
        for field, info in sorted(data.items()):
            value_preview = info['value'][:50].replace('\n', ' ') + '...' if len(info['value']) > 50 else info['value'].replace('\n', ' ')
            audit += f"| {field} | {value_preview} | {info['source']} | {info['confidence']:.0%} | {info['alternatives']} |\n"

        audit += f"""
---

## All Extracted Data Points

"""
        for field, items in sorted(self.extracted.items()):
            audit += f"### {field}\n\n"
            for item in items[:10]:  # Limit to 10 per field
                value_short = item['value'][:100].replace('\n', ' ')
                audit += f"- **{item['source']}** (line {item['line']}, conf: {item['confidence']:.0%})\n"
                audit += f"  `{value_short}`\n\n"
            if len(items) > 10:
                audit += f"*... and {len(items) - 10} more*\n\n"

        with open(self.audit_dir / "_extraction_audit.md", 'w') as f:
            f.write(audit)

    def _generate_conflicts_report(self):
        """Generate report of conflicting data that needs human review."""
        if not self.conflicts:
            return

        report = f"""# Data Conflicts Report
**Client:** {self.client_name}
**Generated:** {datetime.now().isoformat()}

These fields have conflicting values from different sources. Please review and resolve.

---

"""
        for conflict in self.conflicts:
            report += f"## {conflict['field']}\n\n"
            for i, item in enumerate(conflict['values'], 1):
                report += f"**Option {i}** (from `{item['source']}`):\n"
                report += f"```\n{item['value']}\n```\n\n"
            report += "---\n\n"

        with open(self.audit_dir / "_conflicts.md", 'w') as f:
            f.write(report)

    def _generate_gaps_report(self):
        """Generate report of missing fields."""
        if not self.gaps:
            return

        report = f"""# Data Gaps Report
**Client:** {self.client_name}
**Generated:** {datetime.now().isoformat()}

The following fields could not be extracted from the source files.
Please add this information manually to the client profile.

---

## Missing Fields

"""
        for gap in self.gaps:
            report += f"- [ ] **{gap}**\n"

        report += """
---

## How to Fix

1. Open the client profile: `00_{{CLIENT}}_CLIENT_PROFILE.md`
2. Find sections marked `[NEEDS MANUAL INPUT]`
3. Fill in the missing information
4. Remove the `[NEEDS MANUAL INPUT]` placeholder

"""

        with open(self.audit_dir / "_gaps.md", 'w') as f:
            f.write(report)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build client profile from Notion exports + web")
    parser.add_argument('--client-folder', required=True, help="Path to client folder")
    parser.add_argument('--additional-folders', nargs='*', default=[],
                        help="Additional folders to scan (beyond notion_export)")
    parser.add_argument('--urls', nargs='*', default=[],
                        help="URLs to fetch (client website, social profiles, GBP)")
    args = parser.parse_args()

    builder = ProfileBuilder(args.client_folder, args.additional_folders, args.urls)
    builder.build()
