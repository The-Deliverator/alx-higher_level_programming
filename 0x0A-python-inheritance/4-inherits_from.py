#!/usr/bin/python3
"""
Returns:
    True: if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class
    False: Otherwise
"""


def inherits_from(obj, a_class):
    """
    Args:
        obj: The object to be checked
        a_class: The class to check against
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
