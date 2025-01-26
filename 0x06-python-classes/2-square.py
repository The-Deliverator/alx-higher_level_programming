#!/usr/bin/python3
"""Defines a class, Square"""


class Square:
    """The class, Square, with a private instance attribute
    Args:
        size: The size of the square to be set
    Raises:
        TypeError: When size is not an int
        ValueError: When size < 0
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
