# template

New project initialization template for the Project Memory Framework.

```
template/
├── .agent/           # Agent runtime skeleton (TASKS, RESULTS, LOGS)
├── resources/        # New machine starting reference for tools/skills/reference
└── bootstrap.py      # One-command project initializer
```

## Usage

```powershell
python D:\Agent\template\bootstrap.py <project-dir> [--tools]
```

`--tools` also copies template/resources/ into the project's .agent/Resources/ directory.
