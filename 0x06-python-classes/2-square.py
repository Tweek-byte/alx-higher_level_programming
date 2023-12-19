#!/usr/bin/python3
"""Defines a square with a private instance attribute 'size'."""


class Square:
    """Represents a square.

    Attributes:
        __size (int): Size of a side of the square.
    """
    def __init__(self, size=0):
        """Initializes a square with a specified size.

        Args:
            size (int): The size of the side of the square. Default is 0.

        Raises:
            ValueError: If size is less than 0.
            TypeError: If size is not an integer.
        """
        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')
