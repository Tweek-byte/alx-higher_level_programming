#!/usr/bin/python3
"""
This is the "5-test_indentation" module.
The 5-text_indentation module supplies one function, text_indentation.
"""


def text_indentation(text):
    """
    Splits a text into lines along '?', ':', and '.' followed by two new lines.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    flag = 0
    for char in text:
        if flag == 0:
            if char == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if char in ['?', '.', ':']:
                print(char)
                print()
                flag = 0
            else:
                print(char, end="")

    if flag == 1:
        print()
