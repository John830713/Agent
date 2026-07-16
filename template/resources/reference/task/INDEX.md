# Task management

## Types

| Type | Lifecycle | Naming |
|------|-----------|--------|
| **Standing** | Complete → mark `completed` + `verified: YYYY-MM-DD`. Re-verify only if `verified ≠ today`. | Freeform |
| **Adhoc** | Complete → move to `RESULTS/` or delete. | Freeform |
| **Scheduled** | Execute on date → move to `RESULTS/`. | `YYYY-MM-DD-NNN` |

## File format

Each task directory needs at least one doc file (`INDEX.md` or `checklist.md`). Status is determined by a `status:` field or checklist completion.

## Lifecycle

- Standing: stays in place after completion (marked `completed`)
- Adhoc: moved to `RESULTS/` or cleared
- Scheduled: moved to `RESULTS/`

## Referenced by

- [reference/INDEX.md](../INDEX.md)
