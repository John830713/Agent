# AGENTS.md

## What this repo is

This repo is a **framework of agent instructions**, not a software project. It defines how agents operate across projects. All dynamic data lives in each project's `.agent/` directory — never here.

`INDEX.md` is auto-loaded by `opencode.json` and explains the directory structure. Read it once, then rely on this file for operational guidance.

---

## Session start

### Startup flow

1. Read `INDEX.md` — understand framework structure
2. Read `resources/INDEX.md` — navigate to tools, skills, and reference docs
3. Read `CONFIG/INDEX.md` — load framework config
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
