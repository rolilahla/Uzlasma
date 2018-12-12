import sys
from cx_Freeze import setup, Executable

setup(
    name = "Uzlaş Bakalım",
    version = "1.0",
    description = "İşin sırrı kahve içmekte",
    executables = [Executable("gui.py", base = "Win32GUI", icon = "logo.ico")])