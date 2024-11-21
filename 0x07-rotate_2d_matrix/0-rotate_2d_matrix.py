#!/usr/bin/python3
"""
Rotating a 2D Matrix 90 degrees clockwise by
transforming rows into columns
"""


def rotate_2d_matrix(matrix):
    """Rotating function

    ARGS:
        matrix - A 2D matrix
    """
    matrix_length = len(matrix)

    # Transpose the matrix
    for i in range(matrix_length):
        for j in range(i, matrix_length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(matrix_length):
        matrix[i].reverse()
