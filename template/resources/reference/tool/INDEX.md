# Tool management

## Lookup order

1. `<project>/.agent/Tools/` — project-specific tools
2. `D:\Agent\resources\tools/common/` — cross-project tools
3. `D:\Agent\resources\tools/local/` — machine-specific tools

## Adding tools

- Project-specific → `<project>/.agent/Tools/<name>/INDEX.md`
- Cross-project → `D:\Agent\resources\tools/common/<name>/`
- Machine-specific → `D:\Agent\resources\tools/local/<name>/`
- Worth sharing? Copy to `template/resources/tools/` and send a PR

## Git tracking notes

- `D:\Agent\resources/tools/` is mostly git-ignored (per `.gitignore` `/resources/`), except for tool binaries/scripts bundled in this repo (like `mneme.exe`, `restart-opencode.ps1`) which are force-tracked.
- `template/resources/tools/` is git-tracked and serves as the new-machine seed.

## Referenced by

- `reference/INDEX.md` → Tool section
