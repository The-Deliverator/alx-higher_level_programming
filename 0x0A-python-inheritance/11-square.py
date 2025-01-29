#!/usr/bin/python3
"""
a class, Square, that inherits from Rectangle
"""


class BaseGeometry:
    """
    A class with a public nstance method
    """
    def area(self):
        """
        Raises:
            an exception with a message when called
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value
        Raises:
            TypeError: If value != int
            ValueError: value <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than -".format(name))


class Rectangle(BaseGeometry):
    """
    Class, Rectangle, inherited from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Initialization of the Rectangle using dimensions
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Returns the area of class, Rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Description of class, rectangle
        """
        return f"[Rectangle] {self.__size}/{self.__height}"


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
        return self.__size * self.__size

    def __str__(self):
        """
        Returns the description of the class
        """
        return f"[Square] {self.__size}/{self.__size}"
