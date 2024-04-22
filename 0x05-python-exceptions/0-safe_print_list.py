#!/bin/usr/python3
''' function that prints x elements of a list.'''


def safe_print_list(my_list=[], x=0):
    idx = 0
    while x > idx:
        try:
            print(f"{my_list[idx]}", end='')
            idx += 1
        except Exception:
            break
    print()
    return idx
