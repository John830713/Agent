# Resources - 資源庫（New machine starting reference）

Copy this template to `D:\Agent\resources\` when setting up a new machine:

```powershell
Copy-Item -Recurse "D:\Agent\template\resources" "D:\Agent\resources"
```

## Structure

```
resources/
├── INDEX.md
├── tools/              # Tool specifications and usage
│   ├── common/         # Cross-project tools
│   └── local/          # Machine-specific tools
├── skills/             # Reusable AI agent skill definitions
└── reference/          # General reference material
    └── design/         # Tampermonkey UI pattern library
```

## Lookup order

1. Project `.agent/Tools/`
2. `D:\Agent\resources\tools\common/`
3. `D:\Agent\resources\tools\local/`

## Note

- This template is tracked by git and serves as the starting reference for new machines
- `D:\Agent\resources\` is NOT tracked by git, each machine maintains its own version
