#!/usr/bin/env python3
"""
INDEX chain verifier - scan .index.json nodes, hash INDEX.md, detect changes.

Usage:
  python chain_check.py --init          Build initial hash cache
  python chain_check.py --check         Compare current state with cache
  python chain_check.py --verify        Validate forward/referenced_by links
  python chain_check.py --root <path>   Root directory (default: .)
"""

import argparse, hashlib, json, os, re, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path


LEGACY_CACHE_FILE = os.path.expanduser("~/.opencode/chain-cache.json")
CACHE_VERSION = 1


def cache_file_for(root_abs):
    """Return the cache file for a root.

    Uses the legacy single cache file when its stored root matches the
    requested root (preserves D:\\Agent behavior). Any other root gets its own
    per-root cache so checking sub-projects never collides with or clobbers
    the framework cache.
    """
    if os.path.exists(LEGACY_CACHE_FILE):
        try:
            with open(LEGACY_CACHE_FILE, "r", encoding="utf-8") as f:
                stored_root = json.load(f).get("root")
            if stored_root and os.path.normcase(os.path.abspath(stored_root)) == os.path.normcase(root_abs):
                return LEGACY_CACHE_FILE
        except Exception:
            pass
    safe = re.sub(r"[^A-Za-z0-9_-]", "_", os.path.normcase(os.path.abspath(root_abs)))
    return os.path.expanduser(f"~/.opencode/chain-cache-{safe}.json")


def find_nodes(root):
    """Find all directories containing .index.json under root."""
    nodes = []
    for dirpath, dirnames, filenames in os.walk(root):
        if ".git" in dirnames:
            dirnames.remove(".git")
        if ".index.json" in filenames:
            nodes.append(os.path.normpath(dirpath))
    return sorted(nodes)


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def git_hash_object(filepath):
    """Calculate git blob hash for a file using git hash-object."""
    abs_path = os.path.abspath(filepath)
    try:
        result = subprocess.run(
            ["git", "hash-object", abs_path],
            capture_output=True, text=True, check=True,
            cwd=os.path.dirname(abs_path)
        )
        return result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def resolve_relative(base_dir, rel_path):
    """Resolve a relative path from base_dir, returning normalized absolute path."""
    return os.path.normpath(os.path.join(base_dir, rel_path))


def scan_node_hashes(root, nodes):
    """For each node, find INDEX.md and compute git hash. Returns dict of relative path -> {hash: str}."""
    hashes = {}
    root_abs = os.path.abspath(root)
    for node_dir in nodes:
        index_md = os.path.join(node_dir, "INDEX.md")
        if os.path.exists(index_md):
            h = git_hash_object(index_md)
            if h:
                rel = os.path.relpath(index_md, root_abs)
                hashes[rel] = {"hash": h}
    return hashes


def do_init(root):
    """Build initial cache and write to file."""
    root_abs = os.path.abspath(root)
    cache_file = cache_file_for(root_abs)
    nodes = find_nodes(root_abs)
    if not nodes:
        print(f"No .index.json found under {root_abs}")
        sys.exit(1)

    hashes = scan_node_hashes(root_abs, nodes)
    cache = {
        "version": CACHE_VERSION,
        "updated": datetime.now(timezone.utc).isoformat(),
        "root": root_abs,
        "nodes": hashes
    }

    os.makedirs(os.path.dirname(cache_file), exist_ok=True)
    with open(cache_file, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=2, ensure_ascii=False)

    print(f"[OK] Init complete - {len(hashes)} nodes cached")
    print(f"     Cache: {cache_file}")
    print(f"     Root:  {root_abs}")


def do_check(root):
    """Compare current hashes with cache, report changes."""
    root_abs = os.path.abspath(root)
    cache_file = cache_file_for(root_abs)
    if not os.path.exists(cache_file):
        print(f"[ERR] No cache found for {root_abs}. Run --init first.")
        sys.exit(1)

    with open(cache_file, "r") as f:
        cache = json.load(f)

    if cache.get("version") != CACHE_VERSION:
        print(f"[ERR] Cache version mismatch (found {cache.get('version')}, expected {CACHE_VERSION}). Re-run --init.")
        sys.exit(1)

    root_abs = os.path.abspath(root)
    nodes = find_nodes(root_abs)
    current = scan_node_hashes(root_abs, nodes)

    cached = cache.get("nodes", {})
    unchanged = []
    changed = []
    new = []
    missing = []

    for path, info in current.items():
        sha = info["hash"]
        if path in cached:
            if cached[path]["hash"] == sha:
                unchanged.append(path)
            else:
                changed.append(path)
        else:
            new.append(path)

    for path in cached:
        if path not in current:
            missing.append(path)

    # Update cache
    cache["updated"] = datetime.now(timezone.utc).isoformat()
    cache["nodes"] = current
    with open(cache_file, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=2, ensure_ascii=False)

    print(f"[OK]  {len(unchanged)} unchanged")
    for p in sorted(changed):
        print(f"[MOD] changed: {p}")
    for p in sorted(new):
        print(f"[NEW] new:     {p}")
    for p in sorted(missing):
        print(f"[DEL] missing: {p}")

    return len(changed) + len(new) + len(missing)


def do_verify(root):
    """Validate all forward/referenced_by links in .index.json files."""
    root_abs = os.path.abspath(root)
    nodes = find_nodes(root_abs)
    errors = 0

    # Build a set of known node paths (relative to root)
    node_dirs = set()
    for nd in nodes:
        rel = os.path.relpath(nd, root_abs)
        node_dirs.add(rel)

    for node_dir in nodes:
        json_path = os.path.join(node_dir, ".index.json")
        data = load_json(json_path)
        rel = os.path.relpath(node_dir, root_abs)

        # Check version consistency
        if data.get("version") != CACHE_VERSION:
            print(f"[ERR] {rel}/.index.json: version {data.get('version')} != expected {CACHE_VERSION}")
            errors += 1

        # Verify forward links
        for fwd in data.get("forward", []):
            target = resolve_relative(node_dir, fwd)
            target_index = os.path.join(target, "INDEX.md")
            target_json = os.path.join(target, ".index.json")
            if not os.path.exists(target_index):
                print(f"[ERR] {rel}/.index.json: forward -> {fwd} (INDEX.md not found)")
                errors += 1
            if not os.path.exists(target_json):
                print(f"[ERR] {rel}/.index.json: forward -> {fwd} (.index.json not found)")
                errors += 1
            else:
                # Verify back-link exists (referenced_by should resolve to source node dir)
                td = load_json(target_json)
                found_back = False
                for ref in td.get("referenced_by", []):
                    resolved_ref = resolve_relative(target, ref)
                    if os.path.normpath(resolved_ref) == os.path.normpath(node_dir):
                        found_back = True
                        break
                if not found_back:
                    print(f"[ERR] {rel}/.index.json: forward -> {fwd} missing back-link in {fwd}.index.json")
                    errors += 1

        # Verify referenced_by links
        for ref in data.get("referenced_by", []):
            target = resolve_relative(node_dir, ref)
            target_json = os.path.join(target, ".index.json")
            if not os.path.exists(target_json):
                print(f"[ERR] {rel}/.index.json: referenced_by -> {ref} (no .index.json at target)")
                errors += 1

    if errors == 0:
        print(f"[OK] Verify complete - {len(nodes)} nodes, all links valid")
    else:
        print(f"[ERR] {errors} error(s) found")

    return errors


def main():
    parser = argparse.ArgumentParser(description="INDEX chain verifier")
    parser.add_argument("--root", default=".", help="Root directory (default: current dir)")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--init", action="store_true", help="Build initial hash cache")
    group.add_argument("--check", action="store_true", help="Compare against cache")
    group.add_argument("--verify", action="store_true", help="Validate link integrity")
    args = parser.parse_args()

    if args.init:
        do_init(args.root)
    elif args.check:
        sys.exit(do_check(args.root))
    elif args.verify:
        sys.exit(do_verify(args.root))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
