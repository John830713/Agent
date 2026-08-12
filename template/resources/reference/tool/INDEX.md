# Tool management

## Lookup order

1. `<project>/.agent/Tools/` — project-specific tools
2. `D:\Agent\resources\tools/common/` — cross-project tools
3. `D:\Agent\resources\tools/local/` — machine-specific tools

## Adding tools

- Project-specific → `<project>/.agent/Tools/<name>/INDEX.md`
- Cross-project → `D:\Agent\resources\tools\common/<name>/`
- Machine-specific → `D:\Agent\resources\tools/local/<name>/`
- Worth sharing? Copy to `template/resources/tools/` and send a PR

## Available tools

| Directory | Purpose |
|-----------|---------|
| `common/` | Cross-project tools — see `common/INDEX.md` |
| `local/` | Machine-specific tools (varies per machine) — e.g. `msys2-portable/`, `autoit-v3/` |

## Bootstrap check

`bootstrap.py` (in `common/tool-registry/`) verifies a machine's tools are provisioned:

- Distinguishes cross-project tools (`common/`, required) from machine-specific tools (`local/`, optional)
- Verifies each common tool's critical files exist and its `## Entity location` resolves
- On a new machine: run `python ...\tool-registry\bootstrap.py --check`, copy missing `common/` tools from a provisioned machine, then run `scan.py`

## Git tracking notes

- `template/resources/` is git-tracked and is the **architecture seed**: only the INDEX chain (INDEX.md + `.index.json`) for framework tools, plus framework-generic reference topics. It carries no tool scripts, no binaries (`.exe`), and no machine-specific topics.
- `resources/` is machine-local. Only tool binaries/scripts that were force-tracked before (e.g. `mneme.exe`, `es.exe`) remain in git; everything else lives only on this machine.
- Machine-specific reference topics and skills (`resources/reference/`, `resources/skills/`) are never tracked — new machines copy the repo's `template/` and add their own.

## Referenced by

- `resources/reference/INDEX.md` → Subtopic listing
- `AGENTS.md` → Quick reference
