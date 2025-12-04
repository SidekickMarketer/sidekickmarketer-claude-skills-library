import argparse
import os
import sys

def main():
    parser = argparse.ArgumentParser(description="Generate monthly recaps from Looker data")
    parser.add_argument("--client", required=True, help="Client name")
    parser.add_argument("--month", required=True, help="Month Year (e.g. November 2025)")
    parser.add_argument("--data", help="Path to data file")
    parser.add_argument("--context", help="Path to context file")
    
    args = parser.parse_args()
    
    print(f"Generating recap for {args.client} - {args.month}")
    print("NOTE: This script is a placeholder. The skill logic is currently handled by Claude reading the templates.")
    print("To use: ask Claude 'Create the monthly recap for [Client] using this data...'")

if __name__ == "__main__":
    main()

