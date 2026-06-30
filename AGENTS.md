# AGENTS.md

## 角色

本倉庫是 **AI agent 的操作守則**，不是專案本身。所有動態任務資料放在各專案的 `.agent/` 目錄下。

## Session 啟動流程（每次必做）

1. 讀 `INDEX.md` — 理解框架結構與角色
2. 讀 `SCHEMA/INDEX.md` — 理解目錄/檔案規範
3. 讀 `CONFIG/INDEX.md` — 讀取框架設定
4. 讀 `TOOLS/INDEX.md` — 確認可用工具
5. 呼叫 `mneme.recall(query="recent session context")` — 取得跨 session 上下文
6. 切換 scope 到目前專案：`mneme.switch_scope("<project-name>")`
7. 檢查專案 `.agent/TASKS/` — 處理未完成任務

## 專案工作流程

### 開始新專案

從範本複製 `.agent/` 結構（單次 Copy-Item，不需逐檔建立）：

```powershell
Copy-Item -Recurse "D:\Agent\template\.agent" "專案\.agent"
```

然後取代所有檔案中的 `{{project_name}}` 和 `{{date}}` 佔位符。

範本位置：`D:\Agent\template\.agent\`

結構一覽：
```
.agent/
├── INDEX.md                     # 總說明（含 {{project_name}}）
├── TASKS/
│   ├── INDEX.md
│   ├── Standing/
│   │   ├── INDEX.md
│   │   └── Init/
│   │       ├── INDEX.md
│   │       ├── plan.md
│   │       └── checklist.md     # 含 {{project_name}}
│   ├── Adhoc/
│   │   └── INDEX.md
│   └── Scheduled/
│       └── INDEX.md
├── RESULTS/
│   └── INDEX.md
└── LOGS/
    └── INDEX.md
```

### 進行中

- 任務狀態以 `checklist.md` 的 `[x]` 比例判定
- Standing 任務標示 `completed` 後跳過不重複
  - 每次標示時同時更新 `verified: YYYY-MM-DD` 欄位
  - Agent 啟動時：`verified < today` 的 Standing 需重新確認
  - `verified == today` 的 Standing 直接跳過
- Adhoc 任務完成後移至 `RESULTS/` 或清除
- Scheduled 任務依日期處理今日/逾期項目
- 每次 session 結束時依 `SCHEMA/log.schema.md` 寫入 `.agent/LOGS/`

### 發現新工具

依 `SCHEMA/tool.schema.md` 在 `D:\Agent\TOOLS\` 建立工具條目（INDEX.md + spec.md + usage.md）。

## Mneme 設定

- `D:\Agent\mneme.exe` — 專案內二進位
- 資料目錄：`~/.mneme/`
- 專案隔離：使用 `switch_scope("<project-name>")` 切換 scope
- agent 不應在 C 槽非必要路徑寫入檔案
