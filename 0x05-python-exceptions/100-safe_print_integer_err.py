#!/usr/bin/python3
from sys import stderr
'''function that prints an integer.'''


def safe_print_integer_err(value):
    try:
        print('{:d}'.format(value))
        return True
    except Exception as err:
        print('Exception: {}'.format(err), file=stderr)
        return False
