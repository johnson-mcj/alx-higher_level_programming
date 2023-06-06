#!/usr/bin/python3
"""
This is a module that contains a class that avoids dynamically created attributes.
"""

class LockedClass:
    """A class that prevents dynamically created attributes, except for 'first_name'."""

    __slots__ = ['first_name']

    def __init__(self):
        """Initialization method."""
        pass
