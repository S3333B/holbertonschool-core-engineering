#!/usr/bin/env python3
"""A function that writes a string to a text file (UTF8)
and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.

    Args:
        filename (str): Name of the file.
        text (str): Text to write in the file.

    Returns:
        int: Number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as my_file:
        return my_file.write(text)
