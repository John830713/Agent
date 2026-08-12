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
| [chain/](chain/INDEX.md) | INDEX chain specification |
| [conventions/](conventions/INDEX.md) | File naming, data sync |
| [design/](design/INDEX.md) | UI pattern library |
| [git/](git/INDEX.md) | Git commit rules, workflow, safety |
| [log/](log/INDEX.md) | Session log format |
| [mneme/](mneme/INDEX.md) | Mneme capacity, scope, session flow |
| [opencode/](opencode/INDEX.md) | OpenCode app rules, restart, send-to-self |
| [result-archive/](result-archive/INDEX.md) | Result archive format and location |
| [task/](task/INDEX.md) | Task file format |
| [tool/](tool/INDEX.md) | Tool management, registration, tracking |

> Template only carries framework-generic topics. Machine-specific topics
> (e.g. `llama/`, `toolchain/`, project references) stay in the machine's own
> `resources/reference/` and are never copied into `template/`.

## Referenced by

- [INDEX.md](../INDEX.md)
