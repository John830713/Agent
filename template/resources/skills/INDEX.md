# Skills

Skill definitions live in `D:\Agent\resources/skills/`. This directory exists
for new-machine bootstrap — after copy, populate from the live Agent.

**Agent instruction**: read `.local-cache/skills.md` in the parent `resources/` directory for available skills. If the cache does not exist, run the scan tool to regenerate it.

## Registration

When a project provides a skill, place the `.md` file here. Then run:

```powershell
python D:\Agent\resources\tools\common\tool-registry\scan.py
```

## Forward links

*(None — skill files are not packaged in template)*

## Referenced by

- [INDEX.md](../INDEX.md)
