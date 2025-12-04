#!/usr/bin/env python3
import argparse, os
from pathlib import Path
def create(name, out, short):
    root = Path(out) / f"client-{short or name.lower().replace(' ','-')}"
    root.mkdir(parents=True, exist_ok=True)
    for f in ["07_Marketing_Channels/Social_Media/01_Content_Calendars", "07_Marketing_Channels/Social_Media/02_Performance_Data", "07_Marketing_Channels/Social_Media/04_Audit_Reports"]:
        (root/f).mkdir(parents=True, exist_ok=True)
    (root/f"00_{name.replace(' ','_')}_PROFILE.md").touch()
    (root/"07_Marketing_Channels/Social_Media/00_SOCIAL_STRATEGY.md").touch()
    print(f"✅ Created {root}")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument('--client-name'); p.add_argument('--output-dir'); p.add_argument('--short-code')
    a = p.parse_args()
    create(a.client_name, a.output_dir, a.short_code)
