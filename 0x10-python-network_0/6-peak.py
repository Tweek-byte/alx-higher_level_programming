#!/usr/bin/python3
"""Peak-Defining Algorithm method"""

def find_peak(list_of_integers):
    """Gets the peak"""
    if not list_of_integers:
        return None

    len1 = len(list_of_integers)
    n = len1 // 2
    l = list_of_integers

    if n - 1 < 0 and n + 1 >= len1:
        return l[n]
    elif n - 1 < 0:
        return l[n] if l[n] > l[n + 1] else l[n + 1]
    elif n + 1 >= len1:
        return l[n] if l[n] > l[n - 1] else l[n - 1]

    if l[n - 1] < l[n] > l[n + 1]:
        return l[n]

    if l[n + 1] > l[n - 1]:
        return find_peak(l[n:])
    return find_peak(l[:n])
