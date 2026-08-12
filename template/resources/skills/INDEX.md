# Skills

Skill definitions live in `D:\Agent\resources/skills/`. This directory is the
new-machine bootstrap seed — copy it over to get the framework skills in
Agent Skills format (folder per skill, `SKILL.md` with YAML frontmatter).

**Agent instruction**: read `.local-cache/skills.md` in the parent `resources/` directory for available skills. If the cache does not exist, run the scan tool to regenerate it.

## Registration

To add a skill, create a folder `<skill-name>/` containing `SKILL.md` (Agent Skills format), then run:

```powershell
python D:\Agent\resources\tools\common\tool-registry\scan.py
```

## Forward links

| Path | Description |
|------|-------------|
| [mneme/](mneme/SKILL.md) | Cross-session persistent memory (mneme MCP server) |
| [opencode/](opencode/SKILL.md) | Operate the OpenCode desktop app (restart, send message) |

## Referenced by

- [INDEX.md](../INDEX.md)
