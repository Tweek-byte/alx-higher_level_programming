#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    for i in range(length - 1, -1, -1):
        tbi = my_list[i]
        print("{:d}".format(tbi))
