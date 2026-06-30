# Task Schema — 任務目錄規範

## 必要檔案

```
Task-Name/
├── INDEX.md        # 任務說明書
├── plan.md         # 任務計畫（目標、範圍、方法）
└── checklist.md    # 檢查清單（逐項標記完成狀態）
```

## INDEX.md 格式

```markdown
# Task-Name

status: pending | in_progress | completed | cancelled

## 說明

任務的描述與目的。

## 備註

其他注意事項。
```

## plan.md 格式

```markdown
# 計畫

## 目標

## 範圍

## 方法 / 步驟

## 依賴
```

## checklist.md 格式

使用 GFM task list：

```markdown
# 檢查清單

## Phase 1
- [ ] 項目一
- [x] 項目二（已完成）

## Phase 2
- [ ] 項目三
```

## 狀態判定規則

- 所有項目 `[x]` → status: completed
- 部分 `[x]` → status: in_progress
- 全未勾 → status: pending
