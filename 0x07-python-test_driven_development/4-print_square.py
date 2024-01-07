#!/usr/bin/python3
"""
This is the "4-print_square" module.
The 4-print_square module supplies one function, print_square.
"""


def print_square(size):
    """
    Prints a square with '#'s that has a side length of size.

    Args:
        size (int): The side length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size > 0:
        square = ("#" * size + "\n") * size
        print(square, end="")
    else:
        print()
