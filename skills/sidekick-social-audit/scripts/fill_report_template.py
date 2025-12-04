#!/usr/bin/env python3
import argparse, json, sys, re, logging
from pathlib import Path
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def main():
    p = argparse.ArgumentParser(); p.add_argument('--client-folder', required=True)
    args = p.parse_args()
    
    client_path = Path(args.client_folder)
    audit_dir = client_path / "07_Marketing_Channels/Social_Media/04_Audit_Reports"
    metrics_path = audit_dir / "metrics_summary.json"
    tpl_path = Path(__file__).parent.parent / "references/social_audit_matrix.md"
    
    if not tpl_path.exists() or not metrics_path.exists(): sys.exit("❌ Files missing")
    
    with open(metrics_path) as f: data = json.load(f)
    with open(tpl_path) as f: text = f.read()
    
    rep = {
        '{{client_name}}': client_path.name.replace("client-","").title(),
        '{{report_date}}': str(datetime.now().date()),
        '{{growth_status}}': data['macro']['growth_status'],
        '{{yoy_comparison}}': data['macro']['yoy_comparison'],
        '{{trajectory_analysis}}': data['macro']['trajectory_analysis'],
        '{{start_date}}': data['meta']['start_date'],
        '{{end_date}}': data['meta']['end_date'],
        '{{data_months}}': str(data['meta']['total_months']),
        '{{peak_months_list}}': data['seasonality']['peak_months'],
        '{{valley_months_list}}': data['seasonality']['valley_months'],
        '{{seasonality_implications}}': data['seasonality']['implications'],
        '{{executive_summary_paragraph}}': "Analysis Complete. See Agency Brain for strategic context.",
        '{{strategic_diagnosis}}': data['strategic_pivot']['diagnosis'],
        '{{pivot_core_strategy}}': data['strategic_pivot']['core_strategy']
    }
    
    # Platforms
    p_dict = {p['platform']:p for p in data['mechanics']['platforms']}
    for k in ['instagram','facebook','google_business_profile']:
        key = 'ig' if k=='instagram' else ('fb' if k=='facebook' else 'gbp')
        obj = p_dict.get(k, {'volume':0, 'avg_engagement':0, 'recommendation':'No Data'})
        rep[f'{{{{{key}_volume}}}}'] = str(obj.get('volume',0))
        rep[f'{{{{{key}_engagement}}}}'] = str(obj.get('avg_engagement',0)) + "%"
        rep[f'{{{{{key}_recommendation}}}}'] = obj.get('recommendation','')

    # Formats
    f_dict = {f['format']:f for f in data['mechanics']['formats']}
    for k in ['Static','Carousel','Reel']:
        key = k.lower()
        obj = f_dict.get(k, {'percent_of_feed':0, 'avg_engagement':0, 'verdict':'No Data'})
        rep[f'{{{{{key}_percent}}}}'] = str(obj.get('percent_of_feed',0))
        rep[f'{{{{{key}_engagement}}}}'] = str(obj.get('avg_engagement',0)) + "%"
        rep[f'{{{{{key}_verdict}}}}'] = obj.get('verdict','')

    # Hall of Fame (Pad to 3)
    hof = data['hall_of_fame']
    while len(hof) < 3: hof.append({'format':'N/A','date':'N/A','metrics':'N/A','why_legendary':'N/A','reboot_action':'N/A'})
    for i in range(2): # Template has 2 spots
        h = hof[i]
        rep[f'{{{{post_{i+1}_title}}}}'] = f"{h['format']} - {h['date']}"
        rep[f'{{{{post_{i+1}_metric}}}}'] = h['metrics']
        rep[f'{{{{post_{i+1}_why}}}}'] = h['why_legendary']
        rep[f'{{{{post_{i+1}_action}}}}'] = h['reboot_action']

    # Red Flags (Pad to 2)
    rf = data['red_flags']
    while len(rf) < 2: rf.append({'name':'Monitoring','fix':'Continue'})
    for i in range(2):
        rep[f'{{{{red_flag_{i+1}}}}}'] = rf[i]['name']
        rep[f'{{{{red_flag_{i+1}_fix}}}}'] = rf[i]['fix']

    for k,v in rep.items(): text = text.replace(k, str(v))

    out_path = audit_dir / f"{client_path.name}_Audit_COMPLETE.md"
    with open(out_path, 'w') as f: f.write(text)
    logger.info(f"Report written: {out_path}")

if __name__ == "__main__":
    main()
