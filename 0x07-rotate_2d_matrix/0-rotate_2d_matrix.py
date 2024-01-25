#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """rotate a n * n matrix rows become columns
    Do not return anything  modify in place"""

    left, right = 0, len(matrix) - 1
    while left < right:
        for i in range(right - left):
            # pointers
            top, bottom = left, right

            # save the topleft element in temp variable
            topleft = matrix[top][left + i]

            # move botom left element to top left
            matrix[top][left + i] = matrix[bottom - i][left]

            # move bottom right element to bottom left
            matrix[bottom - i][left] = matrix[bottom][right - i]

            # move top right element to bottop right position [n,n]
            matrix[bottom][right - i] = matrix[top + i][right]

            # move the saved topleft element in top right position
            matrix[top + i][right] = topleft

        left += 1
        right -= 1
