# 規格

## 介面

mneme 透過 MCP 協議提供工具。連接方式由 OpenCode MCP config 管理。

## 可用工具

| 工具 | 功能 |
|------|------|
| `remember` | 儲存長期記憶（事實、決策、偏好） |
| `recall` | 語意搜尋記憶 |
| `record_event` | 記錄事件（里程碑、訊息） |
| `pin` | 固定規則到 procedural memory |
| `recall_recent` | 按時間查詢近期事件 |
| `summarize_session` | 產生 session 摘要提示 |
| `stats` | 查看記憶體健康狀態 |
| `forget` | 刪除記憶 |

## 資料目錄

`~/.mneme/`（固定路徑，無法更改）
