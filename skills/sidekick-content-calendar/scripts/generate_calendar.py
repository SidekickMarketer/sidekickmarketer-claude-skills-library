#!/usr/bin/env python3
"""
Content Calendar Generator - Sidekick Content Calendar Skill

Generates a monthly content calendar CSV structure with:
- All posting dates based on frequency targets
- Pillar distribution matching strategy percentages
- Platform-specific format assignments
- Placeholder topics ready for ideation

Usage:
    python generate_calendar.py --client-folder "/path/to/client" --month 2025-02
    python generate_calendar.py --client-folder "/path/to/client" --month 2025-02 --strategy "/path/to/strategy.md"
"""

import argparse
import csv
import json
import re
from datetime import datetime, timedelta
from pathlib import Path
from collections import defaultdict
import calendar


class CalendarGenerator:
    """Generates content calendar CSV from strategy inputs."""

    # Default posting schedule (days of week: 0=Monday, 6=Sunday)
    DEFAULT_POSTING_DAYS = {
        'instagram': [0, 2, 4],  # Mon, Wed, Fri
        'facebook': [0, 2, 3],   # Mon, Wed, Thu
        'gbp': [1, 3],           # Tue, Thu
    }

    # Default pillars if strategy not found
    DEFAULT_PILLARS = {
        'Educational': 30,
        'Social Proof': 25,
        'Behind the Scenes': 20,
        'Community': 15,
        'Promotional': 10,
    }

    # Format distribution (photo-first model)
    FORMAT_DISTRIBUTION = {
        'instagram': {'Carousel': 55, 'Single Image': 35, 'Reel': 10},
        'facebook': {'Single Image': 60, 'Carousel': 30, 'Link Post': 10},
        'gbp': {'Update': 70, 'Offer': 20, 'Event': 10},
    }

    def __init__(self, client_folder: str, month: str, strategy_path: str = None):
        self.client_folder = Path(client_folder)
        self.month = datetime.strptime(month, '%Y-%m')
        self.strategy_path = Path(strategy_path) if strategy_path else None

        # Will be populated from strategy or defaults
        self.pillars = {}
        self.platforms = {}
        self.posting_days = {}

        # Output paths - per-channel structure
        self.base_output_dir = self.client_folder / "07_Marketing_Channels" / "Social_Media"

    def load_strategy(self):
        """Load strategy from file or use defaults."""
        strategy_file = None

        # Try to find strategy file
        if self.strategy_path and self.strategy_path.exists():
            strategy_file = self.strategy_path
        else:
            # Look in standard locations
            candidates = [
                self.client_folder / "07_Marketing_Channels" / "Social_Media" / "00_MASTER_STRATEGY.md",
                self.client_folder / "07_Marketing_Channels" / "Social_Media" / "00_SOCIAL_STRATEGY.md",
                self.client_folder / "SOCIAL_STRATEGY.md",
            ]
            for candidate in candidates:
                if candidate.exists():
                    strategy_file = candidate
                    break

        if strategy_file:
            print(f"  📄 Loading strategy: {strategy_file.name}")
            self._parse_strategy(strategy_file)
        else:
            print("  ⚠️ No strategy file found, using defaults")
            self.pillars = self.DEFAULT_PILLARS.copy()
            self.platforms = {
                'instagram': {'frequency': 4, 'priority': 'Primary'},
                'facebook': {'frequency': 3, 'priority': 'Secondary'},
                'gbp': {'frequency': 2, 'priority': 'Secondary'},
            }
            self.posting_days = self.DEFAULT_POSTING_DAYS.copy()

    def _parse_strategy(self, strategy_file: Path):
        """Extract pillars and platform info from strategy markdown."""
        try:
            content = strategy_file.read_text()

            # Extract pillars from table
            pillar_pattern = r'\|\s*([^|]+)\s*\|\s*(\d+)%\s*\|'
            pillar_matches = re.findall(pillar_pattern, content)

            if pillar_matches:
                for name, pct in pillar_matches:
                    name = name.strip()
                    if name and not name.startswith('Pillar') and not name.startswith('-'):
                        self.pillars[name] = int(pct)

            # Normalize to 100%
            if self.pillars:
                total = sum(self.pillars.values())
                if total != 100:
                    for k in self.pillars:
                        self.pillars[k] = round(self.pillars[k] * 100 / total)
            else:
                self.pillars = self.DEFAULT_PILLARS.copy()

            # Extract platform frequencies
            platform_pattern = r'\|\s*(Instagram|Facebook|Google Business Profile|GBP)\s*\|[^|]*\|[^|]*\|\s*(\d+)[^|]*\|'
            platform_matches = re.findall(platform_pattern, content, re.IGNORECASE)

            self.platforms = {}
            for platform, freq in platform_matches:
                key = platform.lower()
                if 'google' in key or key == 'gbp':
                    key = 'gbp'
                self.platforms[key] = {'frequency': int(freq), 'priority': 'Primary'}

            if not self.platforms:
                self.platforms = {
                    'instagram': {'frequency': 4, 'priority': 'Primary'},
                    'facebook': {'frequency': 3, 'priority': 'Secondary'},
                    'gbp': {'frequency': 2, 'priority': 'Secondary'},
                }

            self.posting_days = self.DEFAULT_POSTING_DAYS.copy()

        except Exception as e:
            print(f"  ⚠️ Error parsing strategy: {e}")
            self.pillars = self.DEFAULT_PILLARS.copy()
            self.platforms = {
                'instagram': {'frequency': 4, 'priority': 'Primary'},
                'facebook': {'frequency': 3, 'priority': 'Secondary'},
                'gbp': {'frequency': 2, 'priority': 'Secondary'},
            }
            self.posting_days = self.DEFAULT_POSTING_DAYS.copy()

    def get_month_dates(self):
        """Get all dates in the target month."""
        year = self.month.year
        month = self.month.month
        num_days = calendar.monthrange(year, month)[1]

        dates = []
        for day in range(1, num_days + 1):
            dates.append(datetime(year, month, day))
        return dates

    def assign_posting_dates(self, platform: str, frequency_per_week: int):
        """Assign posting dates for a platform based on frequency."""
        all_dates = self.get_month_dates()
        posting_days = self.posting_days.get(platform, [0, 2, 4])

        # Get all eligible dates (matching posting days)
        eligible_dates = [d for d in all_dates if d.weekday() in posting_days]

        # If frequency is higher than eligible days, add more days
        num_weeks = len(all_dates) // 7 + 1
        target_posts = frequency_per_week * num_weeks

        if len(eligible_dates) < target_posts:
            # Add more dates as needed
            remaining = [d for d in all_dates if d not in eligible_dates]
            remaining.sort(key=lambda x: x.weekday())  # Prefer start of week
            eligible_dates.extend(remaining[:target_posts - len(eligible_dates)])

        # Take the number we need, evenly distributed
        eligible_dates.sort()
        step = max(1, len(eligible_dates) // target_posts)
        selected = eligible_dates[::step][:target_posts]

        return sorted(selected)

    def distribute_pillars(self, num_posts: int):
        """Distribute pillars across posts based on percentages."""
        distribution = []

        for pillar, pct in self.pillars.items():
            count = round(num_posts * pct / 100)
            distribution.extend([pillar] * count)

        # Pad or trim to exact count
        while len(distribution) < num_posts:
            distribution.append(list(self.pillars.keys())[0])
        distribution = distribution[:num_posts]

        # Shuffle to avoid clustering
        import random
        random.seed(42)  # Reproducible
        random.shuffle(distribution)

        return distribution

    def assign_formats(self, platform: str, num_posts: int):
        """Assign content formats based on platform distribution."""
        dist = self.FORMAT_DISTRIBUTION.get(platform, {'Single Image': 100})
        formats = []

        for fmt, pct in dist.items():
            count = round(num_posts * pct / 100)
            formats.extend([fmt] * count)

        # Pad or trim
        while len(formats) < num_posts:
            formats.append(list(dist.keys())[0])
        formats = formats[:num_posts]

        return formats

    def generate(self):
        """Generate the content calendar."""
        print(f"\n📅 Generating calendar for {self.month.strftime('%B %Y')}")
        print("=" * 50)

        self.load_strategy()

        print(f"\n  Pillars: {', '.join(f'{k} ({v}%)' for k, v in self.pillars.items())}")
        print(f"  Platforms: {', '.join(f'{k} ({v['frequency']}/week)' for k, v in self.platforms.items())}")

        # Generate posts for each platform
        all_posts = []

        for platform, config in self.platforms.items():
            dates = self.assign_posting_dates(platform, config['frequency'])
            pillars = self.distribute_pillars(len(dates))
            formats = self.assign_formats(platform, len(dates))

            for i, date in enumerate(dates):
                post = {
                    'Date': date.strftime('%Y-%m-%d'),
                    'Day': date.strftime('%a'),
                    'Platform': platform.title() if platform != 'gbp' else 'GBP',
                    'Format': formats[i],
                    'Pillar': pillars[i],
                    'Topic': f"[{pillars[i]} topic - {formats[i]}]",
                    'Caption_Outline': "Hook: [TBD] | Body: [TBD] | CTA: [TBD]",
                    'Visual_Direction': "[TBD - describe photo/graphic needed]",
                    'Hashtags': self._default_hashtags(platform),
                    'Status': 'Draft',
                }
                all_posts.append(post)

        # Sort by date
        all_posts.sort(key=lambda x: (x['Date'], x['Platform']))

        # Write per-channel calendars
        platform_map = {
            'Instagram': 'Instagram',
            'Facebook': 'Facebook',
            'GBP': 'GBP',
        }
        
        for platform_display, folder_name in platform_map.items():
            platform_posts = [p for p in all_posts if p['Platform'] == platform_display]
            if not platform_posts:
                continue
                
            # Create per-channel output directory
            channel_dir = self.base_output_dir / folder_name / "Content_Calendars"
            channel_dir.mkdir(parents=True, exist_ok=True)
            
            # Platform abbreviation for filenames
            abbrev = {'Instagram': 'IG', 'Facebook': 'FB', 'GBP': 'GBP'}[platform_display]
            
            # Write CSV
            csv_path = channel_dir / f"{self.month.strftime('%Y-%m')}_{abbrev}_Calendar.csv"
            self._write_csv(platform_posts, csv_path)
            
            # Write brief
            brief_path = channel_dir / f"{self.month.strftime('%Y-%m')}_{abbrev}_Brief.md"
            self._write_brief(platform_posts, brief_path, platform_display)
            
            print(f"   ✅ {platform_display}: {len(platform_posts)} posts → {csv_path.name}")

        print(f"\n✅ Calendar generated!")
        print(f"   📝 Total posts: {len(all_posts)}")

        return all_posts

    def _default_hashtags(self, platform: str):
        """Return placeholder hashtags by platform."""
        if platform == 'gbp':
            return ""
        elif platform == 'facebook':
            return "#[branded] #[local]"
        else:
            return "#[branded] #[niche1] #[niche2] #[local1] #[local2]"

    def _write_csv(self, posts: list, path: Path):
        """Write posts to CSV file."""
        fieldnames = ['Date', 'Day', 'Platform', 'Format', 'Pillar', 'Topic',
                      'Caption_Outline', 'Visual_Direction', 'Hashtags', 'Status']

        with open(path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(posts)

    def _write_brief(self, posts: list, path: Path, platform: str = None):
        """Write calendar brief markdown."""
        # Calculate stats
        platform_counts = defaultdict(lambda: {'total': 0, 'formats': defaultdict(int)})
        pillar_counts = defaultdict(int)

        for post in posts:
            plat = post['Platform']
            platform_counts[plat]['total'] += 1
            platform_counts[plat]['formats'][post['Format']] += 1
            pillar_counts[post['Pillar']] += 1

        total_posts = len(posts)
        
        platform_label = f" - {platform}" if platform else ""

        brief = f"""# Content Calendar Brief - {self.month.strftime('%B %Y')}{platform_label}

## Month Overview
- **Total Posts:** {total_posts}
- **Primary Theme:** [Define monthly theme]
- **Key Dates:** [List special dates]

## Weekly Themes
- Week 1: [Theme]
- Week 2: [Theme]
- Week 3: [Theme]
- Week 4: [Theme]
- Week 5: [Theme if applicable]

## Pillar Distribution

| Pillar | Target | Actual | Status |
|--------|--------|--------|--------|
"""
        for pillar, target_pct in self.pillars.items():
            actual = pillar_counts.get(pillar, 0)
            actual_pct = round(actual / total_posts * 100) if total_posts > 0 else 0
            status = "✅" if abs(actual_pct - target_pct) <= 5 else "⚠️"
            brief += f"| {pillar} | {target_pct}% | {actual_pct}% ({actual}) | {status} |\n"

        brief += f"""
## Platform Breakdown

| Platform | Total | """

        # Get all unique formats
        all_formats = set()
        for p in platform_counts.values():
            all_formats.update(p['formats'].keys())
        all_formats = sorted(all_formats)

        brief += " | ".join(all_formats) + " |\n"
        brief += "|----------|-------|" + "|".join(["-------"] * len(all_formats)) + "|\n"

        for platform, data in platform_counts.items():
            row = f"| {platform} | {data['total']} |"
            for fmt in all_formats:
                row += f" {data['formats'].get(fmt, 0)} |"
            brief += row + "\n"

        brief += """
## Special Content Notes
- [Date]: [Special content for event/holiday]
- [Date]: [Promotional push]

## Action Items
- [ ] Fill in all [TBD] topics
- [ ] Complete caption outlines
- [ ] Specify visual directions
- [ ] Add hashtag sets
- [ ] Review pillar balance

---
*Generated by sidekick-content-calendar*
"""

        with open(path, 'w', encoding='utf-8') as f:
            f.write(brief)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate content calendar CSV')
    parser.add_argument('--client-folder', required=True, help='Path to client folder')
    parser.add_argument('--month', required=True, help='Target month (YYYY-MM format)')
    parser.add_argument('--strategy', help='Path to strategy file (optional)')

    args = parser.parse_args()

    generator = CalendarGenerator(
        client_folder=args.client_folder,
        month=args.month,
        strategy_path=args.strategy
    )
    generator.generate()
