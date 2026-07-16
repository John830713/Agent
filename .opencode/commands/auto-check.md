---
description: Verify INDEX chain integrity across the framework
---

## Chain structure

Every INDEX.md must have:

- **`## Forward links`** — links to child INDEX.md files (with paths)
- **`## Referenced by`** — links to parent files that reference this page

## Verification rules

1. **Forward link check** — for each `## Forward links` entry, the target path must exist on disk
2. **Backward link check** — for each `## Referenced by` entry, the parent file must exist and contain a matching `## Forward links` entry pointing back to this file
3. **Orphan check** — every INDEX.md in the chain must have at least one `## Referenced by` entry (except AGENTS.md, which is the root)

## Entry point

Start from `D:\Agent\AGENTS.md` and follow all Forward links recursively. Every reachable INDEX.md must pass all three checks.

## Report format

```
✅ resources/reference/git/INDEX.md — forward OK, backward OK
❌ resources/reference/foo/INDEX.md — Forward link target `bar/` missing
❌ resources/reference/git/INDEX.md — Referenced by `AGENTS.md` found, but no back-link in AGENTS.md
```
