# native_analyzer.py

Native C/C++ PE analysis tool. Wraps MSYS2 objdump + c++filt + addr2line.

## Use cases

- MinGW-w64 / MSVC compiled C/C++ EXE analysis
- Section layout, import DLL, function list
- Unpacked or unstripped native EXE

## Limitations

- Requires MSYS2 tools (objdump / c++filt / addr2line)
- Stripped EXEs show only raw `.text` section, no function names
