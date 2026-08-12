# chain-check

INDEX chain verifier — scan `.index.json` nodes, hash INDEX.md, detect changes.

## Usage

```bash
python chain_check.py --root D:\Agent\template --init
python chain_check.py --root D:\Agent\template --check
python chain_check.py --root D:\Agent\template --verify
```

## Commands

| Flag | Description |
|------|-------------|
| `--init` | Build initial hash cache to `~/.opencode/chain-cache.json` |
| `--check` | Compare current hashes with cache, report changes, update cache |
| `--verify` | Validate forward/referenced_by links in all `.index.json` |
| `--root <path>` | Root directory to scan (default: current directory) |

## Output format

```
[OK]  17 unchanged
[MOD]  2 changed: reference/git/INDEX.md, reference/mneme/INDEX.md
[NEW]  1 new:     reference/chain/INDEX.md
[DEL]  0 missing
```

Agent reads the `[MOD]` and `[NEW]` lines and reads only those files.

## Notes

- Cache is per-root: `~/.opencode/chain-cache.json` for `D:\Agent`, `~/.opencode/chain-cache-<sanitized-root>.json` for sub-projects — machine-local, not in git
- Running `--check` on a sub-project root (e.g. `D:\EXE_decompilation`) never touches the framework cache
- Hash uses `git hash-object` — same content = same hash across machines
- Requires Python 3.6+ and `git` on PATH

## Referenced by

- [tools/INDEX.md](../../INDEX.md)
