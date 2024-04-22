#!/usr/bin/python3

''' function that prints a matrix of integers.'''


def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        leng = len(i)
        for j in i:
            print("{:d}".format(j), end=' ' if j != i[-1] else '')
        print()
