# Usage

## Basic

```powershell
python Tools\native_analyzer.py D:\target.exe
```

## Manual address inspection

```powershell
& "D:\Program Files\MSYS2Portable\App\msys64\ucrt64\bin\objdump.exe" -d --demangle --start-address=0x140001490 --stop-address=0x1400014f0 target.exe
```

## Notes

- Byproducts in `tmp/` at exe directory
- Stripped EXEs show only `.text` entry
