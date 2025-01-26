#!/usr/bin/python3
"""
A function that returns the list of available attributes and methods
of an object
"""


def lookup(obj):
    """
    Args:
        obj: The object to be inspected
    Return:
        A list object
    """
    return dir(obj)
