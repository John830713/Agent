# tool-registry

Resource registration manager for `D:\Agent\resources\`. Scans tools/local, skills, and reference directories to build a local cache, and validates that registered paths still point to real files.

## Usage

```powershell
# Scan and rebuild cache
python D:\Agent\resources\tools\common\tool-registry\scan.py

# Validate registered paths (check for stale entries)
python D:\Agent\resources\tools\common\tool-registry\validate.py
```

## Commands

| Script | Description |
|--------|-------------|
| `scan.py` | Scan tools/local, skills, reference → build `.local-cache/` |
| `validate.py` | Check cache entries against disk → report stale/missing entries |

## Cache location

`D:\Agent\resources\.local-cache/`

| File | Content |
|------|---------|
| `tools.md` | Registered local tools |
| `skills.md` | Registered skill files |
| `reference.md` | Registered reference topics |

Cache is gitignored (under `/resources/`). Rebuild with `scan.py` after adding/removing tools.

## Registration flow

1. Project builds or installs a tool → creates `INDEX.md` in `D:\Agent\resources\tools\local\<tool-name>\`
2. Run `scan.py` → cache updated
3. Other projects find the tool via cache lookup

## Validation flow

1. Run `validate.py` → checks each cache entry's path exists on disk
2. Stale entries reported → user confirms removal
3. Run `scan.py` → rebuild clean cache

## Notes

- Only directories with `INDEX.md` are registered as tools
- Skills are `.md` files directly under `skills/` (excluding `INDEX.md`)
- Reference topics are subdirectories under `reference/` with `INDEX.md`
- Requires Python 3.6+

## Referenced by

- `resources/tools/INDEX.md`
- `resources/tools/local/INDEX.md`
