def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    r_dictionary = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    di = [r_dictionary[c] for c in roman_string]
    res = 0
    for key, value in enumerate(di):
        res += value
        if key != 0 and di[key - 1] < value:
            res -= (di[key - 1] + di[key - 1])
    return res
