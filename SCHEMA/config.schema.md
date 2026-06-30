# Config Schema — 框架設定規範

## 必要檔案

```
CONFIG/
├── INDEX.md        # 設定說明
└── settings.json   # 框架設定
```

## settings.json 格式

```json
{
  "$schema": "./settings.schema.json",
  "framework_version": "0.1",
  "mneme_enabled": true,
  "auto_log_session": true,
  "task_archive_on_complete": true,
  "standing_recheck_interval_days": 1
}
```

## INDEX.md 格式

```markdown
# CONFIG

## 設定項說明

| 設定 | 類型 | 預設值 | 說明 |
|------|------|--------|------|
| framework_version | string | "0.1" | 框架版本 |
| mneme_enabled | bool | true | 啟用 mneme |
| standing_recheck_interval_days | int | 1 | Standing 任務重新檢查間隔天數 |
```
