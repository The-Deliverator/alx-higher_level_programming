#!/usr/bin/python3
"""
A class, MyList, that inherits from list
"""


class MyList(list):
    """
    Class, MyList, inherits from list
    """

    def print_sorted(self):
        """
        Prints list using ascending sort
        """
        print(sorted(self))
