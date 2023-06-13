#!/usr/bin/python3
"""
Defines the add_item function that adds arguments to a list and saves it to a JSON file
"""

import sys
import os.path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


def add_item(args, filename):
    """
    Add arguments to a list and save it to a JSON file

    Args:
        args (list): List of arguments
        filename (str): Name of the JSON file

    """
    if os.path.exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    my_list.extend(args)
    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    arguments = sys.argv[1:]
    add_item(arguments, "add_item.json")
