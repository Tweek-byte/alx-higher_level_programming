#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if 'a' <= c <= 'z':
            cap = chr(ord(c) - 32)
        else:
            cap = c
        print("{:s}".format(cap), end="")
    print("\n", end="")
