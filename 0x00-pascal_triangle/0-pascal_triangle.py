#!/usr/bin/python3

"""
This script implements the logic of Pascal's triangle.

I first initialize the triangle by starting with an empty
list, the first element of each row will be 1 and the last
element of each row is also 1. The index of the last element
is (n - 1).
"""


def pascal_triangle(n):
    """"
    n is the number of elements.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1]  # Starting each row with 1

        for j in range(1, i):
            # Calculating the next emplement based on the previous row
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        # End each row with 1
        if i > 0:
            row.append(1)
        triangle.append(row)

    return triangle
