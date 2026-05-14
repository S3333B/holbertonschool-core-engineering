#!/usr/bin/env python3
"""
Module base_geometry

Defines the BaseGeometry class.
"""


class BaseGeometry:
    """
    Base class for geometric shapes.
    """

    def area(self):
        """
        Raises an exception because area is not implemented.

        Raises:
            Exception: always raised with a specific message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer.

        Args:
            name (str): name of the parameter
            value (int): value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value <= 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
