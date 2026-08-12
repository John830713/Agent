# mneme — Rules & Notes

## Quick facts

- Binary: `D:\Agent\resources\tools\common\mneme\mneme.exe`
- Data dir: `~/.mneme/`
- Project isolation: use `switch_scope("<project-name>")`
- Cross-session memory: `remember` / `recall` / `pin`

## Capacity

- Target under 500 characters per memory
- Hard limit at 10,000 characters — rejected beyond that
- Embedding model determines search quality

## What NOT to store

- Source code (read from disk each session)
- Tool outputs (captured automatically)
- Whole conversations
- Current project state or transient task progress

## Scope isolation

- `switch_scope("<project>")` separates memories per project
- Default scope is `global` — always switch before writing
- Writes without scope filter land in the active scope

## Windows limitation

Daemon/client mode (`mneme daemon` + `mneme client`) is **not available on Windows** — the daemon transport requires Unix domain sockets; Windows named-pipe support is planned for M4. On Windows, always use `mneme run`.

## Multi-project setup (Windows)

OpenCode 內建多專案模式中，切換專案時 MCP 連線會中斷。加上 mneme daemon/client 在 Windows 不支援，**每個專案必須各自宣告 `mcp.mneme`**：

```json
{
  "mcp": {
    "mneme": {
      "command": ["D:\\Agent\\resources\\tools\\common\\mneme\\mneme.exe", "run"],
      "enabled": true,
      "type": "local",
      "timeout": 120000
    }
  }
}
```

這樣至少在同一個專案內關閉重開後 MCP 會正常運作。

## Data directory

- `~/.mneme/` — not synced across machines
- Each machine maintains its own mneme data
- `forget` is permanent — no undo

## Session flow

- `mneme://procedural` — pinned rules load every session start
- `mneme://context` — recent events auto-loaded
- `record_event` for time-anchored events (milestones, messages)
- `summarize_session` + LLM completion for session digests

## Agent instruction protocol

Reference files may contain a `**Agent instruction**` block at the top of the file. This is a binding directive — the agent **must** execute the specified mneme action on first read in a session.

Pattern:
```markdown
**Agent instruction**: when first reading this file in a session, call `mneme_pin` with the rule below.
```

Rules:
- Only one `**Agent instruction**` block per file
- Action must be a mneme tool call (`mneme_pin`, `mneme_remember`, etc.)
- Agent must not skip or defer — execute immediately on first read
- This is how reference files proactively register rules into procedural memory without relying on the agent to "figure it out"

## Referenced by

- `resources/reference/INDEX.md` → Subtopic listing
- `resources/INDEX.md` → Tools section
- `AGENTS.md` → Quick reference
