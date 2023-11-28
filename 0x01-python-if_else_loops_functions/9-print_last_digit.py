#!/usr/bin/python3
def print_last_digit(number):
    if number > 10:
        dig = number % 10
    elif number < 10:
        dig = abs(number) % 10
    else:
        dig = 0
    print("{:d}".format(dig), end="")
    return dig
