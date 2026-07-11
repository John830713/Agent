# 規格

## 常用指令

| 指令 | 用途 |
|------|------|
| `git status` | 檢視目前狀態 |
| `git diff` | 檢視變更內容 |
| `git log --oneline -10` | 檢視最近 10 筆 commit |
| `git add <file>` | 暫存檔案 |
| `git commit -m "<msg>"` | 提交變更 |
| `git push` | 推送至遠端 |

## 準則

- 只 commit 使用者明確要求的內容
- 不 commit secrets 或憑證
- commit message 簡潔描述變更內容
- 依照功能拆分 commit，每個 commit 只包含單一功能的變更，不相關的改動分開提交
