#!/usr/bin/python3
"""
Module documentation: MagicClass
"""

import math


class MagicClass:
    """
    MagicClass represents a magical class with radius-based calculations.
    """

    def __init__(self, radius=0):
        """
        Initializes a MagicClass object with a given radius.

        Args:
            radius (int or float): The radius value for the MagicClass object.

        Raises:
            TypeError: If the radius is not a number (int or float).
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of the MagicClass object.

        Returns:
            float: The area of the MagicClass object.
        """
        return math.pi * self.__radius ** 2

    def circumference(self):
        """
        Calculates and returns the circumference of the MagicClass object.

        Returns:
            float: The circumference of the MagicClass object.
        """
        return 2 * math.pi * self.__radius
