#!/usr/bin/python3
"""Peak-Defining Algorithm method"""


def find_peak(list_of_integers):
    """Gets the peak"""
    if not list_of_integers:
        return None

    len1 = len(list_of_integers)
    n = len1 // 2

    if n - 1 < 0 and n + 1 >= len1:
        return list_of_integers[n]
    elif n - 1 < 0:
        return list_of_integers[n]
    if list_of_integers[n] > list_of_integers[n + 1]
    else list_of_integers[n + 1]
    elif n + 1 >= len1:
        return list_of_integers[n]
    if list_of_integers[n] > list_of_integers[n - 1]
    else list_of_integers[n - 1]

    if list_of_integers[n - 1] < list_of_integers[n] > list_of_integers[n + 1]:
        return list_of_integers[n]

    if list_of_integers[n + 1] > list_of_integers[n - 1]:
        return find_peak(list_of_integers[n:])
    return find_peak(list_of_integers[:n])
