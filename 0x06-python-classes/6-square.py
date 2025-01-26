#!/usr/bin/python3
""" Define a class, Square"""


class Square:
    """ Defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """
        size:
        The size of the square's side
        position:
        The position of the square

        Raises:
        TypeError: If size is not an integer or position is not a tuple
        of 2 positive integers
        ValueError: If size is less than 0
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        int: The size of square's side
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Returns:
            tuple: Position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Raises:
            TypeError: If value is not a tuple of 2 positive integers
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints square with the character #
        If size = 0, prints an empty line
        """
        if self.__size == 0:
            print("")
            return

        [print("") for _ in range(self.__position[1])]
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
