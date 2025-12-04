#!/usr/bin/env python3
"""Validate client folder has required structure for social audit."""
import argparse
from pathlib import Path

def validate(path):
    p = Path(path)
    if not p.exists():
        print(f"Path not found: {path}")
        return False

    perf_data = p / "07_Marketing_Channels/Social_Media/02_Performance_Data"
    if not perf_data.exists():
        print(f"Missing: 07_Marketing_Channels/Social_Media/02_Performance_Data/")
        return False

    # Check for CSV or Excel files
    csvs = list(perf_data.rglob("*.csv"))
    excels = list(perf_data.rglob("*.xlsx")) + list(perf_data.rglob("*.xls"))

    if not csvs and not excels:
        print("No CSV or Excel files found in 02_Performance_Data/")
        return False

    print(f"Found {len(csvs)} CSV, {len(excels)} Excel files")
    return True

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Validate folder structure for social audit")
    p.add_argument('--path', required=True, help="Path to client folder")
    args = p.parse_args()
    exit(0 if validate(args.path) else 1)
