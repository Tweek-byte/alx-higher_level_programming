#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

    roman_dic = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    value = [roman_dic[x] for x in roman_string]
    res = 0

    for i in range(len(value)):
        res += value[i]
        if value[i - 1] < value[i] and i != 0:
            res -= (value[i - 1] + value[i - 1])

    return res
