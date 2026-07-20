# MSYS2 Portable — MinGW-w64 toolchain

Windows x64 MinGW-w64 toolchain (UCRT64) packaged as portable.

**Installation:** `D:\Program Files\MSYS2Portable`

## Key executables

| Exe | Path | Purpose |
|-----|------|---------|
| `g++.exe` | `App\msys64\ucrt64\bin\g++.exe` | C++ compiler (GCC 16.1.0, Rev5 MSYS2) |
| `mingw32-make.exe` | `App\msys64\ucrt64\bin\mingw32-make.exe` | GNU Make for Windows |
| `windres.exe` | `App\msys64\ucrt64\bin\windres.exe` | Windows resource compiler |

## Usage

```powershell
# From project root, add to PATH or use full path:
& "D:\Program Files\MSYS2Portable\App\msys64\ucrt64\bin\mingw32-make.exe"
```

The project Makefile uses `mingw32-make` directly — assume it's on PATH or a `MakePath.txt` override points to it.

## Shell gotcha

`mingw32-make` invokes `cmd.exe` as the shell (ignoring `SHELL` env var). All recipes must be cmd.exe-compatible:
- No `rm -f` → `del /f`
- No POSIX `for f in ...; do ...; done` → `for %f in (...) do @...`
- Use `$(subst /,\,...)` for `del` paths

## Referenced by

- [tools/local/INDEX.md](../INDEX.md)
- [reference/toolchain/INDEX.md](../../reference/toolchain/INDEX.md) → Build configuration details
