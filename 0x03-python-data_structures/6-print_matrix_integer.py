#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for value in matrix:
        for integer in value:
            print("{:d}".format(integer), end=" ")
        print()
