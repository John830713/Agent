param(
    [Parameter(ParameterSetName="Text", Mandatory=$true)]
    [string]$Text,
    [Parameter(ParameterSetName="File", Mandatory=$true)]
    [string]$FilePath
)

# Force UTF-8 code page for console paste compatibility
chcp 65001 | Out-Null

Add-Type -AssemblyName System.Windows.Forms

Add-Type @"
using System;
using System.Runtime.InteropServices;

public class WinAPI {
    [DllImport("user32.dll")]
    public static extern bool SetForegroundWindow(IntPtr hWnd);

    [DllImport("user32.dll")]
    public static extern void keybd_event(byte bVk, byte bScan, uint dwFlags, UIntPtr dwExtraInfo);

    public const byte VK_RETURN = 0x0D;

    public static void SendEnter() {
        keybd_event(VK_RETURN, 0, 0, UIntPtr.Zero);
        keybd_event(VK_RETURN, 0, 2, UIntPtr.Zero);
    }
}
"@

# Read text from file or use direct parameter
if ($FilePath) {
    if (-not (Test-Path -LiteralPath $FilePath)) {
        Write-Host "File not found: $FilePath"
        exit 1
    }
    $text = [System.IO.File]::ReadAllText((Resolve-Path -LiteralPath $FilePath), [System.Text.Encoding]::UTF8)
} else {
    $text = $Text
}

$procs = Get-Process | Where-Object { $_.MainWindowTitle -eq "OpenCode" }
if (-not $procs) {
    Write-Host "OpenCode window not found."
    exit 1
}

$hwnd = $procs[0].MainWindowHandle
[WinAPI]::SetForegroundWindow($hwnd) | Out-Null
Start-Sleep -Milliseconds 300

[System.Windows.Forms.Clipboard]::SetText($text, [System.Windows.Forms.TextDataFormat]::UnicodeText)
Start-Sleep -Milliseconds 100

[System.Windows.Forms.SendKeys]::SendWait("^v")
Start-Sleep -Milliseconds 100

[WinAPI]::SendEnter()
Write-Host "Sent: $text"
