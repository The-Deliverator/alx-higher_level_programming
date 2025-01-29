#!/usr/bin/python3
"""
Appends a string at the end of a .txt (UTF*) and returns the number
of chars added
"""


def append_write(filename="", text=""):
    """
    Args:
        filename: The name of the file to be appended
        text: The text to be appended to the .txt file

    Return:
        The number of chars that have been appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
