# Specification

## Interface

mneme provides tools through the MCP protocol. Connection is managed by OpenCode MCP config.

## Available tools

| Tool | Function |
|------|----------|
| `remember` | Store long-term memory (facts, decisions, preferences) |
| `recall` | Semantic memory search |
| `record_event` | Record events (milestones, messages) |
| `pin` | Pin rules to procedural memory |
| `recall_recent` | Query recent events by time |
| `summarize_session` | Generate session summary prompt |
| `stats` | View memory health status |
| `forget` | Delete memory |

## Data directory

`~/.mneme/` (fixed path, cannot be changed)
