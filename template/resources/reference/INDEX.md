# Reference

Rules, conventions, and notes organized by topic.

**Agent instruction**: read `.local-cache/reference.md` in the parent `resources/` directory for available reference topics. If the cache does not exist, run the scan tool to regenerate it.

## Registration

When a project provides reference docs, create a subdirectory here with `INDEX.md`. Then run:

```powershell
python D:\Agent\resources\tools\common\tool-registry\scan.py
```

## Forward links

| Path | Description |
|------|-------------|
| [design/](design/INDEX.md) | Tampermonkey UI pattern library |
| [log/](log/INDEX.md) | Session log format |
| [conventions/](conventions/INDEX.md) | File naming, data sync |
| [git/](git/INDEX.md) | Git commit rules, workflow, safety |
| [mneme/](mneme/INDEX.md) | Mneme capacity, scope, session flow |
| [opencode/](opencode/INDEX.md) | OpenCode app rules, restart, send-to-self |
| [chain/](chain/INDEX.md) | INDEX chain specification |

## Referenced by

- [INDEX.md](../INDEX.md)
