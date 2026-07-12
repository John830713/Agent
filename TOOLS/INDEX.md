# TOOLS — 工具庫

AI agent 可自主查閱的工具清單。每個工具是一個獨立目錄，包含說明書、規格與使用範例。

## 使用方式

1. 讀取本檔案確認有哪些可用工具
2. 進入工具目錄讀取 INDEX.md 了解用途
3. 查閱 spec.md 與 usage.md 取得詳細用法
4. 不需詢問使用者即可自行調用

## 註冊新工具

發現新工具時，依 SCHEMA/tool.schema.md 規範建立工具目錄：

```
TOOLS/
├── INDEX.md
└── tool-name/
    ├── INDEX.md    # 說明用途與場景
    ├── spec.md     # 規格 / API
    └── usage.md    # 使用範例
```

## 工具清單

| 工具 | 用途 |
|------|------|
| [mneme](mneme/) | 持久記憶後端，跨 session 儲存/查詢 |
| [git](git/) | 版本控制操作 |
| [design](design/) | UI 設計慣例與可重複使用的 pattern |
