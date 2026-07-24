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

0. **Read pinned rules** — read `mneme://procedural` and treat all pinned items as binding rules for this session.
1. **Read core navigation** — `INDEX.md`, `resources/INDEX.md`
2. **Read changed INDEX.md files** — scan `resources/` for directories with new or modified INDEX.md since last session.
3. **Execute agent instructions** — reference files may contain a `**Agent instruction**` block at the top (e.g. `mneme_pin`). Execute these immediately on first read.
4. `mneme.switch_scope("<project-name>")` — scope all memory writes to the active project
5. Check `<project>/.agent/TASKS/` — pick up unfinished work

If this is a **new machine**, copy the template resources first:
```powershell
Copy-Item -Recurse "D:\Agent\template\resources" "D:\Agent\resources"
```

### Safety rules

- **`D:\Agent\` is read-only from sub-projects** — agents working in other projects (e.g. `D:\Tampermonkey`) must never modify files under `D:\Agent\`
- **The agent working directly on `D:\Agent` may modify it** — but only with explicit user instruction or as part of a defined task
- **Cross-path references are read-only** — writes go to the current project's `.agent/` directory only
- **No random C:\ writes** — keep the filesystem clean
- **New tools for a project** go to `<project>/.agent/Tools/`, not `D:\Agent\resources/tools/`
- **New tools for all machines** go to `D:\Agent\template/resources/tools/` (via git), not `D:\Agent\resources/tools/`

---

## Operational flow

### Before any operation
- If the operation has a matching reference doc (e.g., git → `resources/reference/git/`), **read that INDEX.md first** before acting
- Reference INDEX.md files are already in context from the startup chain load — re-read only if context was lost

### Git commits
- Only commit when the user explicitly asks for it
- Never commit secrets or credentials
- Write concise commit messages describing the change

### Session end
- **Check for pending changes** — run `git status D:\Agent`; if there are uncommitted changes, offer to commit

---

## Gotchas

- **`/resources/` is gitignored** — it is machine-local. Only `template/resources/` is tracked. New machines must seed from `template/resources/`.
- **mneme MCP server** — runs as a local process (`mneme.exe run`) with 120s timeout. Memory writes should go through `mneme_remember`/`mneme_pin`, not file edits.

---

## Quick reference

| Need | Path |
|------|------|
| Shared rules for all projects | `D:\Agent\SHARED_RULES.md` |
| New machine seed | `Copy-Item -Recurse D:\Agent\template\resources D:\Agent\resources` |
| Template source files | `D:\Agent\template/resources/` |
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
| Restart OpenCode | `D:\Agent\resources\tools\common\opencode\restart.ps1` |
| Send message to self | `D:\Agent\resources\tools\common\opencode\send.ps1 -Text "msg"` |
| OpenCode notes | `D:\Agent\resources\reference\opencode\` |
| MSYS2/MinGW toolchain | `D:\Agent\resources\reference\toolchain\` |
| Framework config | *(removed)* |
| Auto-check command | `.opencode/commands/auto-check.md` |

---

## Referenced by

- *(Tip of the chain — no parents. All other INDEX.md files reference this file.)*
