# Mneme — Persistent Memory

Cross-session semantic memory for facts, decisions, preferences, and events.

## When to use

- Remembering decisions and reasoning from earlier sessions
- Recording user preferences about tools, style, or workflow
- Pinning persistent rules that should apply every session
- Tracking milestone events and session summaries

## Available operations

| Operation | Use case |
|-----------|----------|
| `remember` | Store a fact, decision, or preference |
| `recall` | Search memory by semantic similarity |
| `pin` | Promote a rule to procedural memory (loaded every session) |
| `record_event` | Time-anchored event log (milestones, messages) |
| `recall_recent` | Query recent events within a time window |
| `summarize_session` | Generate a prompt template for session summarization |
| `stats` | Check memory store health |
| `forget` | Delete a specific memory |

## Steps

1. **Identify what to store** — facts, decisions, preferences, or events
2. **Call the appropriate operation** — `remember` for durable facts, `record_event` for transient events
3. **Keep it concise** — target under 500 characters; hard limit at 10,000
4. **Verify** — `stats()` to confirm storage; `recall(query)` to confirm retrieval

## Gotchas

- **Size limits** — memories over 10,000 chars are rejected. Extract the key insight.
- **DO NOT store** — code contents, tool outputs, whole conversations, transient state
- **Scope isolation** — `switch_scope("<project>")` separates memories by project
- **Not cross-machine** — mneme data lives in `~/.mneme/`, not synced via git
- **L1 (working) vs L3 (episodic)** — conversation turns auto-record; don't duplicate them with `record_event`
- **`forget` is permanent** — confirm before deleting
