#!/usr/bin/python3

"""
This module defines the Square class.
"""


class Square:
    """
    This class represents a square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square object with an optional size.

        Args:
            size (float or int): The size of the square. Default is 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Args:
            value (float or int): The size of the square.

        Raises:
            TypeError: If value is not a number (float or integer).
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Equality comparison for two squares based on their areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """
        Inequality comparison for two squares based on their areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the areas are not equal, False otherwise.
        """
        return not self.__eq__(other)

    def __gt__(self, other):
        """
        Greater than comparison for two squares based on their areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area is greater, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        raise TypeError("'>': unsupported operand type(s) for Square and {}".format(type(other)))

    def __ge__(self, other):
        """
        Greater than or equal to comparison for two squares based on their areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area is greater or equal, False otherwise.
        """
        return self.__gt__(other) or self.__eq__(other)

    def __lt__(self, other):
        """
        Less than comparison for two squares based on their areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area is less, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        raise TypeError("'<': unsupported operand type(s) for Square and {}".format(type(other)))

    def __le__(self, other):
        """
        Less than or equal to comparison for two squares based on their areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the area is less or equal, False otherwise.
        """
        return self.__lt__(
