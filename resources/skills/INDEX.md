# Skills

Reusable AI agent skills. Each skill is a folder containing a `SKILL.md` in the Agent Skills format (YAML frontmatter with `name` + `description`; progressive disclosure keeps startup context small).

**Agent instruction**: read `.local-cache/skills.md` in the parent `resources/` directory for available skills. If the cache does not exist, run the scan tool to regenerate it.

## Skills

| Skill | Description |
|-------|-------------|
| `mneme/SKILL.md` | Cross-session persistent memory (mneme MCP server) |
| `opencode/SKILL.md` | Operate the OpenCode desktop app (restart, send message) |
| `llama-server/SKILL.md` | llama.cpp server startup & API (entity: `D:\llama`) |
| `llama-update/SKILL.md` | Update llama.cpp binaries (entity: `D:\llama`) |
| `task-authoring/SKILL.md` | Generator task authoring format (entity: `D:\Tampermonkey`) |
| `troubleshooting/SKILL.md` | Browser automation troubleshooting (entity: `D:\Tampermonkey`) |
| `web-operation/SKILL.md` | Browser automation guide (entity: `D:\Tampermonkey`) |

## Registration

To add a skill, create a folder `<skill-name>/` containing `SKILL.md` (Agent Skills format). If it is a registration pointer to an entity file in another project, include `## Entity location`. Then run:

```powershell
python D:\Agent\resources\tools\common\tool-registry\scan.py
```
