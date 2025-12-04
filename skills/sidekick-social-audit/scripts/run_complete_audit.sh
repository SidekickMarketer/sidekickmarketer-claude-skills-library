#!/bin/bash
# Sidekick Social Audit - Complete Pipeline Runner
# Version: 3.2
# Usage: ./run_complete_audit.sh "/path/to/client-folder"

set -e  # Exit on any error

CLIENT="$1"
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
SKILL_ROOT="$(dirname "$SCRIPT_DIR")"

# Output directories (aligned with canonical folder structure)
PERF_DATA="$CLIENT/07_Marketing_Channels/Social_Media/02_Performance_Data"
AUDIT_OUTPUT="$CLIENT/07_Marketing_Channels/Social_Media/04_Audit_Reports"

# 0. Input validation
if [ -z "$CLIENT" ]; then
    echo "ERROR: No client path provided"
    echo "Usage: ./run_complete_audit.sh \"/path/to/client-folder\""
    exit 1
fi

if [ ! -d "$CLIENT" ]; then
    echo "ERROR: Client folder not found: $CLIENT"
    exit 1
fi

if [ ! -d "$PERF_DATA" ]; then
    echo "ERROR: Performance data folder not found"
    echo "   Expected: $PERF_DATA"
    echo ""
    echo "Please drop your social media exports (CSV/Excel) into:"
    echo "   07_Marketing_Channels/Social_Media/02_Performance_Data/"
    exit 1
fi

# Create output directory if needed
mkdir -p "$AUDIT_OUTPUT"

echo "Starting Audit for: $(basename "$CLIENT")"
echo "============================================"
echo "Input:  $PERF_DATA"
echo "Output: $AUDIT_OUTPUT"
echo ""

# 1. Parse - Extract data from CSV + Excel
echo "Step 1/4: Parsing social data..."
python3 "$SKILL_ROOT/scripts/parse_social_data.py" \
    --search-dir "$PERF_DATA" \
    --output "$AUDIT_OUTPUT/data_normalized.json"

# 2. Enrich - Calculate engagement rates
echo "Step 2/4: Calculating engagement..."
python3 "$SKILL_ROOT/scripts/calculate_engagement.py" \
    --json-file "$AUDIT_OUTPUT/data_normalized.json" \
    --output "$AUDIT_OUTPUT/data_enriched.json"

# 3. Analyze - Generate metrics & insights
echo "Step 3/4: Analyzing trends..."
python3 "$SKILL_ROOT/scripts/generate_report_metrics.py" \
    --input "$AUDIT_OUTPUT/data_enriched.json" \
    --output "$AUDIT_OUTPUT/metrics_summary.json"

# 4. Report - Fill template
echo "Step 4/4: Generating report..."
python3 "$SKILL_ROOT/scripts/fill_report_template.py" \
    --client-folder "$CLIENT"

# 5. Validate output
echo "============================================"
echo "Validating report..."
python3 "$SKILL_ROOT/scripts/validate_report.py" \
    --report "$AUDIT_OUTPUT/*_Audit_COMPLETE.md"

echo "============================================"
echo "AUDIT COMPLETE"
echo "Report: $AUDIT_OUTPUT/"
