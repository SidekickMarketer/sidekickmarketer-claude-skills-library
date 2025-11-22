#!/usr/bin/env python3
"""
Setup Client Folder Script
Creates standardized folder structure for Sidekick Marketer clients

Usage:
    python setup_client_folder.py --client-name "Cincinnati Music Academy" --output-dir ./clients
    python setup_client_folder.py --client-name "CMA" --output-dir ./clients --short-code cma
"""

import argparse
import os
import sys
from pathlib import Path
from datetime import datetime


def create_folder_structure(client_name: str, output_dir: str, short_code: str = None) -> Path:
    """
    Create standardized client folder structure
    
    Args:
        client_name: Full client name (e.g., "Cincinnati Music Academy")
        output_dir: Parent directory where client folder will be created
        short_code: Optional short code for folder name (e.g., "cma")
    
    Returns:
        Path to created client folder
    """
    # Generate folder name
    if short_code:
        folder_name = f"client-{short_code.lower()}"
    else:
        # Convert client name to folder-safe format
        folder_name = f"client-{client_name.lower().replace(' ', '-').replace('&', 'and')}"
    
    # Create base client folder
    client_folder = Path(output_dir) / folder_name
    
    if client_folder.exists():
        response = input(f"⚠️  Folder '{folder_name}' already exists. Overwrite? (y/n): ")
        if response.lower() != 'y':
            print("❌ Setup cancelled.")
            sys.exit(0)
    
    client_folder.mkdir(parents=True, exist_ok=True)
    print(f"✅ Created: {client_folder}")
    
    # Define folder structure
    folders = [
        "01_Admin_Legal",
        "02_Onboarding_Access",
        "03_Brand_Assets",
        "04_Marketing_Deliverables",
        "05_Reports_Analytics",
        "06_Paid_Ads",
        "07_Social_Media",
        "07_Social_Media/01_Content_Calendars",
        "07_Social_Media/02_Performance_Data",
        "07_Social_Media/03_Post_Archive",
        "07_Social_Media/04_Audit_Reports",
        "08_SEO",
        "09_Website",
        "10_Email_Marketing",
        "90_Archive"
    ]
    
    # Create all folders
    for folder in folders:
        folder_path = client_folder / folder
        folder_path.mkdir(parents=True, exist_ok=True)
        print(f"  📁 {folder}")
    
    return client_folder


def create_client_profile(client_folder: Path, client_name: str):
    """Create CLIENT_PROFILE.md template"""
    
    # Read template
    template_path = Path(__file__).parent.parent / "references" / "CLIENT_PROFILE_TEMPLATE.md"
    
    if template_path.exists():
        with open(template_path, 'r') as f:
            template = f.read()
    else:
        # Fallback basic template
        template = f"""# Client Profile: {client_name}

**Last Updated:** {datetime.now().strftime('%Y-%m-%d')}
**Account Manager:** [YOUR NAME]
**Active Since:** [START DATE]

[TODO: Fill out client details]
"""
    
    # Replace placeholders
    content = template.replace("[CLIENT NAME]", client_name)
    content = content.replace("[DATE]", datetime.now().strftime('%Y-%m-%d'))
    
    # Generate filename
    safe_name = client_name.upper().replace(' ', '_').replace('&', 'AND')
    filename = f"00_{safe_name}_CLIENT_PROFILE.md"
    
    # Write file
    profile_path = client_folder / filename
    with open(profile_path, 'w') as f:
        f.write(content)
    
    print(f"✅ Created: {filename}")
    return profile_path


def create_social_strategy(client_folder: Path, client_name: str):
    """Create SOCIAL_STRATEGY.md template in 07_Social_Media"""
    
    # Read template
    template_path = Path(__file__).parent.parent / "references" / "SOCIAL_STRATEGY_TEMPLATE.md"
    
    if template_path.exists():
        with open(template_path, 'r') as f:
            template = f.read()
    else:
        # Fallback basic template
        template = f"""# Social Media Strategy: {client_name}

**Strategy Period:** {datetime.now().year}-{datetime.now().year + 1}
**Last Updated:** {datetime.now().strftime('%Y-%m-%d')}

[TODO: Define content pillars and strategy]
"""
    
    # Replace placeholders
    content = template.replace("[CLIENT NAME]", client_name)
    content = content.replace("[DATE]", datetime.now().strftime('%Y-%m-%d'))
    content = content.replace("[e.g., 2024-2025]", f"{datetime.now().year}-{datetime.now().year + 1}")
    
    # Write file
    strategy_path = client_folder / "07_Social_Media" / "00_SOCIAL_STRATEGY.md"
    with open(strategy_path, 'w') as f:
        f.write(content)
    
    print(f"✅ Created: 07_Social_Media/00_SOCIAL_STRATEGY.md")
    return strategy_path


def create_readme_files(client_folder: Path):
    """Create README files in key directories"""
    
    readmes = {
        "07_Social_Media/01_Content_Calendars/README.md": """# Content Calendars

Store monthly content calendars here.

**File naming convention:**
- `YYYY-MM_Content_Calendar.csv`
- Example: `2024-01_Content_Calendar.csv`

**Required columns:**
- Date
- Platform
- Format
- Caption
- Pillar
- Status
""",
        "07_Social_Media/02_Performance_Data/README.md": """# Performance Data

Store analytics exports here.

**File naming convention:**
- `Platform_Analytics_YYYY_Q#.csv` (for quarterly exports)
- `Platform_Analytics_YYYY-MM.csv` (for monthly exports)
- Examples: 
  - `Instagram_Analytics_2024_Q1.csv`
  - `Facebook_Analytics_2024-01.csv`

**Required columns:**
- Date
- Post_ID
- Type
- Likes
- Comments
- Shares
- Saves (if available)
- Reach
- Impressions
""",
        "07_Social_Media/03_Post_Archive/README.md": """# Post Archive

Store PDF exports of actual posts here (optional).

**File naming convention:**
- `YYYY-MM_Platform_Posts.pdf`
- Example: `2024-01_Instagram_Posts.pdf`

**Sources:**
- Platform exports (Instagram Insights, Meta Business Suite)
- Screenshot compilations
- Canva design exports
""",
        "07_Social_Media/04_Audit_Reports/README.md": """# Audit Reports

Completed social media audit reports will be saved here.

**File naming convention:**
- `YYYY-MM_Social_Audit.md`
- Example: `2024-06_Social_Audit.md`
"""
    }
    
    for path, content in readmes.items():
        readme_path = client_folder / path
        with open(readme_path, 'w') as f:
            f.write(content)
        print(f"  📄 {path}")


def create_start_here_doc(client_folder: Path, client_name: str):
    """Create 00_START_HERE.md with onboarding checklist"""
    
    content = f"""# START HERE: {client_name}

Welcome! This folder contains all files and assets for {client_name}.

## 📋 Onboarding Checklist

### Week 1: Setup
- [ ] Complete `00_{client_name.upper().replace(' ', '_')}_CLIENT_PROFILE.md`
- [ ] Upload brand assets to `03_Brand_Assets/`
- [ ] Document platform access in `02_Onboarding_Access/`
- [ ] Create signed agreements in `01_Admin_Legal/`

### Week 2: Strategy
- [ ] Complete `07_Social_Media/00_SOCIAL_STRATEGY.md`
- [ ] Define content pillars with target percentages
- [ ] Document posting frequency by platform
- [ ] Set KPI targets

### Week 3: Data Migration
- [ ] Export historical content calendars
- [ ] Rename to format: `YYYY-MM_Content_Calendar.csv`
- [ ] Place in `07_Social_Media/01_Content_Calendars/`

### Week 4: Analytics Setup
- [ ] Export platform analytics (6-12 months)
- [ ] Rename to format: `Platform_Analytics_YYYY_Q#.csv`
- [ ] Place in `07_Social_Media/02_Performance_Data/`

### Ready for Audit
- [ ] Run validation: `python scripts/validate_folder_structure.py --path [path]`
- [ ] All critical files in place
- [ ] Ready to run social audit skill

---

## 📁 Folder Structure

```
{client_folder.name}/
├── 00_{client_name.upper().replace(' ', '_')}_CLIENT_PROFILE.md   ← Start here
├── 00_START_HERE.md                          ← This file
├── 01_Admin_Legal/                            → Contracts, agreements
├── 02_Onboarding_Access/                      → Login credentials
├── 03_Brand_Assets/                           → Logos, fonts, colors
├── 04_Marketing_Deliverables/                 → All deliverables
├── 05_Reports_Analytics/                      → Monthly reports
├── 06_Paid_Ads/                               → Ad campaigns
├── 07_Social_Media/                           → Social content & strategy
│   ├── 00_SOCIAL_STRATEGY.md                  ← Define pillars here
│   ├── 01_Content_Calendars/                  → Historical posts
│   ├── 02_Performance_Data/                   → Analytics exports
│   ├── 03_Post_Archive/                       → PDF post exports
│   └── 04_Audit_Reports/                      → Generated audits
├── 08_SEO/                                    → SEO work
├── 09_Website/                                → Website files
├── 10_Email_Marketing/                        → Email campaigns
└── 90_Archive/                                → Old/inactive files
```

---

## 🎯 Quick Actions

**Run Social Audit:**
```bash
python scripts/validate_folder_structure.py --path [path-to-this-folder]
# Then use social audit skill with Claude
```

**Need Help?**
- See README files in each subfolder for file naming conventions
- Templates available in `references/` directory
- Contact your account manager

---

*Last updated: {datetime.now().strftime('%Y-%m-%d')}*
"""
    
    start_path = client_folder / "00_START_HERE.md"
    with open(start_path, 'w') as f:
        f.write(content)
    
    print(f"✅ Created: 00_START_HERE.md")


def main():
    parser = argparse.ArgumentParser(
        description="Setup standardized folder structure for Sidekick Marketer clients"
    )
    parser.add_argument(
        '--client-name',
        required=True,
        help='Full client name (e.g., "Cincinnati Music Academy")'
    )
    parser.add_argument(
        '--output-dir',
        required=True,
        help='Parent directory where client folder will be created'
    )
    parser.add_argument(
        '--short-code',
        help='Optional short code for folder name (e.g., "cma")'
    )
    
    args = parser.parse_args()
    
    print("\n🚀 Setting up client folder structure...\n")
    
    # Create folder structure
    client_folder = create_folder_structure(
        args.client_name,
        args.output_dir,
        args.short_code
    )
    
    print("\n📝 Creating template files...\n")
    
    # Create template files
    create_client_profile(client_folder, args.client_name)
    create_social_strategy(client_folder, args.client_name)
    create_readme_files(client_folder)
    create_start_here_doc(client_folder, args.client_name)
    
    print(f"\n✅ Setup complete! Client folder ready at:\n   {client_folder.absolute()}\n")
    print("📋 Next steps:")
    print("   1. Fill out CLIENT_PROFILE.md")
    print("   2. Define strategy in 07_Social_Media/00_SOCIAL_STRATEGY.md")
    print("   3. Import historical data (calendars, analytics)")
    print("   4. Run validation: python scripts/validate_folder_structure.py\n")


if __name__ == "__main__":
    main()
