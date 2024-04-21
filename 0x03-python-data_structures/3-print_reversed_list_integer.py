#!/usr/bin/python3

'''
function that prints all integers of a list, in reverse order.
'''


def print_reversed_list_integer(my_list=[]):
    idx = len(my_list)
    while idx > 0:
        print("{:d}".format(my_list[idx-1]))
        idx -= 1
