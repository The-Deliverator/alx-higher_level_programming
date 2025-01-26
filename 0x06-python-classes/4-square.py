#!/usr/bin/python3
"""
Defining a class, Square.
"""


class Square:
    """
    Description of the class, Square.

    Args:
        size - int. The size of the square
        Attributes - __size int - private instance attribute
    """
    def __init__(self, size=0):
        """
        Initializes the class, Square.
        Raises:
            TypeError: If size is not an int
            ValueError: If size < 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        """
        Retrieves size of the square
        """

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square
        Returns:
            The area of the square
        """
        return self.__size ** 2
