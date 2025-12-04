---
name: sidekick-social-audit
description: Forensic audit of client social media history with engagement metrics, trend analysis, and strategic recommendations. This skill should be used when (1) onboarding a new client to assess current social performance, (2) quarterly or annual performance reviews, (3) before creating a new social strategy, (4) client asks about what's working/not working on social. Requires CSV/Excel exports from Instagram, Facebook, GBP in per-channel folders.
---

# Sidekick Social Audit

## Data Location

Performance data should be in per-channel folders:
```
07_Marketing_Channels/Social_Media/
├── Instagram/
│   └── Performance_Data/    ← IG exports here
├── Facebook/
│   └── Performance_Data/    ← FB exports here
├── GBP/
│   └── Performance_Data/    ← GBP exports here
```

## Phase 1: Data Ingest
```bash
python scripts/validate_folder_structure.py --path "{{client_folder}}"
python scripts/parse_social_data.py --search-dir "{{client_folder}}/07_Marketing_Channels/Social_Media" --output "{{client_folder}}/reports/data_normalized.json"
python scripts/calculate_engagement.py --json-file "{{client_folder}}/reports/data_normalized.json" --output "{{client_folder}}/reports/data_enriched.json"
```

The parser automatically scans all three platform folders:
- `07_Marketing_Channels/Social_Media/Instagram/Performance_Data/`
- `07_Marketing_Channels/Social_Media/Facebook/Performance_Data/`
- `07_Marketing_Channels/Social_Media/GBP/Performance_Data/`

### File Review Requirement

**CRITICAL:** The parser now enumerates ALL files in the directory. Check the output JSON's `file_manifest` section to ensure nothing was missed:

```json
"file_manifest": {
  "total_found": 15,
  "processable_count": 10,
  "processable_files": ["...", "..."],
  "unprocessable": [["report.pdf", "not social data (.pdf)"]],
  "skipped": [...]
}
```

If `unprocessable` contains files that might have social data, manually review them.

## Phase 2: Analysis
```bash
python scripts/generate_report_metrics.py --input "{{client_folder}}/reports/data_enriched.json" --output "{{client_folder}}/reports/metrics_summary.json"
```

## Phase 3: Reporting
```bash
python scripts/fill_report_template.py --client-folder "{{client_folder}}"
```

Then write the **Executive Summary** and **Strategic Pivot** sections:
1. Read `references/AGENCY_BRAIN.md` for PICA Protocol and Carousel Thesis
2. Read client's `00_*_CLIENT_PROFILE.md` for SOW and Archetype
3. Synthesize using client data + Sidekick voice

## Phase 4: Validation
```bash
python scripts/validate_report.py --report "{{client_folder}}/reports/*_COMPLETE.md"
```

## One-Command Execution
```bash
./scripts/run_complete_audit.sh "{{client_folder}}"
```

## References
- `references/AGENCY_BRAIN.md` - Strategic frameworks (PICA, Carousel Thesis)
- `references/social_audit_matrix.md` - Report template
- `references/engagement_benchmarks.json` - Industry benchmarks
