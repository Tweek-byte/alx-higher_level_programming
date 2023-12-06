#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    d_keys = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            d_keys.append(key)
    for key in d_keys:
        del a_dictionary[key]
    return a_dictionary
