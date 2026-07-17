# Project Memory Framework — Agent Operations Manual

本倉庫是 AI agent 的**操作守則與靜態框架定義**，不包含任何動態專案資料。

## 內容

```
D:\Agent\
├── INDEX.md          # 本檔案 — 框架說明
├── AGENTS.md         # Agent 啟動指引（每次 session 必讀）
├── opencode.json     # OpenCode 設定
│
├── resources/        # 工具說明書、通用參考、技能定義（各機台自行維護，不進 git）
│   ├── INDEX.md
│   ├── tools/
│   │   ├── common/   # 跨專案通用工具
│   │   └── local/    # 本機限定工具
│   ├── skills/       # 技能定義
│   └── reference/    # 通用參考資料（含 design 庫）
│
├── template/         # 新機台 resource seed（進 git）
│   └── resources/    # 新機台起始參考（tools, skills, reference）
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
- **resources/ 讓 AI 自主查閱** — 不需問使用者有什麼工具
