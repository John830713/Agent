# analyze.py

Universal EXE detection and classification. Pure Python 3 + struct, no 3rd-party dependencies.

## Use cases

- Unknown EXE quick classification (PyInstaller / .NET / Go / AutoIt / NSIS / Inno Setup / C++ / UPX)
- PyInstaller EXE auto-extraction + decompilation

## Limitations

- Does not handle ELF or Mach-O
- Does not actually unpack, only detects UPX marker

## Referenced by

- [tools/INDEX.md](../../INDEX.md)
