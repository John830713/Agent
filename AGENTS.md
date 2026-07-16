# AGENTS.md

## 角色

本倉庫是 **AI agent 的操作守則**，不是專案本身。所有動態任務資料放在各專案的 `.agent/` 目錄下。

---

## 每次 Session 自動載入

### 啟動流程

1. 讀 `INDEX.md` — 理解框架結構
2. 讀 `resources/INDEX.md` — 確認可用工具與技能
3. 讀 `CONFIG/INDEX.md` — 讀取框架設定
4. `mneme.switch_scope("<專案名>")` — 切換 scope
5. 檢查專案 `.agent/TASKS/` — 處理未完成任務

### 安全規則

- **D:\Agent 所有內容僅供參考** — agent 不應修改此目錄下的任何檔案
- 跨路徑參考僅供讀取，寫入操作限於目前專案的 `.agent/` 目錄
- agent 不應在 C 槽非必要路徑寫入檔案
- 發現新工具時，寫到專案 `.agent/Tools/`，非 `D:\Agent\resources/tools/`

---

## 使用時查找

| 需要 | 位置 |
|------|------|
| 初始化新專案（從零建 .agent/） | `python D:\Agent\template\bootstrap.py <路徑>` |
| 連同工具範本一起初始化 | `python D:\Agent\template\bootstrap.py <路徑> --tools` |
| 工具清單與用法 | `D:\Agent\TOOLS/` |
| 重啟 OpenCode | `D:\Agent\TOOLS\local\restart-opencode\` 或 `resources/skills/restart-opencode.md` |
| 新機台工具起始參考 | `D:\Agent\template\resources/tools/` |
| 技能定義 | `D:\Agent\resources/skills/` |
| 通用參考 | `D:\Agent\resources/reference/` |
| 任務結構與生命週期 | 下方「任務管理」 |
| Session 日誌格式 | 下方「LOGS 寫法」 |
| 跨 Agent 記憶操作 | `resources/tools/` 內搜尋 `mneme` |

---

## 任務管理

### 任務類型

- **Standing** — 一次性任務，完成後標記 `completed` 並填入 `verified: YYYY-MM-DD`。下次 session 若 `verified == today` 則跳過，否則重新確認。
- **Adhoc** — 臨時任務，完成後移至 `RESULTS/` 或清除。
- **Scheduled** — 排程任務，使用 `YYYY-MM-DD-NNN` 命名，依日期執行。

### 檔案格式

每個任務目錄至少包含一個說明檔案（INDEX.md 或 checklist.md），格式不拘。狀態以 `status:` 欄位或 checklist 完成度判定。

### 生命週期

- Standing 完成後保留原地（標記 completed）
- Adhoc 完成後移到 RESULTS/ 或清除
- Scheduled 完成後移到 RESULTS/

---

## 結果歸檔

```
RESULTS/<task-name>/
├── INDEX.md   # 成果說明
└── summary.md # 總結（選配）
```

格式不拘，重點是說明做了什麼、達成了什麼。

---

## LOGS 寫法

每次 session 結束時寫一個檔案到 `.agent/LOGS/`，命名為 `YYYY-MM-DD.md`：

```markdown
# YYYY-MM-DD

## 完成
- 本次完成的事

## 待辦
- 下次要做的（選配）
```

3-5 行即可，不需完整格式。

---

## 工具管理

### 查找順序

1. 先查專案 `.agent/Tools/` — 專案自用工具
2. 再查 `D:\Agent\resources/tools/common/` — 跨專案通用工具
3. 最後查 `D:\Agent\resources/tools/local/` — 本機限定工具

### 新增工具

- 專案自用 → 寫到 `.agent/Tools/<工具名>/INDEX.md`
- 跨專案通用 → 寫到 `D:\Agent\resources/tools/common/`
- 本機限定 → 寫到 `D:\Agent\resources/tools/local/`
- 若工具值得共享，可補進 `template/resources/tools/` 後送 PR

### 目錄說明

- `D:\Agent\resources/tools/` 不進 git，各機台依狀況自行維護
- `template/resources/tools/` 進 git，作為新機台起始參考

---

## mneme 設定

- `D:\Agent\resources\tools\common\mneme\mneme.exe` — 記憶後端二進位
- 資料目錄：`~/.mneme/`
- 專案隔離：使用 `switch_scope("<project-name>")`
- 跨 session 記憶：使用 `remember`/`recall`

---

## 檔案命名慣例

- `.txt` — for human users; content in Traditional Chinese
- `.md` — for AI agents; content in English (or bilingual where shared)
- If efficiency is critical, both formats may use English

---

## 資料同步規範

- **MD 檔案** — 兩岸同步的知識，跨機台共享
- **mneme memory** — 個人進度、臨時決策、session 間的上下文，不跨機台
- **git commit** — 程式碼變更，跨機台同步
