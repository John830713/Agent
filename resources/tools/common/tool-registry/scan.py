#!/usr/bin/env python3
"""Scan resources directories and build local cache.

Scans:
  - tools/local/  → .local-cache/tools.md
  - skills/       → .local-cache/skills.md
  - reference/    → .local-cache/reference.md

Usage:
  python scan.py [--root D:\Agent\resources]
"""

import os
import sys
import argparse
from pathlib import Path


def scan_tools(root: Path):
    """Scan tools/local/ for registered tool directories (must have INDEX.md)."""
    tools_dir = root / "tools" / "local"
    entries = []
    if not tools_dir.is_dir():
        return entries

    for d in sorted(tools_dir.iterdir()):
        if not d.is_dir():
            continue
        index = d / "INDEX.md"
        if index.exists():
            desc = _read_first_heading(index)
            entries.append({
                "name": d.name,
                "description": desc,
                "path": str(d),
                "has_index": True,
            })
        else:
            entries.append({
                "name": d.name,
                "description": d.name,
                "path": str(d),
                "has_index": False,
            })
    return entries


def scan_skills(root: Path):
    """Scan skills/ for .md skill files (excluding INDEX.md)."""
    skills_dir = root / "skills"
    entries = []
    if not skills_dir.is_dir():
        return entries

    for f in sorted(skills_dir.iterdir()):
        if f.suffix == ".md" and f.name != "INDEX.md":
            desc = _read_first_heading(f)
            entries.append({
                "name": f.stem,
                "description": desc,
                "path": str(f),
            })
    return entries


def scan_reference(root: Path):
    """Scan reference/ for subdirectories with INDEX.md."""
    ref_dir = root / "reference"
    entries = []
    if not ref_dir.is_dir():
        return entries

    for d in sorted(ref_dir.iterdir()):
        if not d.is_dir():
            continue
        index = d / "INDEX.md"
        if index.exists():
            desc = _read_first_heading(index)
            entries.append({
                "name": d.name,
                "description": desc,
                "path": str(d),
            })
    return entries


def _read_first_heading(filepath: Path):
    """Extract the first heading line from a markdown file."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("# "):
                    return line[2:].strip()
    except Exception:
        pass
    return filepath.parent.name


def write_cache(cache_dir: Path, filename: str, entries: list, category: str):
    """Write entries to a cache markdown file."""
    cache_dir.mkdir(parents=True, exist_ok=True)
    path = cache_dir / filename

    lines = [f"# {category} cache", ""]
    if not entries:
        lines.append("*(none found)*")
    else:
        for e in entries:
            status = "" if e.get("has_index", True) else " *(no INDEX.md)*"
            lines.append(f"- **{e['name']}**: {e['description']}{status}")
            lines.append(f"  - Path: `{e['path']}`")
    lines.append("")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    return len(entries)


def main():
    parser = argparse.ArgumentParser(description="Scan resources and build local cache")
    parser.add_argument("--root", default=r"D:\Agent\resources",
                        help="Root resources directory (default: D:\\Agent\\resources)")
    args = parser.parse_args()

    root = Path(args.root)
    if not root.is_dir():
        print(f"[ERROR] Root directory not found: {root}")
        sys.exit(1)

    cache_dir = root / ".local-cache"

    print(f"Scanning {root} ...")

    tools = scan_tools(root)
    n = write_cache(cache_dir, "tools.md", tools, "Tools")
    print(f"  tools/local: {n} entries")

    skills = scan_skills(root)
    n = write_cache(cache_dir, "skills.md", skills, "Skills")
    print(f"  skills: {n} entries")

    refs = scan_reference(root)
    n = write_cache(cache_dir, "reference.md", refs, "Reference")
    print(f"  reference: {n} entries")

    print(f"\nCache written to {cache_dir}")


if __name__ == "__main__":
    main()
