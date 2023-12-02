#!/usr/bin/python3
"""pascals triangle module"""


def pascal_triangle(n):
    """that returns a list of lists of integers
    representing the Pascal’s triangle  of n"""

    if n <= 0:
        return []
    else:
        triangle = []
        for row in range(n):
            rowlist = []
            for column in range(row + 1):
                if column == 0 or column == row:
                    rowlist.append(1)
                else:
                    value = (triangle[row - 1][column - 1] +
                             triangle[row - 1][column])
                    rowlist.append(value)
            triangle.append(rowlist)
        return triangle
    for row in triangle:
        print(' '.join(str(item) for item in row))
