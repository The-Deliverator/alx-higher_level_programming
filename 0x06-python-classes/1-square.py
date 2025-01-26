#!/usr/bin/python3
"""Defines a class, Square"""


class Square:
    """The class, Square, with a private size attribute"""

    def __init__(self, size):
        """Initializes the class, Square.

        Args:
            size (int): size to be set
        """
        self.__size = size
