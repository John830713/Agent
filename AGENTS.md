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

0. **Read pinned rules** — read `mneme://procedural`; pinned items are binding rules for this session
1. **Read core navigation** — `INDEX.md`, `resources/INDEX.md`
2. **Detect changes** — run `chain_check.py --check` to find new/modified INDEX.md files; read only those
3. **Execute agent instructions** — reference files may have a `**Agent instruction**` block (e.g. `mneme_pin`); execute immediately on first read
4. `mneme.switch_scope("<project-name>")` — scope all memory writes to the active project
5. Check `<project>/.agent/TASKS/` — pick up unfinished work

New machine:
```powershell
Copy-Item -Recurse "D:\Agent\template\resources" "D:\Agent\resources"
```

### Safety rules

- **`D:\Agent\` is read-only from sub-projects** — agents in other projects (e.g. `D:\Tampermonkey`) must never modify files here
- **The agent on `D:\Agent` may modify it** — only with explicit instruction or as part of a defined task
- **Cross-path references are read-only** — writes go to the current project's `.agent/` only
- **No random `C:\` writes**
- **New tools for a project** → `<project>/.agent/Tools/`, not `D:\Agent\resources/tools/`
- **New tools for all machines** → `D:\Agent\template/resources/tools/` (via git), not `D:\Agent\resources/tools/`

---

## Key gotchas

- **`/resources/` is gitignored** — machine-local. Only `template/resources/` is tracked. New machines seed from `template/resources/`.
- **mneme** runs via MCP (`mneme.exe run`, 120s timeout). On Windows, daemon/client mode is unavailable (no Unix domain sockets). Each project must declare its own `mcp.mneme` in `opencode.json`.
- **Pre-commit hook** (`.githooks\pre-commit`) runs `chain_check.py --verify` — INDEX chain must pass before any commit.

---

## Quick reference

| Need | Location / Command |
|------|-------------------|
| Seed new machine | `Copy-Item -Recurse D:\Agent\template\resources D:\Agent\resources` |
| Restart OpenCode + mneme | `D:\Agent\resources\tools\common\opencode\restart.ps1` |
| Send message to OpenCode | `D:\Agent\resources\tools\common\opencode\send.ps1 -Text "msg"` |
| Rescan tool/skill/reference cache | `python D:\Agent\resources\tools\common\tool-registry\scan.py` |
| Check INDEX chain for changes | `python ...chain-check\chain_check.py --check` |
| Verify INDEX chain integrity | `python ...chain-check\chain_check.py --verify` |
| Auto-check command | `.opencode/commands/auto-check.md` |

Reference structure (start at `resources/INDEX.md`, follow sub-INDEX.md files):
| Area | Path |
|------|------|
| Cross-project tools | `resources/tools/common/` — mneme, chain-check, opencode, es, tool-registry |
| Machine-specific tools | `resources/tools/local/` — varies per machine |
| Reference rules | `resources/reference/` — git, mneme, tool management, conventions, logs, tasks |
| Skill files | `resources/skills/` |
| New-machine seed | `template/resources/` (git-tracked) |

## Session end

- **Check for pending changes** — `git status D:\Agent`; if uncommitted changes exist, offer to commit.
