#!/usr/bin/env python3
"""
Calculate Engagement Script
Standardized engagement rate calculations across social platforms

Usage:
    python calculate_engagement.py --platform instagram --likes 150 --comments 12 --saves 45 --reach 2000
    python calculate_engagement.py --json-file data.json --output enriched.json
    python calculate_engagement.py --platform facebook --reactions 200 --comments 15 --shares 8 --reach 5000
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, Any, Optional


class EngagementCalculator:
    """Calculate standardized engagement rates across platforms"""
    
    # Platform-specific formulas
    FORMULAS = {
        'instagram': {
            'name': 'Instagram',
            'formula': '(likes + comments + shares + saves) / reach * 100',
            'metrics': ['likes', 'comments', 'shares', 'saves'],
            'denominator': 'reach'
        },
        'facebook': {
            'name': 'Facebook',
            'formula': '(reactions + comments + shares) / reach * 100',
            'metrics': ['reactions', 'likes', 'comments', 'shares'],  # reactions or likes
            'denominator': 'reach'
        },
        'google_business_profile': {
            'name': 'Google Business Profile',
            'formula': '(views + clicks + calls) / impressions * 100',
            'metrics': ['views', 'clicks', 'calls'],
            'denominator': 'impressions'
        },
        'linkedin': {
            'name': 'LinkedIn',
            'formula': '(likes + comments + shares + clicks) / impressions * 100',
            'metrics': ['likes', 'comments', 'shares', 'clicks'],
            'denominator': 'impressions'
        },
        'twitter': {
            'name': 'Twitter/X',
            'formula': '(likes + retweets + replies) / impressions * 100',
            'metrics': ['likes', 'retweets', 'replies'],
            'denominator': 'impressions'
        }
    }
    
    # Industry benchmarks (average engagement rates by platform)
    BENCHMARKS = {
        'instagram': {
            'excellent': 6.0,
            'good': 3.0,
            'average': 1.5,
            'poor': 0.5
        },
        'facebook': {
            'excellent': 3.0,
            'good': 1.5,
            'average': 0.5,
            'poor': 0.1
        },
        'google_business_profile': {
            'excellent': 8.0,
            'good': 4.0,
            'average': 2.0,
            'poor': 0.5
        },
        'linkedin': {
            'excellent': 5.0,
            'good': 2.0,
            'average': 1.0,
            'poor': 0.2
        },
        'twitter': {
            'excellent': 2.0,
            'good': 0.5,
            'average': 0.2,
            'poor': 0.05
        }
    }
    
    @classmethod
    def calculate(cls, platform: str, metrics: Dict[str, float]) -> Optional[float]:
        """
        Calculate engagement rate for a post
        
        Args:
            platform: Platform name (instagram, facebook, etc.)
            metrics: Dictionary of metric values
        
        Returns:
            Engagement rate as percentage (e.g., 4.25 for 4.25%)
        """
        
        platform = platform.lower()
        
        if platform not in cls.FORMULAS:
            return None
        
        formula = cls.FORMULAS[platform]
        
        # Get denominator (reach or impressions)
        denominator = metrics.get(formula['denominator'], 0)
        
        if denominator == 0:
            return None
        
        # Sum up engagement metrics
        total_engagement = 0
        
        for metric in formula['metrics']:
            value = metrics.get(metric, 0)
            total_engagement += value
        
        # Calculate percentage
        engagement_rate = (total_engagement / denominator) * 100
        
        return round(engagement_rate, 2)
    
    @classmethod
    def classify(cls, platform: str, engagement_rate: float) -> str:
        """
        Classify engagement rate as excellent/good/average/poor
        
        Args:
            platform: Platform name
            engagement_rate: Engagement rate percentage
        
        Returns:
            Classification string
        """
        
        platform = platform.lower()
        
        if platform not in cls.BENCHMARKS:
            return 'unknown'
        
        benchmarks = cls.BENCHMARKS[platform]
        
        if engagement_rate >= benchmarks['excellent']:
            return 'excellent'
        elif engagement_rate >= benchmarks['good']:
            return 'good'
        elif engagement_rate >= benchmarks['average']:
            return 'average'
        else:
            return 'poor'
    
    @classmethod
    def enrich_post(cls, post: Dict[str, Any]) -> Dict[str, Any]:
        """
        Add calculated engagement rate to post data
        
        Args:
            post: Post dictionary
        
        Returns:
            Enriched post with engagement_rate and classification
        """
        
        platform = post.get('platform', '').lower()
        
        # Skip if already has engagement rate
        if 'engagement_rate' in post and post['engagement_rate'] is not None:
            rate = post['engagement_rate']
        else:
            # Calculate engagement rate
            rate = cls.calculate(platform, post)
            if rate is not None:
                post['engagement_rate'] = rate
        
        # Add classification
        if rate is not None:
            post['engagement_classification'] = cls.classify(platform, rate)
        
        return post
    
    @classmethod
    def process_json_file(cls, input_path: Path, output_path: Path):
        """
        Process JSON file and add engagement calculations
        
        Args:
            input_path: Input JSON file path
            output_path: Output JSON file path
        """
        
        try:
            with open(input_path, 'r') as f:
                data = json.load(f)
        except Exception as e:
            print(f"❌ Failed to read {input_path}: {e}")
            sys.exit(1)
        
        # Process posts
        posts = data.get('posts', [])
        
        enriched_count = 0
        skipped_count = 0
        
        for post in posts:
            original_rate = post.get('engagement_rate')
            enriched_post = cls.enrich_post(post)
            
            if 'engagement_rate' in enriched_post:
                if original_rate is None:
                    enriched_count += 1
            else:
                skipped_count += 1
        
        # Update metadata
        if 'metadata' not in data:
            data['metadata'] = {}
        
        data['metadata']['enrichment'] = {
            'calculated': enriched_count,
            'skipped': skipped_count,
            'total': len(posts)
        }
        
        # Save enriched data
        try:
            with open(output_path, 'w') as f:
                json.dump(data, f, indent=2)
            
            print(f"✅ Processed {len(posts)} posts")
            print(f"   Calculated: {enriched_count}")
            print(f"   Skipped: {skipped_count}")
            print(f"   Saved to: {output_path}")
            
        except Exception as e:
            print(f"❌ Failed to write {output_path}: {e}")
            sys.exit(1)
    
    @classmethod
    def print_formula_guide(cls):
        """Print guide to engagement formulas"""
        
        print("\n" + "="*60)
        print("ENGAGEMENT RATE FORMULAS")
        print("="*60 + "\n")
        
        for platform, formula_data in cls.FORMULAS.items():
            print(f"📱 {formula_data['name']}")
            print(f"   Formula: {formula_data['formula']}")
            print(f"   Metrics: {', '.join(formula_data['metrics'])}")
            
            if platform in cls.BENCHMARKS:
                benchmarks = cls.BENCHMARKS[platform]
                print(f"   Benchmarks:")
                print(f"     • Excellent: ≥{benchmarks['excellent']}%")
                print(f"     • Good: ≥{benchmarks['good']}%")
                print(f"     • Average: ≥{benchmarks['average']}%")
                print(f"     • Poor: <{benchmarks['average']}%")
            
            print()


def main():
    parser = argparse.ArgumentParser(
        description="Calculate standardized engagement rates"
    )
    
    parser.add_argument(
        '--platform',
        choices=['instagram', 'facebook', 'google_business_profile', 'linkedin', 'twitter'],
        help='Social media platform'
    )
    parser.add_argument(
        '--likes',
        type=int,
        help='Number of likes/reactions'
    )
    parser.add_argument(
        '--comments',
        type=int,
        help='Number of comments'
    )
    parser.add_argument(
        '--shares',
        type=int,
        help='Number of shares'
    )
    parser.add_argument(
        '--saves',
        type=int,
        help='Number of saves (Instagram)'
    )
    parser.add_argument(
        '--reactions',
        type=int,
        help='Number of reactions (Facebook)'
    )
    parser.add_argument(
        '--clicks',
        type=int,
        help='Number of clicks'
    )
    parser.add_argument(
        '--calls',
        type=int,
        help='Number of calls (Google Business Profile)'
    )
    parser.add_argument(
        '--views',
        type=int,
        help='Number of views'
    )
    parser.add_argument(
        '--reach',
        type=int,
        help='Reach (unique viewers)'
    )
    parser.add_argument(
        '--impressions',
        type=int,
        help='Impressions (total views)'
    )
    parser.add_argument(
        '--json-file',
        help='JSON file to process (from parse_social_data.py)'
    )
    parser.add_argument(
        '--output',
        help='Output file path (for JSON processing)'
    )
    parser.add_argument(
        '--formulas',
        action='store_true',
        help='Print formula guide and exit'
    )
    
    args = parser.parse_args()
    
    # Print formulas
    if args.formulas:
        EngagementCalculator.print_formula_guide()
        sys.exit(0)
    
    # Process JSON file
    if args.json_file:
        if not args.output:
            print("❌ --output required when using --json-file")
            sys.exit(1)
        
        EngagementCalculator.process_json_file(
            Path(args.json_file),
            Path(args.output)
        )
        sys.exit(0)
    
    # Calculate single post
    if not args.platform:
        print("❌ --platform required for single post calculation")
        parser.print_help()
        sys.exit(1)
    
    # Build metrics dict
    metrics = {}
    
    if args.likes is not None:
        metrics['likes'] = args.likes
    if args.comments is not None:
        metrics['comments'] = args.comments
    if args.shares is not None:
        metrics['shares'] = args.shares
    if args.saves is not None:
        metrics['saves'] = args.saves
    if args.reactions is not None:
        metrics['reactions'] = args.reactions
    if args.clicks is not None:
        metrics['clicks'] = args.clicks
    if args.calls is not None:
        metrics['calls'] = args.calls
    if args.views is not None:
        metrics['views'] = args.views
    if args.reach is not None:
        metrics['reach'] = args.reach
    if args.impressions is not None:
        metrics['impressions'] = args.impressions
    
    # Calculate
    rate = EngagementCalculator.calculate(args.platform, metrics)
    
    if rate is None:
        print("❌ Unable to calculate engagement rate")
        print("   Missing required metrics for platform")
        sys.exit(1)
    
    classification = EngagementCalculator.classify(args.platform, rate)
    
    print(f"\n{'='*60}")
    print(f"ENGAGEMENT RATE: {rate}%")
    print(f"CLASSIFICATION: {classification.upper()}")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
