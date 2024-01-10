#!/usr/bin/python3
"""
Contains the append_write function
"""


def append_write(filename="", text=""):
    """Appends the given text to a file (UTF8)"""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
