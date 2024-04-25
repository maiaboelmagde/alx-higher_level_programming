#!/usr/bin/python3
'''
function that divides 2 integers and prints the result.
'''


def safe_print_division(a, b):
    try:
        returnValue = a/b
        return returnValue
    except ZeroDivisionError:
        returnValue = None
        return returnValue
    finally:
        print("Inside result: {}".format(returnValue))
