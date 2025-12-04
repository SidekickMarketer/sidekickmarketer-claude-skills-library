#!/usr/bin/env python3
"""
Complete CMA Social Data Parser
Parses ALL CSV files from both 05_Reports_Analytics and 07_Social_Media
"""

import csv
import os
import glob
from collections import defaultdict
from datetime import datetime

base_path = "/Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/2. Clients/01_Clients/client-cma"

# Find ALL CSV insight files
all_csv_files = []

# Search pattern 1: 07_Social_Media/02_Performance_Data
pattern1 = os.path.join(base_path, "07_Social_Media/02_Performance_Data/**/*Insights.csv")
all_csv_files.extend(glob.glob(pattern1, recursive=True))

# Search pattern 2: 05_Reports_Analytics
pattern2 = os.path.join(base_path, "05_Reports_Analytics/**/*Insights*.csv")
all_csv_files.extend(glob.glob(pattern2, recursive=True))

print(f"Found {len(all_csv_files)} CSV files to parse\n")

all_posts = []
errors = []

for csv_file in all_csv_files:
    filename = os.path.basename(csv_file)
    
    try:
        with open(csv_file, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            post_count = 0
            
            for row in reader:
                # Determine platform
                if 'IG' in filename or 'Instagram' in filename:
                    platform = 'Instagram'
                    post_type = row.get('Post type', '')
                    
                    # Get publish date from "Publish time" not "Date" (which contains "Lifetime")
                    publish_time = row.get('Publish time', '')
                    
                    # Calculate total engagement
                    likes = int(row.get('Likes', 0) or 0)
                    comments = int(row.get('Comments', 0) or 0)
                    shares = int(row.get('Shares', 0) or 0)
                    saves = int(row.get('Saves', 0) or 0)
                    reach = int(row.get('Reach', 0) or 0)
                    views = int(row.get('Views', 0) or 0)
                    
                    total_engagement = likes + comments + shares + saves
                    engagement_rate = (total_engagement / reach * 100) if reach > 0 else 0
                    
                    all_posts.append({
                        'platform': platform,
                        'file': filename,
                        'publish_time': publish_time,
                        'description': row.get('Description', '')[:100],
                        'post_type': post_type,
                        'reach': reach,
                        'views': views,
                        'likes': likes,
                        'comments': comments,
                        'shares': shares,
                        'saves': saves,
                        'total_engagement': total_engagement,
                        'engagement_rate': engagement_rate,
                        'permalink': row.get('Permalink', '')
                    })
                    post_count += 1
                
                elif 'FB' in filename or 'Facebook' in filename:
                    platform = 'Facebook'
                    
                    publish_time = row.get('Publish time', '')
                    
                    # Calculate total engagement
                    reactions = int(row.get('Reactions', 0) or 0)
                    comments = int(row.get('Comments', 0) or 0)
                    shares = int(row.get('Shares', 0) or 0)
                    reach = int(row.get('Reach', 0) or 0)
                    views = int(row.get('Views', 0) or 0)
                    
                    total_engagement = reactions + comments + shares
                    engagement_rate = (total_engagement / reach * 100) if reach > 0 else 0
                    
                    all_posts.append({
                        'platform': platform,
                        'file': filename,
                        'publish_time': publish_time,
                        'description': (row.get('Title', '') or row.get('Description', ''))[:100],
                        'post_type': row.get('Post type', ''),
                        'reach': reach,
                        'views': views,
                        'likes': reactions,
                        'comments': comments,
                        'shares': shares,
                        'saves': 0,
                        'total_engagement': total_engagement,
                        'engagement_rate': engagement_rate,
                        'permalink': row.get('Permalink', '')
                    })
                    post_count += 1
                    
                elif 'GBP' in filename or 'Google' in filename:
                    platform = 'Google Business Profile'
                    
                    publish_time = row.get('Publish time', '') or row.get('Posted', '')
                    
                    # GBP metrics are different
                    views = int(row.get('Views', 0) or 0)
                    clicks = int(row.get('Clicks', 0) or 0)
                    calls = int(row.get('Calls', 0) or 0)
                    impressions = int(row.get('Impressions', 0) or 0)
                    
                    total_engagement = views + clicks + calls
                    engagement_rate = (total_engagement / impressions * 100) if impressions > 0 else 0
                    
                    all_posts.append({
                        'platform': platform,
                        'file': filename,
                        'publish_time': publish_time,
                        'description': row.get('Post text', '')[:100] or row.get('Summary', '')[:100],
                        'post_type': row.get('Type', 'Update'),
                        'reach': impressions,
                        'views': views,
                        'likes': 0,
                        'comments': 0,
                        'shares': 0,
                        'saves': 0,
                        'clicks': clicks,
                        'calls': calls,
                        'total_engagement': total_engagement,
                        'engagement_rate': engagement_rate,
                        'permalink': ''
                    })
                    post_count += 1
            
            print(f"✅ {filename}: {post_count} posts")
            
    except Exception as e:
        error_msg = f"❌ {filename}: {e}"
        errors.append(error_msg)
        print(error_msg)

print(f"\n{'='*80}")
print(f"PARSING COMPLETE")
print(f"{'='*80}")
print(f"Total posts parsed: {len(all_posts)}")
print(f"Instagram: {len([p for p in all_posts if p['platform'] == 'Instagram'])}")
print(f"Facebook: {len([p for p in all_posts if p['platform'] == 'Facebook'])}")
print(f"GBP: {len([p for p in all_posts if p['platform'] == 'Google Business Profile'])}")
print(f"Errors: {len(errors)}")

# Save detailed results
import json
with open('/tmp/cma_complete_data.json', 'w') as f:
    json.dump({
        'posts': all_posts,
        'summary': {
            'total_posts': len(all_posts),
            'by_platform': {
                'instagram': len([p for p in all_posts if p['platform'] == 'Instagram']),
                'facebook': len([p for p in all_posts if p['platform'] == 'Facebook']),
                'gbp': len([p for p in all_posts if p['platform'] == 'Google Business Profile'])
            },
            'files_processed': len(all_csv_files),
            'errors': errors
        }
    }, f, indent=2)

print(f"\n💾 Full results saved to: /tmp/cma_complete_data.json")

