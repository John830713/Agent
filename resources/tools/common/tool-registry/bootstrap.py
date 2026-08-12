#!/usr/bin/env python3
"""Bootstrap check for the Project Memory Framework.

Verifies a machine's resources/tools are provisioned, distinguishing
cross-project tools (tools/common/) from machine-specific tools (tools/local/).

This is the check the agent triggers on a new machine (via the INDEX chain /
AGENTS.md startup flow). It reports what is missing and how to repair it —
copying missing common tools from a provisioned D:\\Agent machine.

Usage:
  python bootstrap.py [--root D:\\Agent\\resources]

Exit codes:
  0  all common tools present
  1  common tools missing (framework cannot run) — repair required
  2  only optional/local gaps
"""

import argparse
import sys
from pathlib import Path

# Files every framework tool must ship. Keys are tool dirs under tools/common/.
CRITICAL_FILES = {
    "mneme": ["mneme.exe"],
    "chain-check": ["chain_check.py"],
    "tool-registry": ["scan.py", "validate.py", "bootstrap.py"],
    "opencode": ["restart.ps1", "send.ps1"],
    "es": ["es.exe"],
}

DOC_HEADING = "## Entity location"


def check_tool_dir(tool_dir: Path, critical: list):
    """Check a common tool dir: INDEX.md + critical files present."""
    results = []
    index = tool_dir / "INDEX.md"
    if not index.exists():
        results.append(("MISSING", "INDEX.md"))
    else:
        results.append(("ok", "INDEX.md"))
        entity = _read_entity_location(index)
        if entity:
            if Path(entity).exists():
                results.append(("ok", f"entity: {entity}"))
            else:
                results.append(("MISSING", f"entity: {entity}"))

    for f in critical:
        path = tool_dir / f
        results.append(("ok" if path.exists() else "MISSING", f))
    return results


def _read_entity_location(index: Path):
    """Read the first `## Entity location` block value from an INDEX.md.

    Skips locations shown inside fenced code blocks (e.g. registration
    templates). Returns None when the heading is absent or only appears as
    documentation.
    """
    try:
        with open(index, "r", encoding="utf-8") as f:
            lines = f.read().splitlines()
        in_fence = False
        for line in lines:
            stripped = line.strip()
            if stripped.startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            if stripped == DOC_HEADING:
                for j in range(lines.index(line) + 1, len(lines)):
                    nxt = lines[j].strip()
                    if not nxt or nxt.startswith("```"):
                        return None
                    if nxt.startswith("#"):
                        return None
                    return nxt.strip("` ")
    except Exception:
        pass
    return None


def main():
    parser = argparse.ArgumentParser(description="Bootstrap check for D:\\Agent resources")
    parser.add_argument("--check", action="store_true",
                        help="Run the check (default action, kept for symmetry with chain_check)")
    parser.add_argument("--root", default=r"D:\Agent\resources",
                        help="Root resources directory (default: D:\\Agent\\resources)")
    args = parser.parse_args()

    root = Path(args.root)
    common = root / "tools" / "common"
    local = root / "tools" / "local"

    if not common.is_dir():
        print(f"[ERROR] {common} not found — is this a D:\\Agent resources tree?")
        sys.exit(1)

    missing_common = []

    print("== Cross-project tools (tools/common) — required ==")
    for name in sorted(CRITICAL_FILES):
        tool_dir = common / name
        print(f"\n[{name}]")
        if not tool_dir.is_dir():
            print(f"  [MISSING] directory {tool_dir.name}/ not present")
            missing_common.append(name)
            continue
        for status, what in check_tool_dir(tool_dir, CRITICAL_FILES[name]):
            if status == "MISSING":
                missing_common.append(f"{name}/{what}")
                print(f"  [MISSING] {what}")
            else:
                print(f"  [ok] {what}")

    print("\n== Machine-specific tools (tools/local) — optional ==")
    missing_local = 0
    if local.is_dir():
        for d in sorted(local.iterdir()):
            if not d.is_dir():
                continue
            index = d / "INDEX.md"
            if index.exists():
                print(f"  [ok] {d.name}/ (INDEX.md)")
            else:
                print(f"  [MISSING] {d.name}/ — no INDEX.md (not registered)")
                missing_local += 1
    else:
        print("  (no tools/local directory)")
        missing_local += 1

    print()
    if missing_common:
        print(f"[FAIL] {len(missing_common)} missing common tool file(s):")
        for m in missing_common:
            print(f"  - {m}")
        print()
        print("Repair: copy the missing tool(s) from a provisioned D:\\Agent machine.")
        print("  e.g.  Copy-Item -Recurse '<source>\\resources\\tools\\common\\<name>' "
              "'<target>\\resources\\tools\\common\\'")
        print("Then re-run this check. After repair, run scan.py to rebuild the cache.")
        sys.exit(1)

    if missing_local:
        print(f"[OK] Common tools complete. {missing_local} optional local gap(s) — "
              "machine-specific, ignore if not needed.")
        sys.exit(2)

    print("[OK] All tools provisioned.")
    sys.exit(0)


if __name__ == "__main__":
    main()
