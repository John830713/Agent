# SCHEMA — 結構定義層

定義框架中所有目錄與檔案的結構規範。每個 schema 檔案說明一種類型的目錄應該長怎樣、有哪些必要檔案、遵循什麼格式。

## Schema 清單

| 檔案 | 定義對象 |
|------|----------|
| `task.schema.md` | TASKS/ 下的任務目錄結構 |
| `tool.schema.md` | TOOLS/ 下的工具條目結構 |
| `result.schema.md` | RESULTS/ 下的成果目錄結構 |
| `config.schema.md` | CONFIG/ 下的框架設定結構 |
| `log.schema.md` | LOGS/ 下的 session 日誌結構 |

## 如何擴充

如果要新增一種目錄類型（例如 `DESIGNS/`）：
1. 建立新目錄及其 INDEX.md
2. 在 SCHEMA/ 新增對應的 schema 檔案
3. 在根目錄 INDEX.md 更新目錄結構表
