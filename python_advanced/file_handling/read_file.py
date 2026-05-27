#!/usr/bin/env python3
def read_file(filename=""):
    """Read a UTF-8 text file and print it to stdout."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
