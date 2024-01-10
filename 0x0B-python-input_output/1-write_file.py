#!/usr/bin/python3
"""
Contains the write_file function
"""

def write_file(filename="", text=""):
    """Writes the given text to a file (UTF8) and returns the number of characters written."""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
