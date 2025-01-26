#!/usr/bin/python3
"""Defines a class, Square"""


class Square:
    """
    A class used to represent a Square

    __size : int
        the size of the square's side
    """
    def __init__(self, size=0):
        """
        size: int
            The size of the square's side
        Raises:
            TypeError: If size is not an int
            ValueError: If size < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns:
            int - The area of the square
        """
        return self.__size ** 2
