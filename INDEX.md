# Project Memory Framework — Agent Operations Manual

本倉庫是 AI agent 的**操作守則與靜態框架定義**，不包含任何動態專案資料。

## 內容

```
D:\Agent\
├── INDEX.md          # 本檔案 — 框架說明
├── AGENTS.md         # Agent 啟動指引（每次 session 必讀）
├── mneme.exe         # 記憶後端二進位
│
├── SCHEMA/           # 結構定義 — 目錄/檔案格式規範
│   ├── task.schema.md
│   ├── tool.schema.md
│   ├── result.schema.md
│   ├── config.schema.md
│   └── log.schema.md
│
├── TOOLS/            # 工具庫定義
│   ├── INDEX.md
│   ├── mneme/
│   └── git/
│
└── CONFIG/           # 框架設定
    └── INDEX.md
```

## 動態資料位置

所有動態資料（任務、結果、日誌）放在**各專案目錄下的 `.agent/`**：

```
D:\Test1\             # 專案目錄
├── (專案程式碼)
└── .agent\           # Agent runtime 資料（不進 git）
    ├── TASKS\
    │   ├── Standing\
    │   ├── Adhoc\
    │   └── Scheduled\
    ├── RESULTS\
    └── LOGS\
```

## 核心原則

- **`D:\Agent\` 只放靜態定義** — git 倉庫不追蹤動態狀態
- **每個目錄有 INDEX.md** — AI 讀了就懂該目錄用途
- **TOOLS/ 讓 AI 自主查閱** — 不需問使用者有什麼工具
- **SCHEMA/ 規範一切結構** — 遵循 schema 就不會亂
