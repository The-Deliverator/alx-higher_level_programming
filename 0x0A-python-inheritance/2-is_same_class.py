#!/usr/bin/python3
"""
Returns:
    True: If the object is exactly an instance of the specified class
    False: Otherwise.
"""


def is_same_class(obj, a_class):
    """
    Args:
        obj: The object to be checked
        a_class: The class to be checked against
    """
    return (type(obj) == a_class)
