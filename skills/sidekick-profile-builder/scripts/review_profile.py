#!/usr/bin/env python3
"""
Review Profile - Generate a verification checklist for Claude to walk through.
Instead of parsing garbage conflicts, this reads the actual profile and
creates a checklist of key fields that Claude should verify with the user.
"""
import argparse
import json
import re
from pathlib import Path
from typing import Dict, List, Any, Optional


class ProfileReviewer:
    """Generate verification checklist from profile content."""

    def __init__(self, client_folder: str):
        self.client_folder = Path(client_folder)
        self.client_name = self.client_folder.name.replace('client-', '').upper()
        self.audit_dir = self.client_folder / "90_Archive" / "Profile_Build"
        self.profile_path = self.client_folder / f"00_{self.client_name}_CLIENT_PROFILE.md"

        # Key fields to verify for each section
        self.verification_fields = {
            1: {
                'name': 'Business Core',
                'fields': ['Client Name', 'Legal Name', 'Industry', 'Website', 'Address', 'Service Area', 'Founded', 'Company Size']
            },
            2: {
                'name': 'Contacts',
                'fields': ['Primary Contact', 'Email', 'Phone', 'Decision Maker']
            },
            3: {
                'name': 'Target Audience',
                'fields': ['Demographics', 'Primary Segments', 'Customer Journey']
            },
            4: {
                'name': 'Brand Voice',
                'fields': ['Tone', 'Words to Use', 'Words to Avoid']
            },
            5: {
                'name': 'Products & Services',
                'fields': ['Primary Service', 'Secondary Services', 'Price Points']
            },
            6: {
                'name': 'Content Pillars',
                'fields': ['Pillar 1', 'Pillar 2', 'Content Mix']
            },
            7: {
                'name': 'SOW/Deliverables',
                'fields': ['Contract Start', 'Monthly Retainer', 'Social Deliverables']
            },
            8: {
                'name': 'KPIs & Goals',
                'fields': ['Business Goals', 'Platform Metrics', 'Success Definition']
            },
            9: {
                'name': 'Competitors',
                'fields': ['Competitor 1', 'Competitor 2', 'Differentiation']
            },
            10: {
                'name': 'Seasonality',
                'fields': ['Peak Season', 'Low Season', 'Key Events']
            },
            11: {
                'name': 'Visual Brand',
                'fields': ['Primary Color', 'Secondary Color', 'Logo Usage']
            },
            12: {
                'name': 'Account Access',
                'fields': ['Instagram', 'Facebook', 'GBP', 'Google Ads']
            },
            13: {
                'name': 'Guidelines',
                'fields': ['Compliance Requirements', 'Approval Workflow', 'Topics to Avoid']
            },
            14: {
                'name': 'Business Model',
                'fields': ['Revenue Streams', 'Average Transaction', 'Lead Sources']
            },
            15: {
                'name': 'Origin Story',
                'fields': ['Founder', 'Year Founded', 'The Why Story']
            },
            16: {
                'name': 'Local Presence',
                'fields': ['Google Rating', 'Review Count', 'Community Involvement']
            },
            17: {
                'name': 'Marketing History',
                'fields': ['Previous Agency', 'What Worked', 'What Flopped']
            },
            18: {
                'name': 'Content Bank',
                'fields': ['Photo Library', 'Testimonials', 'FAQs']
            },
            19: {
                'name': 'Email & CRM',
                'fields': ['Email Platform', 'List Size', 'CRM System']
            },
            20: {
                'name': 'Relationship Notes',
                'fields': ['Communication Preference', 'Working Style', 'Pet Peeves']
            }
        }

    def read_profile_sections(self) -> Dict[int, str]:
        """Read the profile and extract each section's content."""
        if not self.profile_path.exists():
            return {}

        content = self.profile_path.read_text()
        sections = {}

        # Split by section headers (## 1. Business Core, etc.)
        section_pattern = r'## (\d+)\.\s+(.+?)(?=\n## \d+\.|\n---\n## Build Metadata|$)'
        matches = re.findall(section_pattern, content, re.DOTALL)

        for num, section_content in matches:
            sections[int(num)] = section_content.strip()

        return sections

    def extract_table_values(self, section_content: str) -> Dict[str, str]:
        """Extract key-value pairs from markdown tables in a section."""
        values = {}

        # Match table rows: | **Key** | Value | ... |
        table_pattern = r'\|\s*\*?\*?([^|*]+?)\*?\*?\s*\|\s*([^|]+?)\s*\|'
        matches = re.findall(table_pattern, section_content)

        for key, value in matches:
            key = key.strip()
            value = value.strip()
            if key and value and key not in ['Field', 'Value', '---', '----']:
                values[key] = value

        return values

    def generate_checklist(self) -> Dict[str, Any]:
        """Generate a verification checklist from the profile."""
        sections = self.read_profile_sections()
        checklist = []

        for section_num, config in self.verification_fields.items():
            section_content = sections.get(section_num, '')
            table_values = self.extract_table_values(section_content)

            section_check = {
                'section': section_num,
                'name': config['name'],
                'fields': []
            }

            for field in config['fields']:
                # Try to find the value in extracted table data
                current_value = None
                for key, val in table_values.items():
                    if field.lower() in key.lower():
                        current_value = val
                        break

                section_check['fields'].append({
                    'field': field,
                    'current_value': current_value,
                    'needs_review': current_value is None or current_value == '-' or len(current_value) < 2
                })

            # Only include sections that have items needing review
            needs_review = [f for f in section_check['fields'] if f['needs_review']]
            section_check['needs_review_count'] = len(needs_review)
            checklist.append(section_check)

        return {
            'client': self.client_name,
            'profile_path': str(self.profile_path),
            'checklist': checklist,
            'total_sections': len(checklist),
            'sections_needing_review': len([s for s in checklist if s['needs_review_count'] > 0])
        }

    def generate_review_questions(self) -> Dict[str, Any]:
        """Generate structured review output for Claude."""
        checklist = self.generate_checklist()

        review_data = {
            'client': self.client_name,
            'profile_path': str(self.profile_path),
            'summary': {
                'total_sections': checklist['total_sections'],
                'sections_needing_review': checklist['sections_needing_review']
            },
            'checklist': checklist['checklist'],
            'review_instructions': """
Claude should walk through the profile with the user:

1. For each section, show what's currently in the profile
2. Ask: "Is this correct? Anything to add or change?"
3. User confirms or provides corrections
4. Claude updates the profile

Focus on sections flagged as 'needs_review' first, but verify all sections.

Key questions to ask:
- Section 1: "Is the business name and address correct?"
- Section 2: "Who is the primary contact and how do they prefer to be reached?"
- Section 7: "What's the current SOW? Monthly retainer and deliverables?"
- Section 8: "What are the main goals we're tracking?"

After review, run validate_profile.py to confirm all skills are ready.
"""
        }

        return review_data

    def run(self) -> str:
        """Run review and output JSON."""
        review_data = self.generate_review_questions()

        # Ensure audit dir exists
        self.audit_dir.mkdir(parents=True, exist_ok=True)

        # Save to audit dir
        output_path = self.audit_dir / "_review_checklist.json"
        with open(output_path, 'w') as f:
            json.dump(review_data, f, indent=2)

        print(f"\n{'='*60}")
        print(f"  PROFILE REVIEW - {self.client_name}")
        print(f"{'='*60}\n")

        print(f"  Total sections: {review_data['summary']['total_sections']}")
        print(f"  Sections needing review: {review_data['summary']['sections_needing_review']}")

        # Show which sections need attention
        for section in review_data['checklist']:
            if section['needs_review_count'] > 0:
                print(f"    - Section {section['section']}: {section['name']} ({section['needs_review_count']} fields)")

        print(f"\n  Checklist saved to:")
        print(f"  {output_path}\n")
        print("  Claude should read this file and walk through each section with the user.\n")

        return str(output_path)


def main():
    parser = argparse.ArgumentParser(description='Generate profile review questions')
    parser.add_argument('--client-folder', required=True, help='Path to client folder')

    args = parser.parse_args()

    reviewer = ProfileReviewer(args.client_folder)
    reviewer.run()


if __name__ == '__main__':
    main()
