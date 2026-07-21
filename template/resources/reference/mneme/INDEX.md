# mneme — Rules & Notes

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

- [reference/INDEX.md](../INDEX.md)
