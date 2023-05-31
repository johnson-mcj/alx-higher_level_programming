#!/usr/bin/python3
"""
Module documentation: Square
"""


class Square:
    """
    Square class represents a square shape.
    """

    def __init__(self, size=0):
        """
        Initializes a Square object with a given size.

        Args:
            size (int or float): The size of the square.

        Raises:
            TypeError: If the size is not a number (int or float).
            ValueError: If the size is less than 0.
        """
        self.__size = 0
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int or float: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int or float): The size value to be set.

        Raises:
            TypeError: If the size is not a number (int or float).
            ValueError: If the size is less than 0.
        """
        if type(value) not in [int, float]:
            raise TypeError('size must be a number')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            float: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Implements the equality comparison between two squares.

        Args:
            other (Square): The other square object to compare.

        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Implements the inequality comparison between two squares.

        Args:
            other (Square): The other square object to compare.

        Returns:
            bool: True if the areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Implements the greater than comparison between two squares.

        Args:
            other (Square): The other square object to compare.

        Returns:
            bool: True if the area is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Implements the greater than or equal comparison between two squares.

        Args:
            other (Square): The other square object to compare.

        Returns:
            bool: True if the area is greater than or equal, False otherwise.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Implements the less than comparison between two squares.

        Args:
            other (Square): The other square object to compare.

        Returns:
            bool: True if the area is less, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Implements the less than or equal comparison between two squares.

        Args:
            other (Square): The other square object to compare.

        Returns:
            bool: True if the area is less than or equal, False otherwise.
        """
        return self.area() <= other.area()
