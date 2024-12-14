import os
import platform


# Clears the terminal screen based on the operating system.
def clear_screen():
     # Clear screen for Windows
    if platform.system() == "Windows":
        os.system("cls")
    else:
        # Clear screen for macOS/Linux
        os.system("clear")

