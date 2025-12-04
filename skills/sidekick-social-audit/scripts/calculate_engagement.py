#!/usr/bin/env python3
"""
Calculate engagement rates for social media posts.
Formula: (likes + comments + shares) / reach * 100
"""
import argparse, json, sys, logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def process(input_path, output_path):
    input_file = Path(input_path)

    if not input_file.exists():
        logger.error(f"Input file not found: {input_path}")
        sys.exit(1)

    with open(input_file) as f:
        data = json.load(f)

    if 'posts' not in data or not data['posts']:
        logger.error("No posts found in input file")
        sys.exit(1)

    calculated = 0
    skipped = 0
    zero_reach = 0

    for post in data['posts']:
        # Skip if already has valid engagement rate
        if post.get('engagement_rate') and post['engagement_rate'] > 0:
            skipped += 1
            continue

        # Safely get numeric values (handle None, strings, etc.)
        likes = _to_int(post.get('likes', 0))
        comments = _to_int(post.get('comments', 0))
        shares = _to_int(post.get('shares', 0))
        reach = _to_int(post.get('reach', 0))

        total_interactions = likes + comments + shares

        if reach > 0:
            post['engagement_rate'] = round((total_interactions / reach) * 100, 2)
            calculated += 1
        else:
            post['engagement_rate'] = 0.0
            zero_reach += 1

    # Ensure output directory exists
    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, 'w') as f:
        json.dump(data, f, indent=2, default=str)

    logger.info(f"✅ Engagement calculated: {calculated} posts")
    if skipped > 0:
        logger.info(f"   Skipped (already had rate): {skipped}")
    if zero_reach > 0:
        logger.warning(f"   Zero reach (rate set to 0): {zero_reach}")

def _to_int(val):
    """Safely convert value to int, handling strings, None, floats."""
    if val is None:
        return 0
    if isinstance(val, (int, float)):
        return int(val)
    try:
        return int(float(str(val).replace(',', '').strip() or 0))
    except (ValueError, TypeError):
        return 0

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Calculate engagement rates for social posts")
    p.add_argument('--json-file', required=True, help="Input JSON from parse_social_data.py")
    p.add_argument('--output', required=True, help="Output path for enriched JSON")
    args = p.parse_args()
    process(args.json_file, args.output)
