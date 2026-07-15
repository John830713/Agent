Start-Sleep -Seconds 5
$mneme = "$env:LOCALAPPDATA\Programs\mneme\mneme.exe"
$opencode = "$env:LOCALAPPDATA\Programs\@opencode-aidesktop\OpenCode.exe"
Start-Process -FilePath $mneme -ArgumentList "daemon" -WindowStyle Hidden
taskkill /f /im OpenCode.exe *>$null
Start-Sleep -Seconds 2
Start-Process -FilePath $opencode
