#!/usr/bin/python3
"""
Writes an object to a .txt file, using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Args:
        my_obj: The str to be written to the filename
        filename: The file we are going to be writing to
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
