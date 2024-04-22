#!/bin/usr/python3
''' function that prints x elements of a list.'''


def safe_print_list(my_list=[], x=0):
    idx = 0
    try:
        while x > idx:
            print(my_list[idx], end='')
            idx += 1
        print()
        return idx
    except Exception:
        print()
        return idx
