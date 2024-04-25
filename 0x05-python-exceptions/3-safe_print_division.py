#!/usr/bin/python3
'''
function that divides 2 integers and prints the result.
'''


def safe_print_division(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return None
