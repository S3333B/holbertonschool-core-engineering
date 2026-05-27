#!/usr/bin/env python3
"""A function that appends a string at the end of a text
file (UTF8) and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """Append a string at the end of a UTF8 text file.

    Args:
        filename (str): Name of the file.
        text (str): Text to append in the file.

    Returns:
        int: Number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as my_file:
        return my_file.write(text)
