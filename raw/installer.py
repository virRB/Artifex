import os
import winreg
import ctypes
import subprocess
import time
import shutil
from pathlib import Path

RESET = "\033[0m"
CYAN = "\033[36m"

subprocess.run("cls", shell=True)

BASE = os.path.dirname(os.path.abspath(__file__))

def addToPath(new_path: str):
    new_path = os.path.abspath(new_path)

    with winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        "Environment",
        0,
        winreg.KEY_READ | winreg.KEY_WRITE
    ) as key:

        try:
            current_path, _ = winreg.QueryValueEx(key, "Path")
        except FileNotFoundError:
            current_path = ""

        paths = current_path.split(";") if current_path else []

        if any(
            os.path.normcase(os.path.normpath(p)) ==
            os.path.normcase(os.path.normpath(new_path))
            for p in paths
        ):
            print("Already in PATH")
            return

        updated_path = (
            current_path + ";" + new_path
            if current_path else
            new_path
        )

        winreg.SetValueEx(
            key,
            "Path",
            0,
            winreg.REG_EXPAND_SZ,
            updated_path
        )

    HWND_BROADCAST = 0xFFFF
    WM_SETTINGCHANGE = 0x001A

    result = ctypes.c_ulong()

    ctypes.windll.user32.SendMessageTimeoutW(
        HWND_BROADCAST,
        WM_SETTINGCHANGE,
        0,
        "Environment",
        0,
        5000,
        ctypes.byref(result)
    )


input("Press Enter to install Artifex > ")

new = Path.home() / "artifex"

if os.path.exists(new):
    shutil.copytree(BASE, new, dirs_exist_ok=True)
else:
    shutil.copytree(BASE, new)

addToPath(str(new))

for i in range(20):
    print(f"\rInstalling files: {CYAN}|{'=' * i}|{RESET}", end="", flush=True)
    time.sleep(0.05)

for i in range(20):
    print(f"\rUpdating PATH:   {CYAN}|{'=' * i}|{RESET}", end="", flush=True)
    time.sleep(0.05)

print(f"\n{CYAN}Installation complete! Installed Artifex to: {new}{RESET}")
print("Restart your terminal before using the artifex command.")