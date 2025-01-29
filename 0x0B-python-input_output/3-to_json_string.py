#!/usr/bin/python3
"""
Returns the JSON representation of an object (string)
"""


import json


def to_json_string(my_obj):
    """
    Args:
        my_obj: The object whose JSON representation is to be returned

    Return:
        The JSON representation of my_obj
    """
    return json.dumps(my_obj)
