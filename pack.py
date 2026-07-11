import subprocess
import sys

packages = [
    "sqlite3",      # Built-in
    "csv",          # Built-in
    "os",           # Built-in
    "datetime",     # Built-in
    "tkcalendar"    # External
]


def install_packages():
    subprocess.check_call(
            ["sudo",  "apt", "install", "python3-tk"]
        )
    for package in packages:
        subprocess.check_call(
            ["pip", "install", package]
        )
