#!/usr/bin/python3
"""Definition of the Square class"""


class Square:
    """Represents a square with a defined size.

    Attributes:
        __size (int): The size of a side of the square.
    """

    def __init__(self, size=0):
        """Initializes a square with a specified size.

        Args:
            size (int): The size of a side of the square. Default is 0.
        Returns:
            None
        """

        self.size = size

    def area(self):
        """Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """

        return self.size ** 2

    @property
    def size(self):
        """Getter method for the size of the square.

        Returns:
            int: The size of a side of the square.
        """

        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for the size of the square.

        Args:
            value (int): The size of a side of the square.
        Returns:
            None
        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is less than 0.
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
