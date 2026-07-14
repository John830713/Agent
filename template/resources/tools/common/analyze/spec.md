# Specification

## Interface / command

```
python Tools\analyze.py <exe_path>
```

## Arguments

`exe_path` — target EXE path (required)

## Output

stdout output: file size / CPU architecture / Subsystem / EntryPoint / Section count / Import table / Classification (PyInstaller / .NET / Go / AutoIt / NSIS / Inno Setup / UPX / Native C/C++) / for PyInstaller: auto-extract + pycdc decompilation
