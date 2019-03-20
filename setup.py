import sys
from cx_Freeze import setup, Executable

setup(
    name = "Uzlaş Bakalım",
    version = "1.0",
    description = "Open Source Uzlaşma Programı",
    executables = [Executable("gui.py", base = "Win32GUI", icon = "logo.ico")])