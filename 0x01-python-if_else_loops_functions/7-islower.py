#!/usr/bin/python3
def islower(c):
    for i in range(65, 90):
        if ord(c) == i:
            return False
    for j in range(ord("a"), ord("z")):
        if ord(c) == j:
            return True
