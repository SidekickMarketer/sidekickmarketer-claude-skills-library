#!/usr/bin/env python3
"""
Validate Client Profile Completeness
Checks if profile is ready for downstream skills (social audit, strategy, etc.)
"""
import argparse
import re
from pathlib import Path
from typing import Dict, List, Tuple

# Incomplete markers to detect (actual placeholders only, not source columns)
INCOMPLETE_MARKERS = [
    '[NEEDS MANUAL INPUT]',
    '[NEEDS INPUT]',
    '[NOT FOUND]',
    '[NOT FINAL]',
]

# Patterns that indicate empty VALUE cells (not source columns)
# These are less aggressive and won't count source column dashes as incomplete
EMPTY_VALUE_PATTERNS = [
    r'\|\s*\*\*[^|]+\*\*\s*\|\s*-\s*\|',  # | **Field** | - | (empty value in bold field row)
    r'\|\s*-\s*\|\s*-\s*\|\s*-\s*\|',      # | - | - | - | (all empty row)
]

# Section definitions with requirements for downstream skills
SECTIONS = {
    1: {
        'name': 'Business Core',
        'required_for': ['social_audit', 'strategy', 'reporting'],
        'key_fields': ['Client Name', 'Industry', 'Website', 'Address'],
        'priority': 'required'
    },
    2: {
        'name': 'Contacts',
        'required_for': ['all'],
        'key_fields': ['Primary Contact'],
        'priority': 'required'
    },
    3: {
        'name': 'Target Audience',
        'required_for': ['strategy', 'content'],
        'key_fields': ['Demographics', 'Psychographics'],
        'priority': 'required'
    },
    4: {
        'name': 'Brand Voice',
        'required_for': ['social_audit', 'content', 'strategy'],
        'key_fields': ['Tone', 'Personality', 'Words to Use', 'Words to Avoid'],
        'priority': 'required'
    },
    5: {
        'name': 'Products & Services',
        'required_for': ['strategy', 'content'],
        'key_fields': ['Service/Product'],
        'priority': 'required'
    },
    6: {
        'name': 'Content Pillars',
        'required_for': ['social_audit', 'content', 'strategy'],
        'key_fields': ['Pillar', '% of Mix'],
        'priority': 'required'
    },
    7: {
        'name': 'SOW/Deliverables',
        'required_for': ['social_audit', 'reporting'],
        'key_fields': ['Contract', 'Retainer', 'Platform'],  # More flexible matching
        'priority': 'required'
    },
    8: {
        'name': 'KPIs & Goals',
        'required_for': ['social_audit', 'reporting', 'strategy'],
        'key_fields': ['Metric', 'Baseline', 'Target'],
        'priority': 'required'
    },
    9: {
        'name': 'Competitors',
        'required_for': ['strategy'],
        'key_fields': ['Competitor', 'Website'],
        'priority': 'required'
    },
    10: {
        'name': 'Seasonality & Calendar',
        'required_for': ['strategy', 'content'],
        'key_fields': ['Peak', 'Q1', 'Q3'],  # More flexible matching for seasons
        'priority': 'required'
    },
    11: {
        'name': 'Visual Brand',
        'required_for': ['content'],
        'key_fields': ['Primary', 'Hex'],
        'priority': 'required'
    },
    12: {
        'name': 'Account Access',
        'required_for': ['social_audit', 'content'],
        'key_fields': ['Instagram', 'Facebook', 'Handle'],
        'priority': 'required'
    },
    13: {
        'name': 'Guidelines & Constraints',
        'required_for': ['content', 'strategy'],
        'key_fields': ['Approval', 'Topics to Avoid'],
        'priority': 'required'
    },
    14: {
        'name': 'Business Model & Revenue',
        'required_for': ['strategy'],
        'key_fields': ['Revenue', 'Lead Sources'],
        'priority': 'recommended'
    },
    15: {
        'name': 'Origin Story',
        'required_for': ['content'],
        'key_fields': ['Founder', 'Why'],
        'priority': 'recommended'
    },
    16: {
        'name': 'Local Presence & Reputation',
        'required_for': ['social_audit', 'strategy'],
        'key_fields': ['Google', 'Rating', 'Reviews'],
        'priority': 'recommended'
    },
    17: {
        'name': 'Marketing History',
        'required_for': ['strategy'],
        'key_fields': ['What Worked', 'Previous'],
        'priority': 'recommended'
    },
    18: {
        'name': 'Content Bank & Assets',
        'required_for': ['content'],
        'key_fields': ['Photo', 'Testimonials', 'FAQs'],
        'priority': 'recommended'
    },
    19: {
        'name': 'Email & CRM',
        'required_for': ['strategy'],
        'key_fields': ['Platform', 'List Size'],
        'priority': 'recommended'
    },
    20: {
        'name': 'Relationship Notes',
        'required_for': [],
        'key_fields': ['Communication', 'Working Style'],
        'priority': 'optional'
    },
}

# Skill requirements - what sections must be complete
SKILL_REQUIREMENTS = {
    'social_audit': {
        'name': 'Social Audit',
        'critical': [4, 6, 7, 8, 12],  # Brand voice, pillars, SOW, KPIs, accounts
        'recommended': [1, 16],  # Business core, local presence
        'description': 'Audit social media performance against goals'
    },
    'strategy': {
        'name': 'Strategy Development',
        'critical': [1, 3, 4, 5, 6, 8, 9, 10],
        'recommended': [14, 17],
        'description': 'Develop marketing strategy'
    },
    'content': {
        'name': 'Content Creation',
        'critical': [4, 5, 6, 11, 12, 13],
        'recommended': [3, 15, 18],
        'description': 'Create social content'
    },
    'reporting': {
        'name': 'Performance Reporting',
        'critical': [1, 7, 8],
        'recommended': [2],
        'description': 'Generate performance reports'
    },
    'linkedin_voice': {
        'name': 'LinkedIn Voice Capture',
        'critical': [2, 4, 15],  # Contacts, Brand Voice, Origin Story
        'recommended': [20],  # Relationship notes
        'description': 'Capture founder voice for LinkedIn ghostwriting'
    },
    'linkedin_profile': {
        'name': 'LinkedIn Profile Optimizer',
        'critical': [1, 2, 3, 4, 5, 9, 15],  # Core, contacts, audience, voice, services, competitors, origin
        'recommended': [11],  # Visual brand
        'description': 'Optimize LinkedIn profiles (founder + company)'
    },
    'linkedin_strategy': {
        'name': 'LinkedIn Strategy Creator',
        'critical': [1, 3, 4, 5, 7, 8, 9, 10, 13],  # Most sections needed
        'recommended': [12, 17],  # Accounts, marketing history
        'description': 'Create comprehensive LinkedIn strategy'
    },
    'linkedin_content': {
        'name': 'LinkedIn Content Ideation',
        'critical': [4, 6, 9, 13, 15],  # Voice, pillars, competitors, guidelines, origin
        'recommended': [3, 18],  # Audience, content bank
        'description': 'Generate LinkedIn content ideas'
    },
    'linkedin_pillars': {
        'name': 'LinkedIn Content Pillars',
        'critical': [3, 4, 5, 8, 9],  # Audience, voice, services, goals, competitors
        'recommended': [10, 15],  # Seasonality, origin
        'description': 'Define LinkedIn-specific content pillars'
    }
}


class ProfileValidator:
    def __init__(self, profile_path: str):
        self.profile_path = Path(profile_path)
        self.content = ""
        self.sections = {}
        self.section_scores = {}

    def load(self) -> bool:
        """Load the profile file."""
        if not self.profile_path.exists():
            print(f"❌ Profile not found: {self.profile_path}")
            return False

        with open(self.profile_path, 'r', encoding='utf-8') as f:
            self.content = f.read()
        return True

    def parse_sections(self):
        """Split profile into sections."""
        # Find all section headers
        pattern = r'^## (\d+)\. (.+?)$'
        matches = list(re.finditer(pattern, self.content, re.MULTILINE))

        for i, match in enumerate(matches):
            section_num = int(match.group(1))
            section_name = match.group(2)

            # Get content until next section or end
            start = match.end()
            end = matches[i + 1].start() if i + 1 < len(matches) else len(self.content)
            section_content = self.content[start:end]

            self.sections[section_num] = {
                'name': section_name,
                'content': section_content
            }

    def score_section(self, section_num: int) -> Tuple[float, List[str]]:
        """
        Score a section's completeness (0-100%).
        Returns (score, list of issues).
        """
        if section_num not in self.sections:
            return 0.0, ["Section not found in profile"]

        content = self.sections[section_num]['content']
        issues = []

        # Check for incomplete markers (actual placeholders)
        incomplete_count = 0
        for marker in INCOMPLETE_MARKERS:
            count = content.count(marker)
            if count > 0:
                incomplete_count += count
                issues.append(f"Found '{marker}' ({count}x)")

        # Check for empty value cells using smarter patterns
        for pattern in EMPTY_VALUE_PATTERNS:
            matches = re.findall(pattern, content)
            if matches:
                incomplete_count += len(matches)

        # Check for key fields
        section_def = SECTIONS.get(section_num, {})
        key_fields = section_def.get('key_fields', [])
        fields_found = 0

        for field in key_fields:
            # Check if field exists with actual content (not just placeholder)
            if field.lower() in content.lower():
                # Check if there's actual data after the field
                # Handle both plain text and markdown bold formats: "Client Name:" or "**Client Name**"
                field_pattern = rf'\*?\*?{re.escape(field)}\*?\*?[:\s\|]+([^\|\n]+)'
                match = re.search(field_pattern, content, re.IGNORECASE)
                if match:
                    value = match.group(1).strip()
                    # Check if value is real data
                    is_placeholder = any(m in value for m in INCOMPLETE_MARKERS)
                    is_empty = value in ['-', '', '?', 'N/A']
                    if not is_placeholder and not is_empty and len(value) > 2:
                        fields_found += 1
                    else:
                        issues.append(f"'{field}' needs data")
                else:
                    issues.append(f"'{field}' needs data")

        # Calculate score
        if not key_fields:
            # No key fields defined, base on incomplete markers
            lines = content.count('\n')
            if lines == 0:
                return 0.0, ["Section is empty"]
            score = max(0, 100 - (incomplete_count * 10))
        else:
            field_score = (fields_found / len(key_fields)) * 70
            marker_penalty = min(30, incomplete_count * 5)
            score = max(0, field_score + (30 - marker_penalty))

        return min(100, score), issues

    def validate(self) -> dict:
        """Run full validation and return results."""
        if not self.load():
            return None

        self.parse_sections()

        results = {
            'profile_path': str(self.profile_path),
            'sections': {},
            'overall_score': 0,
            'required_score': 0,
            'recommended_score': 0,
            'skill_readiness': {},
            'blocking_issues': [],
            'warnings': []
        }

        required_scores = []
        recommended_scores = []

        # Score each section
        for section_num, section_def in SECTIONS.items():
            score, issues = self.score_section(section_num)
            self.section_scores[section_num] = score

            status = 'complete' if score >= 80 else 'partial' if score >= 40 else 'incomplete'

            results['sections'][section_num] = {
                'name': section_def['name'],
                'score': score,
                'status': status,
                'priority': section_def['priority'],
                'issues': issues
            }

            if section_def['priority'] == 'required':
                required_scores.append(score)
                if score < 50:
                    results['blocking_issues'].append(
                        f"Section {section_num} ({section_def['name']}) is incomplete"
                    )
            elif section_def['priority'] == 'recommended':
                recommended_scores.append(score)
                if score < 50:
                    results['warnings'].append(
                        f"Section {section_num} ({section_def['name']}) needs attention"
                    )

        # Calculate overall scores
        all_scores = list(self.section_scores.values())
        results['overall_score'] = sum(all_scores) / len(all_scores) if all_scores else 0
        results['required_score'] = sum(required_scores) / len(required_scores) if required_scores else 0
        results['recommended_score'] = sum(recommended_scores) / len(recommended_scores) if recommended_scores else 0

        # Check skill readiness
        for skill_id, skill_def in SKILL_REQUIREMENTS.items():
            critical_scores = [self.section_scores.get(s, 0) for s in skill_def['critical']]
            recommended_scores_skill = [self.section_scores.get(s, 0) for s in skill_def['recommended']]

            critical_avg = sum(critical_scores) / len(critical_scores) if critical_scores else 0
            critical_min = min(critical_scores) if critical_scores else 0

            # Skill is ready if all critical sections are at least 50%
            is_ready = all(s >= 50 for s in critical_scores)

            missing_sections = [
                f"{s}. {SECTIONS[s]['name']}"
                for s in skill_def['critical']
                if self.section_scores.get(s, 0) < 50
            ]

            results['skill_readiness'][skill_id] = {
                'name': skill_def['name'],
                'description': skill_def['description'],
                'ready': is_ready,
                'critical_score': critical_avg,
                'missing': missing_sections
            }

        return results

    def print_report(self, results: dict):
        """Print formatted validation report."""
        print("\n" + "=" * 60)
        print("📋 PROFILE VALIDATION REPORT")
        print("=" * 60)
        print(f"\nProfile: {Path(results['profile_path']).name}")

        # Overall scores
        print("\n📊 COMPLETION SCORES")
        print("-" * 40)
        overall = results['overall_score']
        required = results['required_score']
        recommended = results['recommended_score']

        print(f"   Overall:      {self._score_bar(overall)} {overall:.0f}%")
        print(f"   Required:     {self._score_bar(required)} {required:.0f}%")
        print(f"   Recommended:  {self._score_bar(recommended)} {recommended:.0f}%")

        # Skill readiness
        print("\n🎯 SKILL READINESS")
        print("-" * 40)
        for skill_id, skill in results['skill_readiness'].items():
            status = "✅ READY" if skill['ready'] else "❌ NOT READY"
            print(f"   {skill['name']}: {status}")
            if not skill['ready'] and skill['missing']:
                for missing in skill['missing'][:3]:
                    print(f"      ↳ Missing: {missing}")

        # Section breakdown
        print("\n📑 SECTION BREAKDOWN")
        print("-" * 40)

        print("\n   Required Sections (1-13):")
        for num in range(1, 14):
            section = results['sections'].get(num, {})
            self._print_section_line(num, section)

        print("\n   Recommended Sections (14-19):")
        for num in range(14, 20):
            section = results['sections'].get(num, {})
            self._print_section_line(num, section)

        print("\n   Optional Sections (20):")
        section = results['sections'].get(20, {})
        self._print_section_line(20, section)

        # Blocking issues
        if results['blocking_issues']:
            print("\n🚨 BLOCKING ISSUES")
            print("-" * 40)
            for issue in results['blocking_issues']:
                print(f"   • {issue}")

        # Recommendations
        print("\n💡 NEXT STEPS")
        print("-" * 40)

        # Find most impactful incomplete sections
        incomplete_required = [
            (num, s) for num, s in results['sections'].items()
            if s['priority'] == 'required' and s['score'] < 70
        ]
        incomplete_required.sort(key=lambda x: x[1]['score'])

        if incomplete_required:
            print("   Complete these sections first:")
            for num, section in incomplete_required[:5]:
                print(f"   1. Section {num}: {section['name']} ({section['score']:.0f}%)")
                if section['issues']:
                    print(f"      → {section['issues'][0]}")
        else:
            print("   ✅ All required sections are complete!")
            print("   Consider filling in recommended sections for better results.")

        print("\n" + "=" * 60)

    def _score_bar(self, score: float, width: int = 20) -> str:
        """Generate a visual progress bar."""
        filled = int(score / 100 * width)
        empty = width - filled

        if score >= 80:
            color = "🟩"
        elif score >= 50:
            color = "🟨"
        else:
            color = "🟥"

        return f"[{'█' * filled}{'░' * empty}]"

    def _print_section_line(self, num: int, section: dict):
        """Print a single section status line."""
        if not section:
            print(f"   {num:2}. {'Unknown':<30} ❓ Not found")
            return

        name = section['name'][:28]
        score = section['score']

        if score >= 80:
            icon = "✅"
        elif score >= 50:
            icon = "🟡"
        else:
            icon = "❌"

        print(f"   {num:2}. {name:<30} {icon} {score:>3.0f}%")


def find_profile(client_folder: str) -> Path:
    """Find the profile file in a client folder."""
    folder = Path(client_folder)

    # Look for 00_*_CLIENT_PROFILE.md
    profiles = list(folder.glob("00_*_CLIENT_PROFILE.md"))
    if profiles:
        return profiles[0]

    # Fallback: any CLIENT_PROFILE.md
    profiles = list(folder.glob("*CLIENT_PROFILE.md"))
    if profiles:
        return profiles[0]

    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Validate client profile completeness for downstream skills"
    )
    parser.add_argument(
        '--client-folder',
        help="Path to client folder (will find profile automatically)"
    )
    parser.add_argument(
        '--profile',
        help="Direct path to profile file"
    )
    parser.add_argument(
        '--skill',
        choices=['social_audit', 'strategy', 'content', 'reporting', 
                 'linkedin_voice', 'linkedin_profile', 'linkedin_strategy', 
                 'linkedin_content', 'linkedin_pillars'],
        help="Check readiness for specific skill"
    )
    parser.add_argument(
        '--json',
        action='store_true',
        help="Output results as JSON"
    )

    args = parser.parse_args()

    # Find profile
    profile_path = None
    if args.profile:
        profile_path = Path(args.profile)
    elif args.client_folder:
        profile_path = find_profile(args.client_folder)
        if not profile_path:
            print(f"❌ No profile found in: {args.client_folder}")
            print("   Run build_profile.py first to generate a profile.")
            exit(1)
    else:
        print("❌ Please provide --client-folder or --profile")
        exit(1)

    # Validate
    validator = ProfileValidator(str(profile_path))
    results = validator.validate()

    if not results:
        exit(1)

    # Output
    if args.json:
        import json
        print(json.dumps(results, indent=2))
    else:
        validator.print_report(results)

        # Exit code based on skill readiness
        if args.skill:
            skill_ready = results['skill_readiness'].get(args.skill, {}).get('ready', False)
            exit(0 if skill_ready else 1)
        else:
            # Exit 0 if required sections are >70% complete
            exit(0 if results['required_score'] >= 70 else 1)
