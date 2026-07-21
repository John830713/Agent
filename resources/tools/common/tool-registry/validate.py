#!/usr/bin/env python3
"""Validate resource cache entries against disk.

Reads .local-cache/*.md, checks each Path entry exists on disk,
reports stale/missing entries.

Usage:
  python validate.py [--root D:\Agent\resources]
"""

import os
import re
import sys
import argparse
from pathlib import Path


CACHE_FILES = {
    "tools.md": "Tools",
    "skills.md": "Skills",
    "reference.md": "Reference",
}


def parse_cache(cache_path: Path):
    """Parse a cache .md file and extract entries with paths."""
    entries = []
    if not cache_path.exists():
        return entries

    with open(cache_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    current_name = None
    for line in lines:
        # Match "- **name**:" pattern
        m = re.match(r"^- \*\*(.+?)\*\*:", line)
        if m:
            current_name = m.group(1)
            continue

        # Match "  - Path: `path`" pattern
        m = re.match(r"^\s+- Path: `(.+?)`", line)
        if m and current_name:
            entries.append({
                "name": current_name,
                "path": m.group(1),
            })
            current_name = None

    return entries


def validate_entries(entries: list):
    """Check if each entry's path exists on disk."""
    valid = []
    stale = []

    for e in entries:
        p = Path(e["path"])
        if p.exists():
            valid.append(e)
        else:
            stale.append(e)

    return valid, stale


def main():
    parser = argparse.ArgumentParser(description="Validate resource cache entries")
    parser.add_argument("--root", default=r"D:\Agent\resources",
                        help="Root resources directory (default: D:\\Agent\\resources)")
    args = parser.parse_args()

    root = Path(args.root)
    cache_dir = root / ".local-cache"

    if not cache_dir.is_dir():
        print(f"[ERROR] Cache directory not found: {cache_dir}")
        print("Run scan.py first to build the cache.")
        sys.exit(1)

    total_valid = 0
    total_stale = 0

    for filename, category in CACHE_FILES.items():
        cache_path = cache_dir / filename
        entries = parse_cache(cache_path)

        if not entries:
            print(f"[{category}] No entries in cache")
            continue

        valid, stale = validate_entries(entries)
        total_valid += len(valid)
        total_stale += len(stale)

        if stale:
            print(f"\n[{category}] {len(valid)} OK, {len(stale)} STALE:")
            for e in stale:
                print(f"  [STALE] {e['name']} -> {e['path']}")
        else:
            print(f"[{category}] {len(valid)} OK, 0 stale")

    print(f"\nTotal: {total_valid} valid, {total_stale} stale")

    if total_stale > 0:
        print("\nStale entries found. Consider removing the corresponding")
        print("directories/files and running scan.py to rebuild the cache.")
        sys.exit(1)
    else:
        print("All entries valid.")
        sys.exit(0)


if __name__ == "__main__":
    main()
