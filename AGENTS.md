# AGENTS.md

## What this repo is

This repo is a **framework of agent instructions**, not a software project. It defines how agents operate across projects. All dynamic data lives in each project's `.agent/` directory — never here.

`INDEX.md` is auto-loaded by `opencode.json` and explains the directory structure. Read it once, then rely on this file for operational guidance.

---

## Session start

### Startup flow

1. Read `INDEX.md` — understand framework structure
2. Read `resources/INDEX.md` — confirm available tools and skills
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

| Need | Path / Command |
|------|---------------|
| Init new project (from scratch) | `python D:\Agent\template\bootstrap.py <dir>` |
| Init with tool templates | `python D:\Agent\template\bootstrap.py <dir> --tools` |
| Tool docs listing | `D:\Agent\TOOLS/` |
| Tool docs (common / cross-project) | `D:\Agent\resources\tools\common\` |
| Tool docs (local / machine-specific) | `D:\Agent\resources\tools\local\` |
| Restart OpenCode + mneme daemon | `D:\Agent\resources\tools\common\restart-opencode\` or `resources/skills/restart-opencode.md` |
| New machine starting reference | `D:\Agent\template\resources/tools/` |
| Skill definitions | `D:\Agent\resources/skills/` |
| General reference | `D:\Agent\resources/reference/` |
| Task structure & lifecycle | See "Task management" below |
| Session log format | See "Session logs" below |
| Cross-agent memory operations | Search `mneme` under `D:\Agent\resources/tools/` |

---

## Task management

### Task types

- **Standing** — one-time task. Mark `completed` and set `verified: YYYY-MM-DD`. On next session, skip if `verified == today`, otherwise re-verify.
- **Adhoc** — temporary task. Move to `RESULTS/` or delete on completion.
- **Scheduled** — scheduled task. Named `YYYY-MM-DD-NNN`, executed by date, moved to `RESULTS/` on completion.

### File format

Each task directory needs at least one doc file (`INDEX.md` or `checklist.md`). Status is determined by a `status:` field or checklist completion.

### Lifecycle

- Standing: stays in place after completion (marked `completed`)
- Adhoc: moved to `RESULTS/` or cleared
- Scheduled: moved to `RESULTS/`

---

## Result archive

```
RESULTS/<task-name>/
├── INDEX.md   # What was done
└── summary.md # Summary (optional)
```

Free format. The key point is to explain what was done and what was achieved.

---

## Session logs

Write one file to `.agent/LOGS/YYYY-MM-DD.md` at session end:

```markdown
# YYYY-MM-DD

## Done
- what was done

## Next
- what to do next (optional)
```

3-5 lines. No need for full format.

---

## Tool management

### Lookup order

1. `<project>/.agent/Tools/` — project-specific tools
2. `D:\Agent\resources\tools/common/` — cross-project tools
3. `D:\Agent\resources\tools/local/` — machine-specific tools

### Adding tools

- Project-specific → `<project>/.agent/Tools/<name>/INDEX.md`
- Cross-project → `D:\Agent\resources\tools/common/<name>/`
- Machine-specific → `D:\Agent\resources\tools/local/<name>/`
- Worth sharing? Copy to `template/resources/tools/` and send a PR

### Git tracking notes

- `D:\Agent\resources/tools/` is mostly git-ignored (per `.gitignore` `/resources/`), except for tool binaries/scripts bundled in this repo (like `mneme.exe`, `restart-opencode.ps1`) which are force-tracked.
- `template/resources/tools/` is git-tracked and serves as the new-machine seed.

---

## mneme

- Binary: `D:\Agent\resources\tools\common\mneme\mneme.exe`
- Data dir: `~/.mneme/`
- Project isolation: use `switch_scope("<project-name>")`
- Cross-session memory: `remember` / `recall` / `pin`

---

## File naming convention

- `.txt` — for human users; content in Traditional Chinese
- `.md` — for AI agents; content in English (or bilingual where shared)
- If efficiency is critical, both formats may use English

---

## Data sync

- **MD files** — shared knowledge across machines, synced via git
- **mneme memory** — personal progress, ad-hoc decisions, session context; NOT cross-machine
- **git commit** — code changes, synced across machines
