# Usage

## Basic

```powershell
python Tools\analyze.py target.exe
```

## PyInstaller

Auto-extract and decompile:

```powershell
python Tools\analyze.py myapp.exe
# -> myapp_extracted\ + decompiled .py
```

## Notes

- Creates `*_extracted\` temp directory in CWD
- Decompiled output placed in execution directory
