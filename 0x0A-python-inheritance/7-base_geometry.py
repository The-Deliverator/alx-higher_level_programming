#!/usr/bin/python3
"""
Writes a class, BaseGeometry
"""


class BaseGeometry:
    """
    Class, BaseGeometry
    """
    def area(self):
        """
        Raises an exception with a message when called
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates value:
            value: Always str
            if value != int: Raise TypeError with message
            If value <= 0: Raise ValueError with message
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
