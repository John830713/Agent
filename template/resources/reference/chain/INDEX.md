# INDEX chain — Specification v1

## 1. Purpose

The INDEX chain is a bidirectional linked-list structure over directories, where each node is a directory containing:
- `INDEX.md` — human/agent readable content
- `.index.json` — machine-readable metadata (links + version)

This enables an agent to navigate the framework's documentation tree lazily, reading only what it needs.

## 2. Node rules

Every node directory must contain:
- `INDEX.md` — with `## Forward links` and `## Referenced by` sections
- `.index.json` — matching the schema below

Leaf nodes (no sub-nodes) have an empty `forward` array.

## 3. `.index.json` schema

```json
{
  "version": 1,
  "forward": ["child-dir/"],
  "referenced_by": ["../parent-dir/INDEX.md"]
}
```

| Field | Required | Description |
|-------|----------|-------------|
| `version` | Yes | Schema version (integer). Must match across all nodes. |
| `forward` | Yes | Array of child directory paths (relative to this JSON). Empty for leaf nodes. |
| `referenced_by` | Yes | Array of parent file paths (relative to this JSON) that reference this node. |

## 4. Chain rules

- **Forward links** — parent → child. `forward` entries point from a node to its sub-nodes.
- **Backward links** — child → parent. `referenced_by` entries point from a node to its parent INDEX.md.
- Every `forward` entry must have a matching `referenced_by` entry in the target.
- Every `referenced_by` entry must have a matching `forward` entry in the source.

## 5. Version policy

- All `.index.json` files must have the same `version` value.
- When the schema changes, all nodes are updated together.
- `chain-check --init` validates version consistency before running.

## 6. Referenced by

- `reference/INDEX.md` → Chain section
