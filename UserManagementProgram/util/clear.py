import os
import platform

def consoleClear():
    if platform.system().lower().find("windows") != -1:
        os.system('cls')  # windows
        print("\n" * 20)
    else:
        os.system('clear')  # linux, mac
