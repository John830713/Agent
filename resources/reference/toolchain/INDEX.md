# MinGW-w64 toolchain (UCRT64) — Build configuration reference

## Target

`x86_64-w64-mingw32` — 64-bit Windows, UCRT (Universal C Runtime), static.

## Compiler flags (D:\Project Makefile)

| Flag | Purpose |
|------|---------|
| `-O2` | Optimize for speed |
| `-Wall` | Enable most warnings |
| `-std=c++17` | C++17 with GNU extensions |
| `-MMD -MP` | Auto-dependency generation (.d files) |
| `-static-libgcc -static-libstdc++ -static` | Fully static — no runtime DLLs |
| `-municode` | Use `wWinMain`/Unicode CRT entry |
| `-DDEBUG_CONSOLE=1` | Debug: `AllocConsole` + `DBG` traces |

## Install

Packaged as portable MSYS2: `D:\Program Files\MSYS2Portable`

| Runtime | Path |
|---------|------|
| C++ headers | `App\msys64\ucrt64\include\` |
| C++ stdlib | `App\msys64\ucrt64\lib\` |
| GCC libs | `lib/gcc/x86_64-w64-mingw32/16.1.0/` |

## Thread model

**posix** — MinGW-w64 with POSIX threading support (`-D_REENTRANT`). Enables `std::thread`, `std::mutex`, etc.

## Build commands (D:\Project)

| Command | What it does |
|---|---|
| `mingw32-make` | Release build |
| `mingw32-make debug` | Clean rebuild with `DEBUG_CONSOLE=1` (AllocConsole, full DBG traces) |
| `mingw32-make test` | Build + run all test targets (AutoKeyTest, TooltipTest, DebugStateTest) |
| `mingw32-make rebuild` | `clean` then `all` |
| `mingw32-make distclean` | `clean` + delete `GeneratedBuild.mk`, `GeneratedIcon.*`, `Translation\zh-TW.ini` (triggers full regeneration; does NOT delete `GeneratedModuleRegistry.*`) |
| `mingw32-make CXXFLAGS_EXTRA=-DDEBUG_CONSOLE=1` | **CAUTION**: incremental only — `main.o` / `DebugConsole.o` may not recompile. Prefer `Build.bat -debug` instead. |
| `py Build.py` | Regenerate `GeneratedBuild.mk`, `GeneratedModuleRegistry.*`, merged translations |
| `Build.bat` | Release build via MakePath.txt or MSYS2 (`clean` + `py Build.py` + `make`) |
| `Build.bat -debug` | Debug build (same but `CXXFLAGS_EXTRA=-DDEBUG_CONSOLE=1` — full rebuild guaranteed) |
| `Build.bat trim` | Release build + trim intermediate files |
| `py ProjectPackager.py --mode report` | Generate packaging report |
| `py ProjectPackager.py --mode export-clean` | Export a clean copy of the project |
| `py ProjectSnapshot.py [--summary\|--full]` | Generate a project context snapshot |

- Makefile auto-runs `py Build.py` if `GeneratedBuild.mk` or `Translation/zh-TW.ini` is missing.
- `Build.py` scans `Modules/*/*.module.ini`. No manual Makefile edits needed to add a module.
- `Debug/UI/GuiTest.cpp` exists but has no Makefile target — compile manually if needed.

### Shell environment

`mingw32-make` (MinGW-w64) uses `cmd.exe` as the shell **regardless** of the `SHELL` variable. All recipes must be cmd.exe-compatible:
- **No** `rm -f` → use `del /f`
- **No** POSIX `for f in ...; do ...; done` → use cmd.exe `for %f in (...) do @...`
- Paths need `$(subst /,\,...)` for `del` to work
- Clean target pattern: `-@del /f /q $(subst /,\,$(ALL_OBJS)) 2>nul`

## Pre-existing warnings

All current `-Wall` warnings are pre-existing (not caused by new code):

| Warning | Location |
|---------|----------|
| `winsock2.h before windows.h` | `Modules/RemoteControl/RemoteControlModule.h:9` |
| Unused variable `kv` | `Services/TranslationService.cpp:120` |
| Unused variables `act`, `ok` | `UI/SettingsDialog.cpp:403,591` |
| `PIK_SLIDER` not handled in switch | `Pet/MainWindow.cpp:1259` |

## Referenced by

- [reference/INDEX.md](../INDEX.md) → Subtopic listing
- [tools/local/msys2-portable/INDEX.md](../../tools/local/msys2-portable/INDEX.md) → Tool registration
- `D:\Project\resources\reference\INDEX.md` → Common references table
