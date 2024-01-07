#!/usr/bin/python3
"""
A class called 0-add_integer and returns the addition of two numbers
"""


def add_integer(a, b=98):
    """Returns the addition of two numbers"""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    a = int(a)
    b = int(b)

    return a + b
