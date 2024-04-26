#!/usr/bin/python3
from sys import stderr
'''function that executes a function safely.'''


def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as err:
        print("Exception: {}".format(err), file=stderr)
        result = None
    return result
