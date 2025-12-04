---
name: sidekick-social-audit
description: Rigorous forensic audit of client social media history analyzing long-term trends, seasonality, platform mix, and format effectiveness within Sidekick's photo-first service model. Use when conducting social media audits, performance analysis, or strategy pivots for any Sidekick Marketer client. Works with standardized client folder structure.
---

# Sidekick Marketer: Full-History Social Audit

## Objective
Perform a forensic audit of a client's social media history. Move beyond "vanity metrics" to identify the specific mechanics driving business results **within Sidekick's photo-first service model**.

**Scope:** Review the **ENTIRE** available history to understand trajectory, but weight technical analysis (formats/algorithms) toward the last 6-12 months.

## Phase 1: Archeology (Data Ingest)

### Step 1: Validate Structure
Run validation: `python scripts/validate_folder_structure.py --path "{{client_folder_path}}"`
*   If validation fails, review output or attempt adaptive discovery.

### Step 2: Load Context
1.  **Profile:** Read `00_[CLIENT]_CLIENT_PROFILE.md`.
2.  **Strategy:** Read `07_Social_Media/00_SOCIAL_STRATEGY.md`. (Flag if missing).

### Step 3: Ingest & Process Data
1.  **Parse Data:** `python scripts/parse_social_data.py --search-dir "{{client_folder_path}}/07_Social_Media/02_Performance_Data/" --output temp_data.json`
2.  **Calculate Metrics:** `python scripts/calculate_engagement.py --json-file temp_data.json --output enriched_data.json`
3.  **Check Freshness:** Flag if data is >3 months old.

## Phase 2: The Macro Analysis
*Use the processed data to determine:*
1.  **Growth Trajectory:** Year-over-Year comparison.
2.  **Seasonality:** Peak months vs. Valley months.
3.  **"Hall of Fame":** Identify Top 5 Posts of **All Time**.

## Phase 3: The Technical Deep Dive
*Analyze last 6-12 months.*

### A. Format Forensics (Photo-First)
*   **Calculations:** Compare Avg Engagement Rate (Static vs Carousel vs Reel).
*   **Constraint:** Do NOT recommend daily Stories/TikToks.
*   **Flag:** If Carousels outperform Static images.

### B. Platform Mix & ROI
*   Calculate volume vs. engagement for IG, FB, GBP.

## Phase 4: Reporting (Automated)

### Step 1: Generate Metrics Summary
Run the analyst script:
`python scripts/generate_report_metrics.py --input enriched_data.json --output metrics.json`

### Step 2: Auto-Fill Template
Run the templating script to create the draft:
`python scripts/fill_report_template.py --metrics metrics.json --template references/social_audit_matrix.md --output draft_report.md --client-name "{{client_name}}"`

### Step 3: Human Strategy (The "Brain" Work)
Open `draft_report.md`. The numbers are filled. You must now write:
*   **Executive Summary:** Synthesize the data into a story.
*   **Strategic Pivot:** Recommendations based on the data.
*   **Why it's legendary:** Analyze the creative of the Hall of Fame posts.

### Step 4: Validation
Run: `python scripts/validate_report.py --report draft_report.md`

## Phase 5: Delivery
Output the final, validated Markdown report.