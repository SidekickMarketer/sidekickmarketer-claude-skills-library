import csv
import os
from collections import defaultdict
from datetime import datetime

# Define paths
base_path = "/Users/kylenaughtrip/Library/CloudStorage/GoogleDrive-kyle@sidekickmarketer.com/My Drive/01_Sidekick Marketer/2. Clients/01_Clients/client-cma"

# CSV files to parse
csv_files = [
    "05_Reports_Analytics/01_Discovery Phase/Social Media and GBP/02_Feb 2025/2025-02_CMA_IG-Insights.csv.csv",
    "05_Reports_Analytics/01_Discovery Phase/Social Media and GBP/02_Feb 2025/2025-02_CMA_FB-Insights.csv",
    "05_Reports_Analytics/01_Discovery Phase/Social Media and GBP/04_April 2025/2025-04_CMA_IG-Insights (1).csv",
    "05_Reports_Analytics/01_Discovery Phase/Social Media and GBP/05_May 2025/2025-05_CMA_IG-Insights.csv",
    "05_Reports_Analytics/01_Discovery Phase/Social Media and GBP/05_May 2025/2025-05_CMA_FB-Insights.csv",
    "07_Social_Media/02_Performance_Data/2025-01_January/2025-01_CMA_FB-Insights.csv",
    "07_Social_Media/02_Performance_Data/2025-03_March/2025-03_CMA_IG-Insights.csv",
    "07_Social_Media/02_Performance_Data/2025-03_March/2025-03_CMA_FB-Insights.csv",
]

all_posts = []

for csv_file in csv_files:
    full_path = os.path.join(base_path, csv_file)
    if not os.path.exists(full_path):
        continue
    
    try:
        with open(full_path, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Determine platform
                if 'IG' in csv_file or 'Instagram' in csv_file:
                    platform = 'Instagram'
                    post_type = row.get('Post type', '')
                    
                    # Calculate total engagement
                    likes = int(row.get('Likes', 0) or 0)
                    comments = int(row.get('Comments', 0) or 0)
                    shares = int(row.get('Shares', 0) or 0)
                    saves = int(row.get('Saves', 0) or 0)
                    reach = int(row.get('Reach', 0) or 0)
                    
                    total_engagement = likes + comments + shares + saves
                    engagement_rate = (total_engagement / reach * 100) if reach > 0 else 0
                    
                    all_posts.append({
                        'platform': platform,
                        'month': csv_file.split('/')[2] if len(csv_file.split('/')) > 2 else csv_file.split('_')[0],
                        'description': row.get('Description', '')[:100],
                        'post_type': post_type,
                        'reach': reach,
                        'likes': likes,
                        'comments': comments,
                        'shares': shares,
                        'saves': saves,
                        'total_engagement': total_engagement,
                        'engagement_rate': engagement_rate,
                        'permalink': row.get('Permalink', '')
                    })
                
                elif 'FB' in csv_file or 'Facebook' in csv_file:
                    platform = 'Facebook'
                    
                    # Calculate total engagement
                    reactions = int(row.get('Reactions', 0) or 0)
                    comments = int(row.get('Comments', 0) or 0)
                    shares = int(row.get('Shares', 0) or 0)
                    reach = int(row.get('Reach', 0) or 0)
                    
                    total_engagement = reactions + comments + shares
                    engagement_rate = (total_engagement / reach * 100) if reach > 0 else 0
                    
                    all_posts.append({
                        'platform': platform,
                        'month': csv_file.split('/')[2] if len(csv_file.split('/')) > 2 else csv_file.split('_')[0],
                        'description': (row.get('Title', '') or row.get('Description', ''))[:100],
                        'post_type': row.get('Post type', ''),
                        'reach': reach,
                        'likes': reactions,
                        'comments': comments,
                        'shares': shares,
                        'saves': 0,
                        'total_engagement': total_engagement,
                        'engagement_rate': engagement_rate,
                        'permalink': row.get('Permalink', '')
                    })
    except Exception as e:
        print(f"Error parsing {csv_file}: {e}")

# Sort posts by total engagement
hall_of_fame = sorted(all_posts, key=lambda x: x['total_engagement'], reverse=True)[:15]

print("\n" + "="*80)
print("HALL OF FAME - TOP 15 POSTS BY ENGAGEMENT")
print("="*80)

for i, post in enumerate(hall_of_fame, 1):
    print(f"\n#{i} - {post['platform']} ({post['month']})")
    print(f"Description: {post['description']}")
    print(f"Type: {post['post_type']}")
    print(f"Reach: {post['reach']} | Engagement: {post['total_engagement']} ({post['engagement_rate']:.1f}%)")
    print(f"Breakdown: {post['likes']} likes, {post['comments']} comments, {post['shares']} shares, {post['saves']} saves")

# Format analysis
print("\n" + "="*80)
print("FORMAT PERFORMANCE ANALYSIS")
print("="*80)

format_stats = defaultdict(lambda: {'count': 0, 'total_engagement': 0, 'total_reach': 0})

for post in all_posts:
    if post['platform'] == 'Instagram':
        format_type = post['post_type']
        if 'carousel' in format_type.lower():
            key = 'IG Carousel'
        elif 'image' in format_type.lower():
            key = 'IG Single Image'
        elif 'reel' in format_type.lower():
            key = 'IG Reel'
        else:
            key = f'IG {format_type}'
        
        format_stats[key]['count'] += 1
        format_stats[key]['total_engagement'] += post['total_engagement']
        format_stats[key]['total_reach'] += post['reach']

print(f"\n{'Format':<20} {'Count':<8} {'Avg Reach':<12} {'Avg Engagement':<18} {'Engagement Rate'}")
print("-" * 80)

for format_type, stats in sorted(format_stats.items()):
    if stats['count'] > 0:
        avg_reach = stats['total_reach'] / stats['count']
        avg_engagement = stats['total_engagement'] / stats['count']
        avg_rate = (avg_engagement / avg_reach * 100) if avg_reach > 0 else 0
        print(f"{format_type:<20} {stats['count']:<8} {avg_reach:<12.1f} {avg_engagement:<18.1f} {avg_rate:.1f}%")

# Month-over-month trends
print("\n" + "="*80)
print("MONTH-OVER-MONTH ENGAGEMENT TRENDS")
print("="*80)

month_stats = defaultdict(lambda: {'count': 0, 'total_engagement': 0, 'total_reach': 0})

for post in all_posts:
    month = post['month']
    month_stats[month]['count'] += 1
    month_stats[month]['total_engagement'] += post['total_engagement']
    month_stats[month]['total_reach'] += post['reach']

print(f"\n{'Month':<20} {'Posts':<8} {'Avg Reach':<12} {'Avg Engagement':<18} {'Engagement Rate'}")
print("-" * 80)

for month in sorted(month_stats.keys()):
    stats = month_stats[month]
    if stats['count'] > 0:
        avg_reach = stats['total_reach'] / stats['count']
        avg_engagement = stats['total_engagement'] / stats['count']
        avg_rate = (avg_engagement / avg_reach * 100) if avg_reach > 0 else 0
        print(f"{month:<20} {stats['count']:<8} {avg_reach:<12.1f} {avg_engagement:<18.1f} {avg_rate:.1f}%")

print(f"\n\nTotal posts analyzed: {len(all_posts)}")
print("="*80)

