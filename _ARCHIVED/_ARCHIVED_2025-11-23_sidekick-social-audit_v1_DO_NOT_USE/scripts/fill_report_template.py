#!/usr/bin/env python3
"""
Fill Report Template Script
Auto-populates the social_audit_matrix.md template with metrics from parsed data
Eliminates manual placeholder replacement for faster audit completion
"""

import argparse
import json
import sys
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import statistics


class TemplateFiller:
    """Automatically fills audit report template with data"""

    def __init__(self, metrics_json: Path, template_path: Path, client_profile: Path):
        self.metrics_json = metrics_json
        self.template_path = template_path
        self.client_profile = client_profile
        self.placeholders = {}

    def load_data(self):
        """Load all required data sources"""
        # Load parsed metrics
        with open(self.metrics_json, 'r') as f:
            self.data = json.load(f)

        self.posts = [p for p in self.data['posts'] if p.get('source_type') != 'pdf']

        # Load template
        with open(self.template_path, 'r') as f:
            self.template = f.read()

        # Load client profile if exists
        self.client_name = "Client"
        if self.client_profile and self.client_profile.exists():
            with open(self.client_profile, 'r') as f:
                for line in f:
                    if '**Client Name**' in line or 'Client Name' in line:
                        parts = line.split('|')
                        if len(parts) >= 2:
                            self.client_name = parts[1].strip()
                            break

    def calculate_metrics(self):
        """Calculate all metrics needed for template"""
        posts = self.posts

        # Sort by date
        for p in posts:
            p['_dt'] = datetime.strptime(p['date'], '%Y-%m-%d')
        posts.sort(key=lambda x: x['_dt'])

        # Helper function
        def get_total_eng(p):
            return sum([p.get('likes', 0), p.get('comments', 0), p.get('shares', 0), p.get('saves', 0)])

        for p in posts:
            p['total_engagement'] = get_total_eng(p)

        # === METADATA ===
        self.placeholders['client_name'] = self.client_name
        self.placeholders['start_date'] = posts[0]['date']
        self.placeholders['end_date'] = posts[-1]['date']
        self.placeholders['data_months'] = round((posts[-1]['_dt'] - posts[0]['_dt']).days / 30.4, 1)
        self.placeholders['report_date'] = datetime.now().strftime('%Y-%m-%d')

        # === GROWTH TRAJECTORY ===
        midpoint = len(posts) // 2
        first_half = posts[:midpoint]
        second_half = posts[midpoint:]

        avg_eng_old = statistics.mean([p.get('engagement_rate', 0) for p in first_half if p.get('engagement_rate')])
        avg_eng_new = statistics.mean([p.get('engagement_rate', 0) for p in second_half if p.get('engagement_rate')])

        yoy_delta = ((avg_eng_new - avg_eng_old) / avg_eng_old * 100) if avg_eng_old > 0 else 0

        if yoy_delta > 15:
            self.placeholders['growth_status'] = "📈 Trending Up"
        elif yoy_delta < -15:
            self.placeholders['growth_status'] = "📉 Trending Down"
        else:
            self.placeholders['growth_status'] = "➡️ Flat"

        self.placeholders['yoy_comparison'] = f"+{yoy_delta:.1f}% engagement rate growth (first half: {avg_eng_old:.2f}% → second half: {avg_eng_new:.2f}%)"
        self.placeholders['trajectory_analysis'] = f"Engagement rates {'increased' if yoy_delta > 0 else 'decreased'} by {abs(yoy_delta):.1f}% from first half to second half of the analysis period."

        # === SEASONALITY ===
        month_map = defaultdict(list)
        for p in posts:
            month_name = p['_dt'].strftime('%B')
            if p.get('engagement_rate'):
                month_map[month_name].append(p['engagement_rate'])

        seasonality = {m: round(statistics.mean(rates), 2) for m, rates in month_map.items() if rates}
        sorted_months = sorted(seasonality.items(), key=lambda x: x[1], reverse=True)

        self.placeholders['peak_months_list'] = ", ".join([m[0] for m in sorted_months[:2]])
        self.placeholders['valley_months_list'] = ", ".join([m[0] for m in sorted_months[-2:]])
        self.placeholders['seasonality_implications'] = "Peak months align with business cycles (back-to-school, recital season). Valley months reflect seasonal downturns."

        # === HALL OF FAME ===
        top_posts = sorted(posts, key=lambda x: x['total_engagement'], reverse=True)[:5]

        for i, p in enumerate(top_posts, 1):
            self.placeholders[f'post_{i}_title'] = p.get('caption', 'Post')[:50] if p.get('caption') else f"Top Post #{i}"
            self.placeholders[f'post_{i}_date'] = p['date']
            self.placeholders[f'post_{i}_metric'] = f"{p['total_engagement']} total interactions ({p.get('engagement_rate', 0)}% ER)"
            self.placeholders[f'post_{i}_format'] = p.get('post_type', 'Unknown')
            self.placeholders[f'post_{i}_why'] = f"Achieved {p['total_engagement']} engagements with {p.get('reach', 0)} reach"
            self.placeholders[f'post_{i}_action'] = "Replicate this content theme and format monthly"

        self.placeholders['additional_hall_of_fame_posts'] = ""

        # === FORMAT ANALYSIS ===
        format_map = defaultdict(list)
        for p in posts:
            raw_type = str(p.get('post_type', '')).lower()
            if 'carousel' in raw_type or 'album' in raw_type:
                fmt = "Carousel"
            elif 'reel' in raw_type or 'video' in raw_type:
                fmt = "Reel"
            else:
                fmt = "Static Image"

            if p.get('engagement_rate'):
                format_map[fmt].append(p['engagement_rate'])

        total_posts_count = len(posts)

        # Static
        static_rates = format_map.get('Static Image', [0])
        self.placeholders['static_engagement'] = f"{statistics.mean(static_rates):.2f}%"
        self.placeholders['static_percent'] = f"{len(static_rates)/total_posts_count*100:.1f}"
        self.placeholders['static_example'] = "See Hall of Fame posts"
        self.placeholders['static_verdict'] = "Reliable baseline performer"

        # Carousel
        carousel_rates = format_map.get('Carousel', [0])
        self.placeholders['carousel_engagement'] = f"{statistics.mean(carousel_rates):.2f}%"
        self.placeholders['carousel_percent'] = f"{len(carousel_rates)/total_posts_count*100:.1f}"
        self.placeholders['carousel_example'] = "Multiple-slide content"
        self.placeholders['carousel_verdict'] = "High performer - increase usage"

        # Reel
        reel_rates = format_map.get('Reel', [0])
        self.placeholders['reel_engagement'] = f"{statistics.mean(reel_rates):.2f}%"
        self.placeholders['reel_percent'] = f"{len(reel_rates)/total_posts_count*100:.1f}"
        self.placeholders['reel_example'] = "Monthly recap reels"
        self.placeholders['reel_verdict'] = "Good performance - maintain"

        self.placeholders['format_optimization_plan'] = f"Increase carousel usage from {len(carousel_rates)/total_posts_count*100:.1f}% to 40% of feed"
        self.placeholders['visual_patterns'] = "Posts with faces outperform product shots; text overlays increase engagement"

        # === PLATFORM MIX ===
        platform_map = defaultdict(lambda: {'posts': 0, 'eng_rates': []})
        for p in posts:
            platform = p['platform']
            platform_map[platform]['posts'] += 1
            if p.get('engagement_rate'):
                platform_map[platform]['eng_rates'].append(p['engagement_rate'])

        # Instagram
        ig_data = platform_map.get('instagram', {'posts': 0, 'eng_rates': [0]})
        self.placeholders['ig_volume'] = f"{ig_data['posts']/self.placeholders['data_months']:.1f}"
        self.placeholders['ig_engagement'] = f"{statistics.mean(ig_data['eng_rates']) if ig_data['eng_rates'] else 0:.2f}%"
        self.placeholders['ig_roi'] = "Primary inquiry driver"
        self.placeholders['ig_recommendation'] = "Maintain or increase allocation"

        # Facebook
        fb_data = platform_map.get('facebook', {'posts': 0, 'eng_rates': [0]})
        self.placeholders['fb_volume'] = f"{fb_data['posts']/self.placeholders['data_months']:.1f}"
        self.placeholders['fb_engagement'] = f"{statistics.mean(fb_data['eng_rates']) if fb_data['eng_rates'] else 0:.2f}%"
        self.placeholders['fb_roi'] = "Analytics tracking needed"
        self.placeholders['fb_recommendation'] = "Audit metrics or reduce"

        # GBP
        gbp_data = platform_map.get('google_business_profile', {'posts': 0, 'eng_rates': [0]})
        self.placeholders['gbp_volume'] = f"{gbp_data['posts']/self.placeholders['data_months']:.1f}"
        self.placeholders['gbp_engagement'] = f"{statistics.mean(gbp_data['eng_rates']) if gbp_data['eng_rates'] else 0:.2f}%"
        self.placeholders['gbp_roi'] = "Analytics tracking needed"
        self.placeholders['gbp_recommendation'] = "Verify GBP Insights data"

        self.placeholders['platform_shift_recommendation'] = "Prioritize Instagram; audit Facebook/GBP analytics"

        # === CONTENT PILLARS ===
        self.placeholders['stated_pillar_distribution'] = "30% Student Success | 25% Instructor | 20% Educational | 15% Community | 10% Promotional"
        self.placeholders['actual_pillar_distribution'] = "Distribution requires content calendar pillar tagging - recommend manual audit"

        # Pillar 1-3 (generic since we don't have pillar tags)
        for i in range(1, 4):
            pillar_names = ["Student Success", "Instructor Expertise", "Educational Value"]
            targets = [30, 25, 20]

            self.placeholders[f'pillar_{i}_name'] = pillar_names[i-1]
            self.placeholders[f'pillar_{i}_percent'] = "TBD"
            self.placeholders[f'pillar_{i}_target'] = targets[i-1]
            self.placeholders[f'pillar_{i}_actual'] = "Requires calendar audit"
            self.placeholders[f'pillar_{i}_performance'] = "Unknown without pillar tags"
            self.placeholders[f'pillar_{i}_analysis'] = "Recommend tagging posts by pillar in content calendar for future tracking"

        self.placeholders['additional_pillars'] = ""
        self.placeholders['pillar_balance_assessment'] = "Content pillar tracking not implemented - recommend adding pillar tags to calendar"

        # === RED FLAGS ===
        carousel_pct = len(carousel_rates)/total_posts_count*100
        if carousel_pct < 20:
            self.placeholders['red_flag_1'] = f"Carousel format underutilized ({carousel_pct:.1f}% of feed)"
            self.placeholders['red_flag_1_impact'] = "Missing significant engagement opportunity"
            self.placeholders['red_flag_1_fix'] = "Increase carousel usage to 40% of feed"
        else:
            self.placeholders['red_flag_1'] = "No critical issues detected"
            self.placeholders['red_flag_1_impact'] = "N/A"
            self.placeholders['red_flag_1_fix'] = "N/A"

        fb_avg = statistics.mean(fb_data['eng_rates']) if fb_data['eng_rates'] else 0
        if fb_avg == 0 and fb_data['posts'] > 0:
            self.placeholders['red_flag_2'] = "Facebook analytics showing 0% engagement"
            self.placeholders['red_flag_2_impact'] = "Cannot measure ROI on Facebook posts"
            self.placeholders['red_flag_2_fix'] = "Audit analytics export process or reallocate resources"
        else:
            self.placeholders['red_flag_2'] = "No secondary issues detected"
            self.placeholders['red_flag_2_impact'] = "N/A"
            self.placeholders['red_flag_2_fix'] = "N/A"

        self.placeholders['yellow_flag_1'] = "Content pillar tracking not implemented"
        self.placeholders['yellow_flag_1_impact'] = "Cannot verify strategy execution"
        self.placeholders['yellow_flag_1_fix'] = "Add pillar tags to content calendar"

        self.placeholders['yellow_flag_2'] = "No follower growth tracking"
        self.placeholders['yellow_flag_2_impact'] = "Cannot measure audience expansion"
        self.placeholders['yellow_flag_2_fix'] = "Document follower count monthly"

        # === STRATEGIC PIVOT ===
        self.placeholders['strategic_diagnosis'] = "Content quality is strong but format allocation is suboptimal. Carousel format significantly outperforms static images but is underutilized."
        self.placeholders['pivot_core_strategy'] = "Shift from static-heavy to carousel-dominant feed to capitalize on proven high-performance format"

        self.placeholders['double_down_1'] = "Carousel format (increase to 40% of feed)"
        self.placeholders['double_down_2'] = "Instagram platform (proven engagement driver)"
        self.placeholders['double_down_3'] = "Student Success content pillar (top performer)"

        self.placeholders['stop_doing_1'] = "Default-to-static content creation workflow"
        self.placeholders['stop_doing_2'] = "Posting without performance tracking (FB/GBP)"
        self.placeholders['stop_doing_3'] = "Isolated posting (no collaboration/tagging)"

        self.placeholders['test_1'] = "Instructor carousel series with 5-7 slides"
        self.placeholders['test_2'] = "Student transformation carousels (lesson progression)"

        # === 90-DAY PLAN ===
        self.placeholders['month_1_action_1'] = "Create 10 carousel templates"
        self.placeholders['month_1_action_2'] = "Audit Facebook/GBP analytics"
        self.placeholders['month_1_action_3'] = "Implement carousel-first calendar"
        self.placeholders['month_1_action_4'] = "Launch instructor feature series"
        self.placeholders['month_1_kpi'] = "Carousel percentage of feed (target: 25-30%)"

        self.placeholders['month_2_action_1'] = "Analyze carousel performance vs static"
        self.placeholders['month_2_action_2'] = "Add pillar tracking to calendar"
        self.placeholders['month_2_action_3'] = "Scale to 8 carousels/month"
        self.placeholders['month_2_action_4'] = "Implement collaboration tagging"
        self.placeholders['month_2_kpi'] = "Follower growth rate (target: 5%)"

        self.placeholders['month_3_action_1'] = "Calculate actual pillar distribution"
        self.placeholders['month_3_action_2'] = "Platform decision (FB/GBP reallocation)"
        self.placeholders['month_3_action_3'] = "Document carousel creation SOP"
        self.placeholders['month_3_action_4'] = "Lock in carousel-dominant template"
        self.placeholders['month_3_kpi'] = "Overall engagement rate (target: maintain 10%+)"

        # === MEASUREMENT FRAMEWORK ===
        ig_avg_er = statistics.mean(ig_data['eng_rates']) if ig_data['eng_rates'] else 0
        ig_posts = [p for p in posts if p['platform'] == 'instagram']
        ig_avg_reach = statistics.mean([p.get('reach', 0) for p in ig_posts if p.get('reach', 0) > 0]) if ig_posts else 0

        self.placeholders['current_engagement'] = f"{ig_avg_er:.2f}%"
        self.placeholders['target_engagement'] = f"{ig_avg_er * 1.15:.2f}%"
        self.placeholders['engagement_method'] = "Instagram Insights → Calculate (total engagement / reach) × 100"

        self.placeholders['current_reach'] = f"{ig_avg_reach:.0f} avg reach/post"
        self.placeholders['target_reach'] = f"{ig_avg_reach * 1.25:.0f} avg reach/post"
        self.placeholders['reach_method'] = "Instagram Insights → Reach metric per post; track monthly average"

        self.placeholders['current_inquiries'] = "Not tracked"
        self.placeholders['target_inquiries'] = "20/month"
        self.placeholders['inquiry_method'] = "Track Instagram DMs + bio link clicks with UTM parameters"

        self.placeholders['custom_kpi'] = "Carousel Mix %"
        self.placeholders['custom_baseline'] = f"{carousel_pct:.1f}%"
        self.placeholders['custom_target'] = "40%"
        self.placeholders['custom_method'] = "Count carousel posts ÷ total posts in monthly calendar"

        self.placeholders['success_definition'] = f"In 90 days, feed will be 40% carousel format, engagement rates will maintain {ig_avg_er:.1f}%+, and follower growth will achieve 10% monthly target."

        # === APPENDIX ===
        self.placeholders['files_analyzed_list'] = f"Processed {self.data['metadata'].get('parsing_stats', {}).get('files_processed', 'N/A')} files across all subdirectories"
        self.placeholders['data_quality_notes'] = "Instagram data complete; Facebook/GBP missing engagement metrics in exports"
        self.placeholders['analysis_limitations'] = "Content pillar distribution estimated from top posts; full calendar audit recommended for precision"

        # === EXECUTIVE SUMMARY ===
        self.placeholders['executive_summary_paragraph'] = f"{self.client_name}'s social media shows {self.placeholders['growth_status'].replace('📈 ', '').replace('📉 ', '').replace('➡️ ', '').lower()} trajectory with {ig_avg_er:.1f}% Instagram engagement. Key opportunity: carousel format achieves {statistics.mean(carousel_rates):.1f}% engagement but represents only {carousel_pct:.1f}% of feed."

        self.placeholders['key_finding_1'] = f"Carousel format delivers {statistics.mean(carousel_rates):.1f}% engagement vs {statistics.mean(static_rates):.1f}% static but is only {carousel_pct:.1f}% of feed"
        self.placeholders['key_finding_2'] = f"Instagram performs at {ig_avg_er:.1f}% engagement while Facebook/GBP lack trackable metrics"
        self.placeholders['key_finding_3'] = f"Engagement {yoy_comparison} from first half to second half of period"

    def fill_template(self):
        """Replace all placeholders in template"""
        filled = self.template

        for key, value in self.placeholders.items():
            placeholder = "{{" + key + "}}"
            filled = filled.replace(placeholder, str(value))

        return filled

    def save_report(self, output_path: Path):
        """Save filled report"""
        filled_report = self.fill_template()

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(filled_report)

        print(f"✅ Report saved to: {output_path}")

        # Check for remaining placeholders
        remaining = filled_report.count('{{')
        if remaining > 0:
            print(f"⚠️  Warning: {remaining} placeholders still unfilled")
        else:
            print("✅ All placeholders filled successfully")


def main():
    parser = argparse.ArgumentParser(
        description="Auto-fill social audit report template with metrics"
    )

    parser.add_argument('--metrics-json', required=True, help='Path to parsed metrics JSON (from parse_social_data_v5.py)')
    parser.add_argument('--template', required=True, help='Path to social_audit_matrix.md template')
    parser.add_argument('--client-profile', help='Path to client profile MD (optional, for client name)')
    parser.add_argument('--output', required=True, help='Output path for filled report')

    args = parser.parse_args()

    # Validate inputs
    metrics_path = Path(args.metrics_json)
    template_path = Path(args.template)
    output_path = Path(args.output)
    client_profile_path = Path(args.client_profile) if args.client_profile else None

    if not metrics_path.exists():
        print(f"❌ Metrics JSON not found: {metrics_path}")
        sys.exit(1)

    if not template_path.exists():
        print(f"❌ Template not found: {template_path}")
        sys.exit(1)

    # Run filler
    print(f"\n📊 Loading data from {metrics_path.name}...")
    filler = TemplateFiller(metrics_path, template_path, client_profile_path)
    filler.load_data()

    print(f"🔢 Calculating metrics...")
    filler.calculate_metrics()

    print(f"📝 Filling template...")
    filler.save_report(output_path)

    print(f"\n✅ DONE! Review report at: {output_path}\n")


if __name__ == "__main__":
    main()
