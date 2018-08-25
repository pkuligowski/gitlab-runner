"""
Setup file for cx_freeze
"""
import sys
from cx_Freeze import setup, Executable


setup(name = "main",
        version = "0.1",
        description = "My application!",
        executables = [Executable("src/main.py", base=None)])
