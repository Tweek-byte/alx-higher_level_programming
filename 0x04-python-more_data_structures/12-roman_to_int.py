def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    r_dic = {"I": 1, "V": 5, "X": 10,
             "L": 50, "C": 100, "D": 500, "M": 1000}

    result = prev_v = 0

    for char in reversed(roman_string):
        v = r_dic.get(char, 0)
        result -= v if v < prev_v else -v
        prev_v = v

    return result
