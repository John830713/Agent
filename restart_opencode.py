import subprocess, time, os, signal, sys

mneme_bin = os.path.expandvars(r"%LOCALAPPDATA%\Programs\mneme\mneme.exe")
opencode_bin = os.path.expandvars(r"%LOCALAPPDATA%\Programs\@opencode-aidesktop\OpenCode.exe")

if not os.path.exists(mneme_bin):
    print("mneme not found at", mneme_bin)
    sys.exit(1)

if not os.path.exists(opencode_bin):
    print("OpenCode not found at", opencode_bin)
    sys.exit(1)

time.sleep(3)

subprocess.run(["taskkill", "/f", "/im", "OpenCode.exe"], capture_output=True)
time.sleep(2)

subprocess.Popen([opencode_bin], shell=True)
print("OpenCode restarted")
