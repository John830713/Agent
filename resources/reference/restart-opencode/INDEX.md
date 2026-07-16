# restart-opencode — Rules & Notes

## Before restarting

- **Announce first** — the script will hang the agent session; tell the user before executing
- Save any unsaved work — restart is immediate after the kill signal

## Path dependencies

- Hardcoded to `%LOCALAPPDATA%` — machine-specific, not portable
- Requires `OpenCode.exe` at the standard install path
- `taskkill /f /im OpenCode.exe` only targets OpenCode, safe for other processes

## Script variants

| Script | Starts mneme | Use case |
|--------|-------------|----------|
| `restart_opencode.ps1` | Yes | Full restart with mneme daemon |
| `restart_opencode.py` | No | Quick restart if mneme is already running |

## After restart

- OpenCode reloads `.opencode/tools/` from disk — no reinstall needed
- Verify tools and config are loaded correctly
- If mneme daemon fails, check `~/.mneme/.lock`

## Referenced by

- `resources/reference/INDEX.md` → Subtopic listing
- `resources/INDEX.md` → Tools section
- `AGENTS.md` → Quick reference
