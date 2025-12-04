#!/usr/bin/env python3
"""
Fill Report Template Script
Auto-fills the social audit markdown template with calculated metrics.
"""
import argparse
import json
from datetime import datetime

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--metrics', required=True, help="Path to metrics.json")
    parser.add_argument('--template', required=True, help="Path to social_audit_matrix.md")
    parser.add_argument('--output', required=True, help="Path to save the draft report")
    parser.add_argument('--client-name', required=True, help="Name of the client")
    args = parser.parse_args()

    # Load Data
    with open(args.metrics, 'r') as f: data = json.load(f)
    with open(args.template, 'r') as f: template = f.read()

    meta = data.get('meta', {})
    macro = data.get('macro', {})
    mech = data.get('mechanics', {})
    
    # 1. Basic Metadata Replacements
    replacements = {
        '{{client_name}}': args.client_name,
        '{{report_date}}': datetime.now().strftime('%Y-%m-%d'),
        '{{start_date}}': meta.get('start_date', 'N/A'),
        '{{end_date}}': meta.get('end_date', 'N/A'),
        '{{data_months}}': str(meta.get('total_months', 'N/A')),
        '{{growth_status}}': macro.get('growth_status', 'N/A'),
        '{{yoy_comparison}}': macro.get('yoy_delta', 'N/A'),
        '{{peak_months_list}}': ", ".join(macro.get('peaks', ['N/A'])),
        '{{valley_months_list}}': ", ".join(macro.get('valleys', ['N/A'])),
    }

    # 2. Platform Stats
    # Looks for "Instagram", "Facebook", "Google" in the data and fills specific tags
    for p in mech.get('platforms', []):
        name = p['platform'].lower()
        tag = None
        if 'instagram' in name: tag = 'ig'
        elif 'facebook' in name: tag = 'fb'
        elif 'google' in name: tag = 'gbp'
        
        if tag:
            replacements[f'{{{{ {tag}_volume }}}}'] = str(p.get('volume', 0))
            replacements[f'{{{{{tag}_volume}}}}'] = str(p.get('volume', 0)) # Handle spacing variations
            replacements[f'{{{{ {tag}_engagement }}}}'] = f"{p.get('avg_engagement', 0)}%"
            replacements[f'{{{{{tag}_engagement}}}}'] = f"{p.get('avg_engagement', 0)}%"

    # 3. Format Stats
    # Looks for "Static", "Carousel", "Reel"
    for f in mech.get('formats', []):
        name = f['format'].lower()
        tag = None
        if 'static' in name: tag = 'static'
        elif 'carousel' in name: tag = 'carousel'
        elif 'reel' in name: tag = 'reel'
        
        if tag:
            replacements[f'{{{{ {tag}_engagement }}}}'] = f"{f.get('avg_engagement', 0)}%"
            replacements[f'{{{{ {tag}_percent }}}}'] = str(f.get('percent_of_feed', 0))

    # 4. Hall of Fame (Top 2 Posts)
    hof = data.get('hall_of_fame', [])
    for i in range(3): # Fill up to 3 if they exist
        if i < len(hof):
            post = hof[i]
            # Fill placeholders like {{post_1_date}}, {{post_2_metric}}
            replacements[f'{{{{post_{i+1}_title}}}}'] = f"{post.get('format', 'Post')} on {post.get('date')}"
            replacements[f'{{{{post_{i+1}_date}}}}'] = post.get('date', 'N/A')
            replacements[f'{{{{post_{i+1}_metric}}}}'] = post.get('metrics', 'N/A')
            replacements[f'{{{{post_{i+1}_format}}}}'] = post.get('format', 'N/A')

    # Execute Replacements
    content = template
    for key, value in replacements.items():
        content = content.replace(key, str(value))
        
    # Save
    with open(args.output, 'w') as f:
        f.write(content)
    
    print(f"✅ Draft report generated at: {args.output}")

if __name__ == "__main__":
    main()