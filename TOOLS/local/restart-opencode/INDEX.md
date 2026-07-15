# restart-opencode

Restart OpenCode desktop app and mneme daemon.

## Files

- `restart_opencode.ps1` — PowerShell version (preferred). Also starts mneme daemon.
- `restart_opencode.py` — Python version. Only restarts opencode, no mneme.

## Usage

```powershell
# PowerShell version (recommended)
powershell -ExecutionPolicy Bypass -File D:\Agent\TOOLS\local\restart-opencode\restart_opencode.ps1

# Python version
python D:\Agent\TOOLS\local\restart-opencode\restart_opencode.py
```

## What it does

1. Wait for current session to finish (3-5s)
2. Kill `OpenCode.exe` process
3. Wait 2s for clean shutdown
4. Start OpenCode again
5. (PS1 only) Start mneme daemon in background

## When to use

- After modifying `.opencode/tools/*.ts` (tool definitions)
- After modifying `opencode.json` config
- When opencode is unresponsive

## Notes

- Uses `taskkill /f /im OpenCode.exe` — only targets OpenCode, safe for other processes
- Paths are hardcoded to `%LOCALAPPDATA%` — machine-specific, not portable
- PS1 version starts mneme daemon; use this if mneme needs to be running
- Python version is simpler, use if mneme is already running
