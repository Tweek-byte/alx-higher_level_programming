#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list and len(my_list):
        val = 0
        z = 0
        for i in my_list:
            val += (i[0] * i[1])
            z += i[1]
        return (val / z)
    return 0
