# AGENTS.md

## What this repo is

This repo is a **framework of agent instructions**, not a software project. It defines how agents operate across projects. All dynamic data lives in each project's `.agent/` directory — never here.

`INDEX.md` is auto-loaded by `opencode.json` and explains the directory structure. Read it once, then rely on this file for operational guidance.

---

## Language

- 結論與總結 → 繁體中文
- 中間推理過程 → 可用英文
- 程式碼註解 → 全部英文

## Session start

### Startup flow

1. **Read core navigation** — `INDEX.md`, `resources/INDEX.md`, `CONFIG/INDEX.md`
2. **Load INDEX chain** — run `chain_check.py` to sync with cache:
   ```
   python D:\Agent\resources\tools\common\chain-check\chain_check.py
        --root D:\Agent --check
   ```
   If no cache exists (first run), use `--init` instead — this reads every INDEX.md in the chain and caches their hashes.
3. **Read changed nodes** — for each `[MOD]` or `[NEW]` line from step 2, read the corresponding INDEX.md. On first run (`--init`) this means all nodes.
4. `mneme.switch_scope("<project-name>")` — scope all memory writes to the active project
5. Check `<project>/.agent/TASKS/` — pick up unfinished work

If this is a **new machine**, copy the template resources first:
```powershell
Copy-Item -Recurse "D:\Agent\template\resources" "D:\Agent\resources"
```

### Safety rules

- **`D:\Agent\` is read-only reference** — never modify any file under this directory
- **Cross-path references are read-only** — writes go to the current project's `.agent/` directory only
- **No random C:\ writes** — keep the filesystem clean
- **New tools** go to `<project>/.agent/Tools/`, not `D:\Agent\resources/tools/`

---

## Operational flow

### Before any operation
- If the operation has a matching reference doc (e.g., git → `resources/reference/git/`), **read that INDEX.md first** before acting
- Reference INDEX.md files are already in context from the startup chain load — re-read only if context was lost

### Session end
- **Check for pending changes** — run `git status D:\Agent`; if there are uncommitted changes, offer to commit
- Run `chain_check.py --check` to refresh the cache so the next session picks up only what changed

---

## Quick reference

| Need | Path |
|------|------|
| Init new project | `python D:\Agent\template\bootstrap.py <dir>` |
| Init with tool templates | `python D:\Agent\template\bootstrap.py <dir> --tools` |
| Tool entity files | `D:\Agent\resources/tools/` |
| Skill usage guides | `D:\Agent\resources/skills/` |
| Rules, conventions, notes | `D:\Agent\resources/reference/` |
| Tool lookup & adding rules | `D:\Agent\resources/reference/tool/` |
| Task management | `D:\Agent\resources/reference/task/` |
| Result archive format | `D:\Agent\resources/reference/result-archive/` |
| Session log format | `D:\Agent\resources/reference/log/` |
| File naming & data sync | `D:\Agent\resources/reference/conventions/` |
| Git rules & workflow | `D:\Agent\resources/reference/git/` |
| mneme rules & limits | `D:\Agent\resources/reference/mneme/` |
| Restart OpenCode notes | `D:\Agent\resources/reference/restart-opencode/` |
| New machine seed | `D:\Agent\template/resources/` |
| Framework config | `D:\Agent\CONFIG/` |
| Auto-check command | `.opencode/commands/auto-check.md` |

---

## Referenced by

- *(Tip of the chain — no parents. All other INDEX.md files reference this file.)*
