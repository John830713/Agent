# opencode — OpenCode 工具集

OpenCode 桌面應用程式相關工具。

## Tools

| Tool | File | Description |
|------|------|-------------|
| Restart | `restart.ps1` / `restart.py` | 重啟 OpenCode 及 mneme daemon |
| Send | `send.ps1` | 透過剪貼簿送訊息到 OpenCode 視窗 |

## restart

重啟 OpenCode 桌面應用程式。

```powershell
# PowerShell 版（推薦，會啟動 mneme daemon）
powershell -ExecutionPolicy Bypass -File D:\Agent\resources\tools\common\opencode\restart.ps1

# Python 版（不啟動 mneme）
python D:\Agent\resources\tools\common\opencode\restart.py
```

流程：等待 3-5s → `taskkill /f /im OpenCode.exe` → 等待 2s → 重新啟動。PS1 版會先啟動 mneme daemon。

適用時機：修改 `.opencode/` 工具定義、修改 `opencode.json`、OpenCode 無回應時。

## send

透過剪貼簿將文字貼上 OpenCode 視窗並送出，繞過 IME 輸入法問題。

```powershell
powershell -ExecutionPolicy Bypass -File D:\Agent\resources\tools\common\opencode\send.ps1 -Text "your message"
```

流程：找到 OpenCode 視窗 → 拉到前景 → 設定剪貼簿 → Ctrl+V 貼上 → Enter 送出。

## Notes

- 路徑硬編碼 `%LOCALAPPDATA%`，僅限本機使用
- Send 依賴視窗標題精確匹配 `"OpenCode"`
- Send 使用 `SendKeys` 模擬 Ctrl+V 和 Enter，需視窗在前景
