#!/usr/bin/python3
"""
A class, Rectangle, that inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    The class, Rectangle, inherited from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Initializes the rectangle using dimensions
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
