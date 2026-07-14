# Specification

## Interface / command

```
python Tools\native_analyzer.py <exe_path>
```

## Arguments

`exe_path` — target native PE path (required)

## Output

stdout:
- file format / architecture / EntryPoint
- Section list
- Import DLL and functions
- Disassembly function list (with source file if DWARF)
- C++ symbols path

Byproducts (in exe_path's tmp/):
- `{name}_disassembly.txt`
- `{name}_debug.txt`
- `{name}_cpp_symbols.txt`
