#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if sentence == "":
        return (length, None)
    else:
        char = sentence[0]
    return (length, char)
