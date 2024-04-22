#!/usr/bin/python3

'''function that finds the biggest integer of a list'''


def max_integer(my_list=[]):
    max = 0
    for i in my_list:
        if i > max:
            max = i
    return max
