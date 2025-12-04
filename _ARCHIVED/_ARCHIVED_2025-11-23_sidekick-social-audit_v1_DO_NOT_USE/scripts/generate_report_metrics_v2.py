#!/usr/bin/env python3
import json
import argparse
from datetime import datetime
from collections import defaultdict
import statistics

def analyze(input_path):
    with open(input_path) as f: data = json.load(f)
    posts = data.get('posts', [])
    if not posts: return {}
    
    # Sort
    for p in posts: 
        if p.get('date'):
            p['_dt'] = datetime.strptime(p['date'], '%Y-%m-%d')
    posts = [p for p in posts if '_dt' in p]
    posts.sort(key=lambda x: x['_dt'])
    
    if not posts: return {}
    
    # Macro (Half vs Half)
    mid = len(posts)//2
    first = posts[:mid]
    second = posts[mid:]
    avg1 = statistics.mean([p.get('engagement_rate',0) for p in first]) if first else 0
    avg2 = statistics.mean([p.get('engagement_rate',0) for p in second]) if second else 0
    yoy = ((avg2 - avg1)/avg1)*100 if avg1 > 0 else 0
    
    # Seasonality
    months = defaultdict(list)
    for p in posts: months[p['_dt'].strftime('%B')].append(p.get('engagement_rate',0))
    season_avg = {k:statistics.mean(v) for k,v in months.items()}
    sorted_m = sorted(season_avg.items(), key=lambda x:x[1], reverse=True)
    
    # Formats
    formats = defaultdict(list)
    for p in posts:
        fmt = 'Static'
        pt = str(p.get('post_type','')).lower()
        if 'carousel' in pt or 'album' in pt: fmt = 'Carousel'
        elif 'reel' in pt or 'video' in pt: fmt = 'Reel'
        formats[fmt].append(p.get('engagement_rate',0))
    
    fmt_stats = []
    for k,v in formats.items():
        fmt_stats.append({'format':k, 'avg_engagement':round(statistics.mean(v),2), 'percent_of_feed':round(len(v)/len(posts)*100,1)})

    # Platform
    plat_map = defaultdict(list)
    for p in posts: plat_map[p['platform']].append(p.get('engagement_rate',0))
    plat_stats = [{'platform':k, 'volume':len(v), 'avg_engagement':round(statistics.mean(v),2)} for k,v in plat_map.items()]

    # Hall of Fame
    def get_interactions(p): return sum([p.get('likes',0), p.get('comments',0), p.get('shares',0), p.get('saves',0)])
    top = sorted(posts, key=get_interactions, reverse=True)[:5]
    hof = [{'date':p['date'], 'metrics':f"{get_interactions(p)} interactions", 'format':p.get('post_type','?')} for p in top]

    return {
        'meta': {'start_date':posts[0]['date'], 'end_date':posts[-1]['date'], 'total_months':round(len(posts)/30.4, 1)},
        'macro': {'growth_status': "📈 Trending Up" if yoy > 5 else ("📉 Trending Down" if yoy < -5 else "➡️ Flat"), 'yoy_delta': f"{round(yoy,1)}%", 'peaks':[x[0] for x in sorted_m[:2]], 'valleys':[x[0] for x in sorted_m[-2:]]},
        'hall_of_fame': hof,
        'mechanics': {'formats':fmt_stats, 'platforms':plat_stats}
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True) # <--- This is the critical line
    args = parser.parse_args()
    
    res = analyze(args.input)
    with open(args.output, 'w') as f: json.dump(res, f, indent=2)
    print(f"✅ Metrics generated: {args.output}")