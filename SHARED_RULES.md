# Shared Rules — Agent Framework Base

All projects under `D:\` should reference this file via `opencode.json`:

```json
"instructions": ["AGENTS.md", "D:\\Agent\\SHARED_RULES.md"]
```

Project-specific `AGENTS.md` only needs to contain project-specific rules.

---

## Language

- 一般回答、解釋、溝通：使用**繁體中文**（臺灣正體）
- 程式碼、函式名稱、變數名稱、註解：使用**英文**
- 混合內容（例如解釋一段程式碼）：說明部分用繁體中文，程式碼本身用英文

## Git

- Every file change must be committed immediately. Don't batch.
- Commit messages in English.
- Don't push unless asked.
- Revert safely — `git stash` or `git commit` first. Never overwrite uncommitted work.

## Safety

- Never modify `.opencode/` — infrastructure files, breaks opencode loading.
- Write temp files to `.agent/`, not project root.
- No random `C:\` writes.

## INDEX Chain

When you need to understand how something works:

1. Start at `resources/INDEX.md`
2. Follow sub-INDEX.md to the right file
3. Don't skip — unless the answer is trivially obvious

Cross-project references:
- `D:\Agent\resources\reference\` — framework-level rules and tools
- `D:\Agent\resources\tools\common\` — shared tool documentation
