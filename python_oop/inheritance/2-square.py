#!/usr/bin/env python3
"""
Module square

Defines the Square class.
"""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a square.

        Args:
            size (int): size of the square
        """
        self.integer_validator("size", size)

        self.__size = size

        super().__init__(size, size)

