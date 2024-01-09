#!/usr/bin/python3
"""
Contains the read_file function
"""


def read_file(filename=""):
    """This function reads a text file (UTF8) and prints it to stdout:"""

    with open(filename, "r", encoding="utf-8") as FD:
        print(FD.read(), end="")
