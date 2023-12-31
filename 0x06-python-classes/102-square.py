#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square.

    Attributes:
        size (int): The size of the square.
    """

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size to set.
        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def __eq__(self, other):
        """Define the == comparison to a Square.

        Args:
            other (Square): The square to compare with.
        Returns:
            bool: True if areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison to a Square.

        Args:
            other (Square): The square to compare with.
        Returns:
            bool: True if areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison to a Square.

        Args:
            other (Square): The square to compare with.
        Returns:
            bool: True if the area is less, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to a Square.

        Args:
            other (Square): The square to compare with.
        Returns:
            bool: True if the area is less or equal, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to a Square.

        Args:
            other (Square): The square to compare with.
        Returns:
            bool: True if the area is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= comparison to a Square.

        Args:
            other (Square): The square to compare with.
        Returns:
            bool: True if the area is greater or equal, False otherwise.
        """
        return self.area() >= other.area()
