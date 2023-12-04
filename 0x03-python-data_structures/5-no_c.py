#!/usr/bin/python3
def no_c(my_string):
    output = ""
    for s in my_string:
        if s != "C" and s != "c":
            output += s
    return output
