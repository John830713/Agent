# Usage

## Unpack

```powershell
D:\Python_decompilation\Tools\upx.exe -d packed.exe -o unpacked.exe
```

## Analyze after unpack

```powershell
python Tools\analyze.py unpacked.exe
python Tools\native_analyzer.py unpacked.exe
```

## Notes

- Place unpacked files in `tmp/` to keep source directory clean
