#!/usr/bin/python3
"""
Reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    Args:
        filename: The name of the file to be read
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
