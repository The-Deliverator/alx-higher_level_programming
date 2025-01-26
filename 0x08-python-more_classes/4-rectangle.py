#!/usr/bin/python3
"""
Defines the class, Rectangle
"""


class Rectangle:
    """ Empty class, Rectangle"""
    def __init__(self, width=0, height=0):
        """ Initializes the class, Rectangle
        Args:
            Width: Width of the rectangle
            Height: Height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Gets the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle

        Raises:
            TypeError: If width is not an int
            ValueError: If width is < 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle

        Raises:
            TypeError: If height is not an int
            ValueError: If height < 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle

        Returns:
            The area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle

        Returns:
            The perimeter of the rectangle or 0 if
            height or width == 0
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self) -> str:
        """Prints the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ""
        for column in range(self.__height):
            for row in range(self.__width):
                rectangle += "#"
            if column < self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """
        Returns:
            String representation of the class, Rectangle
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
