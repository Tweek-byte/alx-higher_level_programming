#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    k = a_dictionary.get
    return max(a_dictionary, k)
