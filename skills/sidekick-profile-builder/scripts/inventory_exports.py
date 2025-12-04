#!/usr/bin/env python3
"""
Inventory Notion Exports
Scans a folder of exported markdown files and catalogs what each contains.
"""
import argparse
import json
import re
import os
from pathlib import Path
from datetime import datetime
from collections import defaultdict

# Keywords that indicate what category a file might contain
CATEGORY_KEYWORDS = {
    'business_core': [
        'client name', 'company', 'industry', 'website', 'founded',
        'location', 'address', 'contact', 'owner', 'ceo', 'founder'
    ],
    'target_audience': [
        'audience', 'segment', 'icp', 'demographic', 'persona',
        'customer', 'buyer', 'target market', 'who we serve'
    ],
    'brand_voice': [
        'voice', 'tone', 'brand', 'messaging', 'personality',
        'style', 'how we sound', 'writing style', 'brand guide'
    ],
    'content_pillars': [
        'pillar', 'content type', 'theme', 'category', 'topic',
        'content strategy', 'content mix', 'content calendar'
    ],
    'sow_deliverables': [
        'deliverable', 'posts per', 'frequency', 'monthly', 'sow',
        'contract', 'scope', 'agreement', 'services'
    ],
    'kpis_goals': [
        'goal', 'kpi', 'metric', 'target', 'benchmark',
        'success', 'measure', 'objective', 'okr'
    ],
    'competitors': [
        'competitor', 'competition', 'versus', 'alternative',
        'market', 'landscape', 'compare'
    ],
    'guidelines': [
        'guideline', 'rule', 'constraint', 'avoid', "don't",
        'never', 'policy', 'approval', 'restriction'
    ],
    'social_media': [
        'instagram', 'facebook', 'social', 'gbp', 'google business',
        'tiktok', 'linkedin', 'twitter', 'youtube'
    ],
    'performance': [
        'analytics', 'report', 'performance', 'engagement',
        'impressions', 'reach', 'clicks', 'conversion'
    ]
}

def classify_file(content: str) -> dict:
    """Analyze content and return category scores."""
    content_lower = content.lower()
    scores = {}
    matches = {}

    for category, keywords in CATEGORY_KEYWORDS.items():
        score = 0
        found = []
        for keyword in keywords:
            count = content_lower.count(keyword)
            if count > 0:
                score += count
                found.append(f"{keyword} ({count}x)")
        if score > 0:
            scores[category] = score
            matches[category] = found

    return {'scores': scores, 'matches': matches}

def get_file_stats(path: Path) -> dict:
    """Get basic file statistics."""
    stat = path.stat()
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    # Count structure elements
    headers = len(re.findall(r'^#+\s', content, re.MULTILINE))
    tables = len(re.findall(r'^\|', content, re.MULTILINE))
    lists = len(re.findall(r'^[-*]\s', content, re.MULTILINE))
    links = len(re.findall(r'\[.*?\]\(.*?\)', content))

    return {
        'size_bytes': stat.st_size,
        'modified': datetime.fromtimestamp(stat.st_mtime).isoformat(),
        'lines': content.count('\n') + 1,
        'chars': len(content),
        'headers': headers,
        'tables': tables,
        'list_items': lists,
        'links': links,
        'content': content
    }

def inventory(source_dir: str, output_path: str = None):
    """Scan all files and create inventory."""
    source = Path(source_dir)

    if not source.exists():
        print(f"❌ Source directory not found: {source}")
        return None

    # Collect all processable files
    extensions = {'.md', '.txt', '.csv', '.json'}
    files = [f for f in source.rglob('*') if f.suffix.lower() in extensions and f.is_file()]

    if not files:
        print(f"⚠️  No processable files found in {source}")
        return None

    print(f"📂 Scanning {len(files)} files in {source.name}/")
    print("=" * 50)

    inventory = {
        'source': str(source),
        'scan_date': datetime.now().isoformat(),
        'total_files': len(files),
        'files': [],
        'category_summary': defaultdict(list)
    }

    for filepath in sorted(files):
        rel_path = filepath.relative_to(source)
        stats = get_file_stats(filepath)
        classification = classify_file(stats['content'])

        # Determine primary category
        if classification['scores']:
            primary_category = max(classification['scores'], key=classification['scores'].get)
            primary_score = classification['scores'][primary_category]
        else:
            primary_category = 'unclassified'
            primary_score = 0

        file_info = {
            'path': str(rel_path),
            'full_path': str(filepath),
            'size_bytes': stats['size_bytes'],
            'lines': stats['lines'],
            'modified': stats['modified'],
            'structure': {
                'headers': stats['headers'],
                'tables': stats['tables'],
                'list_items': stats['list_items'],
                'links': stats['links']
            },
            'primary_category': primary_category,
            'category_scores': classification['scores'],
            'keyword_matches': classification['matches']
        }

        inventory['files'].append(file_info)
        inventory['category_summary'][primary_category].append(str(rel_path))

        # Print summary
        cat_display = primary_category.upper() if primary_category != 'unclassified' else '???'
        print(f"  [{cat_display:15}] {rel_path} ({stats['lines']} lines)")

    # Print category summary
    print("\n" + "=" * 50)
    print("📊 CATEGORY SUMMARY")
    print("=" * 50)

    for category, files_list in sorted(inventory['category_summary'].items()):
        print(f"\n{category.upper()} ({len(files_list)} files):")
        for f in files_list[:5]:
            print(f"  • {f}")
        if len(files_list) > 5:
            print(f"  ... and {len(files_list) - 5} more")

    # Save inventory
    if output_path:
        out = Path(output_path)
    else:
        out = source.parent / "reports" / "_file_inventory.json"

    out.parent.mkdir(parents=True, exist_ok=True)

    # Remove content from saved inventory (too large)
    for f in inventory['files']:
        if 'content' in f:
            del f['content']

    with open(out, 'w') as f:
        json.dump(inventory, f, indent=2, default=str)

    print(f"\n✅ Inventory saved: {out}")
    return inventory

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Inventory Notion export files")
    parser.add_argument('--source', required=True, help="Path to Notion export folder")
    parser.add_argument('--output', help="Output path for inventory JSON")
    args = parser.parse_args()

    inventory(args.source, args.output)
