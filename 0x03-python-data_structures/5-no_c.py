#!/usr/bin/python3
def no_c(my_string):
    for s in my_string:
        if s != "C" and s != "c":
            print("{:s}".format(s), end="")
