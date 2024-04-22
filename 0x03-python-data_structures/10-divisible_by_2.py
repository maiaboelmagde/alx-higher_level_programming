#!/usr/bin/python3

'''
function that finds all multiples of 2 in a list.
'''


def divisible_by_2(my_list=[]):
    result = my_list[:]
    idx = 0
    for i in my_list:
        if i % 2 == 0:
            result[idx] = 1
        else:
            result[idx] = 0
        idx += 1
    return result
