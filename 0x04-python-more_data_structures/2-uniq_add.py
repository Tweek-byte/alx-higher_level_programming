#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    if my_list is None:
        my_list = []
    for i in set(my_list):
        res += i
    return res
