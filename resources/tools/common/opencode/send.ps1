param(
    [Parameter(Mandatory=$true)]
    [string]$Text
)

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

$procs = Get-Process | Where-Object { $_.MainWindowTitle -eq "OpenCode" }
if (-not $procs) {
    Write-Host "OpenCode window not found."
    exit 1
}

$hwnd = $procs[0].MainWindowHandle
[WinAPI]::SetForegroundWindow($hwnd) | Out-Null
Start-Sleep -Milliseconds 300

[System.Windows.Forms.Clipboard]::SetText($Text)
Start-Sleep -Milliseconds 100

[System.Windows.Forms.SendKeys]::SendWait("^v")
Start-Sleep -Milliseconds 100

[WinAPI]::SendEnter()
Write-Host "Sent: $Text"
