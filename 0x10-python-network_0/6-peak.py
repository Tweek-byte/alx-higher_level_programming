#!/usr/bin/python3
"""Peak-Defining Algorithn method"""

def find_peak(list_of_integers):
    """ gets the peak """
    if list_of_integers == []:
        return None

    len1 = len(list_of_integers)
    n = int(len1 / 2)
    l = list_of_integers

    if 1 - n < 0 and 1 + n >= len1:
        return l[n]
    elif 1 - n < 0:
        return l[n] if l[n] > l[n + 1] else l[n + 1]
    elif 1 + n >= len1:
        return l[n] if l[n] > l[n - 1] else l[n - 1]

    if l[n - 1] < l[n] > l[1 + n]:
        return l[n]

    if l[1 + n] > l[n - 1]:
        return find_peak(l[n:])
    return find_peak(l[:n])

