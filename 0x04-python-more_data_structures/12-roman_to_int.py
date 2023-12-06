def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    r_dic = {"I": 1, "V": 5, "X": 10,
             "L": 50, "C": 100, "D": 500, "M": 1000}

    res = 0
    prev_v = 0

    for char in reversed(roman_string):
        val = r_dic.get(char, 0)

        if val < prev_v:
            res -= val
        else:
            res += val

        prev_v = val

    return res
