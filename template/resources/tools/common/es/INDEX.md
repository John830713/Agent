# es — Everything Search CLI

Command-line interface for Voidtools Everything — instant file search across NTFS volumes.

## Entity location

`D:\Agent\resources\tools\common\es\`

## Usage

```powershell
# Search files by name
D:\Agent\resources\tools\common\es\es.exe -n filename.txt

# Search with regex
D:\Agent\resources\tools\common\es\es.exe -r ".*\.log$"

# Search in a specific folder
D:\Agent\resources\tools\common\es\es.exe -path D:\SomeFolder -n query
```

## Key flags

| Flag | Description |
|------|-------------|
| `-n <name>` | Search by filename (supports wildcards: `*.txt`) |
| `-r <regex>` | Regex filename search |
| `-path <dir>` | Limit search to a directory |
| `-s` | Match case-sensitive |
| `-w` | Match whole word only |
| `-sort <field>` | Sort by: name, path, size, date-run, date-modified, date-created |
| `-instance <n>` | Use non-default Everything instance (if multiple are running) |

## Notes

- Requires Everything service (`Everything.exe -svc`) to be running on the machine
- Returns results instantly — good for searching across large codebases
- Paths are returned as absolute Windows paths

## Referenced by

- [tools/common/INDEX.md](../INDEX.md)
