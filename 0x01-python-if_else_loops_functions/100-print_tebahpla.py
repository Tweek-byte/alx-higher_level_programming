#!/usr/bin/python3
for _ in range(26):
    if _ % 2 == 0:
        print("{:c}".format(122 - _), end="")
    else:
        print("{:c}".format(90 - _), end="")
