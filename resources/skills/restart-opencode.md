# Restart OpenCode

Restart the OpenCode desktop app to reload tool definitions or config changes.

## When to use

- Modified `.opencode/tools/*.ts` (custom tool definitions)
- Modified `opencode.json` (config, instructions)
- OpenCode is unresponsive or behaving strangely

## Steps

1. **Save all work** — restart kills the current session
2. **Run the restart script:**
   ```powershell
   powershell -ExecutionPolicy Bypass -File D:\Agent\TOOLS\local\restart-opencode\restart_opencode.ps1
   ```
3. **Wait** — script handles shutdown, wait, and relaunch automatically
4. **Verify** — confirm tools and config are loaded correctly

## Gotchas

- `taskkill /f /im OpenCode.exe` only targets OpenCode — safe for other processes
- PS1 version also starts mneme daemon; Python version does not
- Paths are hardcoded to `%LOCALAPPDATA%` — won't work on other machines
- After restart, opencode reloads `.opencode/tools/` from disk — no reinstall needed
