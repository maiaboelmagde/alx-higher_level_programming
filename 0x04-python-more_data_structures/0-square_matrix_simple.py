#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    indx1 = 0
    new_matrix = []
    for i in matrix:
        new_matrix.append([])
        for j in i:
            new_matrix[indx1].append(j*j)
        indx1 += 1
    return new_matrix
