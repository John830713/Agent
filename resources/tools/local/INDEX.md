# Local tools

Machine-specific tools — not shared across machines. Content varies per machine.

**Agent instruction**: read `.local-cache/tools.md` in the parent `resources/` directory for available tools. If the cache does not exist, run the scan tool to regenerate it.

## Registration

When a project provides a tool, create `INDEX.md` in a subdirectory here pointing back to the project's tool path. Then run:

```powershell
python D:\Agent\resources\tools\common\tool-registry\scan.py
```
