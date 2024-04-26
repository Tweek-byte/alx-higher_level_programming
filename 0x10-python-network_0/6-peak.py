#!/usr/bin/python3
"""Peak-Defining Algorithm method"""


def find_peak(list_of_integers):
    """Gets the peak"""
    if not list_of_integers:
        return None

    len1 = len(list_of_integers)
    n = len1 // 2
    ls = list_of_integers

    if n - 1 < 0 and n + 1 >= len1:
        return ls[n]
    elif n - 1 < 0:
        return ls[n] if ls[n] > ls[n + 1] else ls[n + 1]
    elif n + 1 >= len1:
        return ls[n] if ls[n] > ls[n - 1] else ls[n - 1]

    if ls[n - 1] < ls[n] > ls[n + 1]:
        return ls[n]

    if ls[n + 1] > ls[n - 1]:
        return find_peak(ls[n:])
    return find_peak(ls[:n])
