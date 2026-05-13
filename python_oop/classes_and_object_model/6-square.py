#!/usr/bin/env python3
"""Defines a Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square with size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation."""

        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError(
                "position must be a tuple of 2 positive integers"
            )

        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using # and position."""

        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            print((" " * self.__position[0]) + ("#" * self.__size))

    def __str__(self):
        """Return the string representation of the square."""

        if self.__size == 0:
            return ""

        lines = []

        for i in range(self.__position[1]):
            lines.append("")

        for i in range(self.__size):
            lines.append(
                (" " * self.__position[0]) +
                ("#" * self.__size)
            )

        return "\n".join(lines)
