---
name: opencode
description: Operate the OpenCode desktop app — restart after config or custom-tool changes, send messages to the chat window via send.ps1.
---

# OpenCode

OpenCode 桌面應用程式的操作技能。

## Restart

### When to use

- Modified `.opencode/tools/*.ts` (custom tool definitions)
- Modified `opencode.json` (config, instructions)
- OpenCode is unresponsive or behaving strangely

### Steps

1. **Save all work** — restart kills the current session
2. **Run the restart script:**
   ```powershell
   powershell -ExecutionPolicy Bypass -File D:\Agent\resources\tools\common\opencode\restart.ps1
   ```
3. **Wait** — script handles shutdown, wait, and relaunch automatically
4. **Verify** — confirm tools and config are loaded correctly

### Auto-restart with post-reboot message

To restart and automatically send a message after reboot:

```powershell
# 1. Start background timer (20s delay)
Start-Process -FilePath "powershell" -ArgumentList "-NoProfile -ExecutionPolicy Bypass -Command `"Start-Sleep -Seconds 20; powershell -NoProfile -ExecutionPolicy Bypass -File 'D:\Agent\resources\tools\common\opencode\send.ps1' -Text 'check - restart OK'`"" -WindowStyle Hidden

# 2. Execute restart
powershell -NoProfile -ExecutionPolicy Bypass -File D:\Agent\resources\tools\common\opencode\restart.ps1
```

## Send message to self

Use `send.ps1` to send a message to the OpenCode chat window programmatically.

### When to use

- Triggering post-restart checks
- Sending automated notifications from background tasks
- Any scenario where the agent needs to talk to itself

### Steps

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File D:\Agent\resources\tools\common\opencode\send.ps1 -Text "your message"
```

### How it works

1. Find OpenCode window by title `"OpenCode"`
2. Bring to foreground
3. Set clipboard content via `Clipboard.SetText()`
4. Paste with `Ctrl+V` (bypasses IME issues)
5. Send `Enter` to submit

### Gotchas

- Window title must match `"OpenCode"` exactly
- Uses `SendKeys` for Ctrl+V and Enter — window must be in foreground
- Clipboard content is overwritten
- For background triggers, combine with `Start-Process` and `Start-Sleep`:
  ```powershell
  Start-Process -FilePath "powershell" -ArgumentList "-NoProfile -ExecutionPolicy Bypass -Command `"Start-Sleep -Seconds 15; powershell -NoProfile -ExecutionPolicy Bypass -File 'D:\Agent\resources\tools\common\opencode\send.ps1' -Text 'your message'`"" -WindowStyle Hidden
  ```

## Gotchas

- **Announce before restarting** — the restart command will hang the agent session; tell the user it's expected
- `taskkill /f /im OpenCode.exe` only targets OpenCode — safe for other processes
- PS1 version also starts mneme daemon; Python version does not
- Paths are hardcoded to `%LOCALAPPDATA%` — machine-specific, not portable
- After restart, opencode reloads `.opencode/tools/` from disk — no reinstall needed
