#!/usr/bin/python3
"""
a class, Square, that inherits from Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    The class inherited from rectangle
    """

    def __init__(self, size):
        """
        Initializing the class with dimensions
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Returns the area of the class
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns the description of the class
        """
        return f"[Rectangle] {self.__size}/{self.__size}"
