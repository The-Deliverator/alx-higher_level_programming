#!/usr/bin/python3
"""
Writes a string to a .txt file (UTF8) and returns the number of chars
written
"""


def write_file(filename="", text=""):
    """
    Args:
        filename: The name of the file to write into
        text: The text to be written in the file

    Return:
        The number of chars written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
