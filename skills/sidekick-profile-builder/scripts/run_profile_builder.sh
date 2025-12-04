#!/bin/bash
# Sidekick Profile Builder - Complete Pipeline
# Usage: ./run_profile_builder.sh "/path/to/client-folder"

set -e

CLIENT="$1"
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
SKILL_ROOT="$(dirname "$SCRIPT_DIR")"

# Validation
if [ -z "$CLIENT" ]; then
    echo "❌ ERROR: No client folder provided"
    echo "Usage: ./run_profile_builder.sh \"/path/to/client-folder\""
    exit 1
fi

if [ ! -d "$CLIENT" ]; then
    echo "❌ ERROR: Client folder not found: $CLIENT"
    exit 1
fi

NOTION_DIR="$CLIENT/notion_export"
if [ ! -d "$NOTION_DIR" ]; then
    echo "⚠️  WARNING: Notion export folder not found"
    echo "   Expected: $NOTION_DIR"
    echo ""
    echo "   Continuing anyway - you can still scan other folders."
fi

echo "🚀 Building Profile for: $(basename "$CLIENT")"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Ask about additional folders
echo ""
echo "📁 The profile builder will scan: notion_export/"
echo ""
echo "Do you have any additional folders to scan?"
echo "(These could be contracts, discovery docs, brand assets, etc.)"
echo ""
echo "Enter folder paths (one per line), or press ENTER to skip:"
echo "(Type 'done' when finished)"
echo ""

ADDITIONAL_FOLDERS=()
while true; do
    read -r -p "   Folder path: " folder_input
    if [ -z "$folder_input" ] || [ "$folder_input" = "done" ]; then
        break
    fi
    if [ -d "$folder_input" ]; then
        ADDITIONAL_FOLDERS+=("$folder_input")
        echo "   ✅ Added: $folder_input"
    else
        echo "   ⚠️  Folder not found: $folder_input (skipping)"
    fi
done

# Ask about URLs to fetch
echo ""
echo "🌐 Do you have any URLs to fetch?"
echo "(Client website, social profiles, Google Business Profile)"
echo ""
echo "Enter URLs (one per line), or press ENTER to skip:"
echo "(Type 'done' when finished)"
echo ""

URLS=()
while true; do
    read -r -p "   URL: " url_input
    if [ -z "$url_input" ] || [ "$url_input" = "done" ]; then
        break
    fi
    URLS+=("$url_input")
    echo "   ✅ Added: $url_input"
done

# Summary
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📋 SCAN SUMMARY:"
if [ -d "$NOTION_DIR" ]; then
    echo "   • notion_export/ folder"
fi
if [ ${#ADDITIONAL_FOLDERS[@]} -gt 0 ]; then
    echo "   • ${#ADDITIONAL_FOLDERS[@]} additional folder(s)"
fi
if [ ${#URLS[@]} -gt 0 ]; then
    echo "   • ${#URLS[@]} URL(s) to fetch"
fi
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Step 1: Inventory
echo ""
echo "📋 Step 1: Inventorying files..."
if [ -d "$NOTION_DIR" ]; then
    python3 "$SKILL_ROOT/scripts/inventory_exports.py" \
        --source "$NOTION_DIR" \
        --output "$CLIENT/_file_inventory.json"
else
    echo "   (Skipping notion_export inventory - folder not found)"
fi

# Step 2: Build Profile
echo ""
echo "🔨 Step 2: Extracting & building profile..."

# Build the command with optional arguments
BUILD_CMD="python3 \"$SKILL_ROOT/scripts/build_profile.py\" --client-folder \"$CLIENT\""

if [ ${#ADDITIONAL_FOLDERS[@]} -gt 0 ]; then
    BUILD_CMD="$BUILD_CMD --additional-folders"
    for folder in "${ADDITIONAL_FOLDERS[@]}"; do
        BUILD_CMD="$BUILD_CMD \"$folder\""
    done
fi

if [ ${#URLS[@]} -gt 0 ]; then
    BUILD_CMD="$BUILD_CMD --urls"
    for url in "${URLS[@]}"; do
        BUILD_CMD="$BUILD_CMD \"$url\""
    done
fi

# Execute the build command
eval $BUILD_CMD

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ PROFILE BUILD COMPLETE"
echo ""
echo "📂 Outputs:"
echo "   • Profile: $CLIENT/00_*_CLIENT_PROFILE.md"
echo "   • Audit:   $CLIENT/_extraction_audit.md"
echo "   • Review:  $CLIENT/_conflicts.md (if any)"
echo "   • Gaps:    $CLIENT/_gaps.md (if any)"

# Step 3: Validate
echo ""
echo "🔍 Step 3: Validating profile completeness..."
python3 "$SKILL_ROOT/scripts/validate_profile.py" --client-folder "$CLIENT"

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "👆 Review the validation report above."
echo "   Fill in incomplete sections before running other skills."
