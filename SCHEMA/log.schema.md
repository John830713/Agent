# Log Schema — session 日誌規範

## 位置

```
.agent/LOGS/
├── INDEX.md
└── YYYY-MM-DD.md       # 每次 session 一檔
└── YYYY-MM-DD-NNN.md   # 同一天多個 session 加流水號
```

## 格式

```markdown
# YYYY-MM-DD (Session N)

## 目標

本次 session 要完成的事。

## 完成項目

- [x] 項目一
- [ ] 項目二（未完成）

## 決策記錄

- 決策內容 + 原因

## 待辦（移至下個 session）

- 未完成的項目

## 備註
```

## AI 使用方式

- session 結束時自動寫入新日誌
- 啟動時讀取最新日誌取得上次中斷點
