#!/usr/bin/env python3
import sys, json, logging
from pathlib import Path
try: import pandas as pd
except: sys.exit("Error: pip install pandas")

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

class Analyzer:
    def __init__(self, bench_path=None):
        self.benchmarks = {"instagram": {"healthy_min": 3.0}, "facebook": {"healthy_min": 1.0}, "google_business_profile": {"healthy_min": 2.0}}
        if bench_path and Path(bench_path).exists():
            with open(bench_path) as f: self.benchmarks = json.load(f)

    def analyze(self, input_path, output_path):
        with open(input_path) as f: data = json.load(f)
        if not data.get('posts'): return
        df = pd.DataFrame(data['posts'])
        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values('date')
        
        # 1. Macro & YoY
        total_days = (df['date'].max() - df['date'].min()).days
        if total_days >= 730:
            last_year = df[df['date'] > (df['date'].max() - pd.Timedelta(days=365))]['engagement_rate'].mean()
            prev_year = df[df['date'] <= (df['date'].max() - pd.Timedelta(days=365))]['engagement_rate'].mean()
            yoy = ((last_year - prev_year)/prev_year)*100 if prev_year > 0 else 0
            yoy_str = f"{yoy:+.1f}% vs previous year"
        else:
            mid = df['date'].min() + (df['date'].max() - df['date'].min())/2
            first = df[df['date'] < mid]['engagement_rate'].mean()
            second = df[df['date'] >= mid]['engagement_rate'].mean()
            yoy = ((second - first)/first)*100 if first > 0 else 0
            yoy_str = f"{yoy:+.1f}% (first half vs second half)"

        # 2. Seasonality
        df['month'] = df['date'].dt.month_name()
        monthly = df.groupby('month')['engagement_rate'].mean().sort_values(ascending=False)
        peak = ", ".join(monthly.head(3).index) if len(monthly) >= 6 else "Insufficient data"
        valley = ", ".join(monthly.tail(3).index) if len(monthly) >= 6 else "Insufficient data"

        # 3. Platforms
        platforms = []
        for p in df['platform'].unique():
            pdf = df[df['platform']==p]
            avg = pdf['engagement_rate'].mean() if 'engagement_rate' in pdf else 0
            target = self.benchmarks.get(p, {}).get('healthy_min', 2.0)
            rec = "Scale up" if avg >= target else "Review strategy"
            platforms.append({'platform':p, 'volume':len(pdf), 'avg_engagement':round(avg,2), 'recommendation':rec})

        # 4. Formats
        def get_fmt(pt):
            s = str(pt).lower()
            return 'Carousel' if 'carousel' in s else ('Reel' if 'reel' in s else 'Static')
        if 'post_type' in df.columns:
            df['fmt'] = df['post_type'].apply(get_fmt)
        else:
            df['fmt'] = 'Static'  # Default if no post_type column
        formats = []
        for f in ['Static','Carousel','Reel']:
            fdf = df[df['fmt']==f]
            if len(fdf)>0:
                formats.append({'format':f, 'avg_engagement':round(fdf['engagement_rate'].mean(),2), 'percent_of_feed':round(len(fdf)/len(df)*100,1), 'verdict': "Keep" if fdf['engagement_rate'].mean() > 2 else "Improve"})

        # 5. Hall of Fame
        df['total_interact'] = df['likes'].fillna(0) + df['comments'].fillna(0) + df['shares'].fillna(0)
        hof = []
        for _, r in df.nlargest(5, 'total_interact').iterrows():
            hof.append({
                'date': r['date'].strftime('%Y-%m-%d'),
                'metrics': f"{int(r['total_interact'])} interactions",
                'format': r['fmt'],
                'why_legendary': f"High engagement ({r['engagement_rate']}%)",
                'reboot_action': f"Recreate this {r['fmt']}"
            })

        # 6. Red Flags
        red_flags = []
        fmt_dict = {f['format']:f for f in formats}
        if 'Carousel' in fmt_dict and 'Static' in fmt_dict:
            if fmt_dict['Carousel']['avg_engagement'] > fmt_dict['Static']['avg_engagement']:
                if fmt_dict['Carousel']['percent_of_feed'] < 25:
                    red_flags.append({'name':'Format Misallocation', 'fix':'Increase Carousel output'})
        
        while len(red_flags) < 2: red_flags.append({'name':'Monitoring', 'fix':'Continue current strategy'})

        # Output
        metrics = {
            'meta': {'start_date': str(df['date'].min().date()), 'end_date': str(df['date'].max().date()), 'total_months': round(total_days/30, 1)},
            'macro': {'growth_status': "Trending Up" if yoy > 0 else "Trending Down", 'yoy_delta': f"{yoy:.1f}%", 'yoy_comparison': yoy_str, 'trajectory_analysis': f"Growth is {yoy:.1f}%"},
            'seasonality': {'peak_months': peak, 'valley_months': valley, 'implications': "Align calendar with peaks"},
            'mechanics': {'platforms': platforms, 'formats': formats},
            'hall_of_fame': hof,
            'red_flags': red_flags,
            'strategic_pivot': {'diagnosis': 'Review format mix', 'core_strategy': 'Double down on top formats'}
        }
        
        with open(output_path, 'w') as f: json.dump(metrics, f, indent=2, default=str)
        logger.info(f"✅ Metrics generated: {output_path}")

if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('--input', required=True); p.add_argument('--output', required=True); p.add_argument('--benchmarks')
    a = p.parse_args()
    Analyzer(a.benchmarks).analyze(a.input, a.output)
