# Tools - 工具說明書目錄

AI agent 可自主查閱的工具清單。每個工具為一個獨立子目錄，包含 INDEX.md（用途）、spec.md（規格/API）和 usage.md（範例）。

## common/ - 跨專案通用工具

| 工具 | 用途 |
|------|------|
| [git](common/git/) | 版本控制操作 |
| [mneme](common/mneme/) | 持久記憶後端 |
| [analyze](common/analyze/) | 萬用 EXE 檢測（純 Python） |

## local/ - 本機限定工具

| 工具 | 用途 | 依賴 |
|------|------|------|
| [native_analyzer](local/native_analyzer/) | 原生 PE 分析 | objdump |
| [upx](local/upx/) | UPX 脫殼 | upx.exe |
| [pycdc](local/pycdc/) | Python 反編譯 | pycdc.exe |

## design/ - Tampermonkey UI design library

| 工具 | 用途 |
|------|------|
| [design](design/) | UI pattern library for Tampermonkey scripts |
