#!/usr/bin/python3
""" Island Perimeter"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid:

    grid is a list of list of integers:
    0 represents water
    1 represents land
    Each cell is square, with a side length of 1
    Cells are connected horizontally/vertically (not diagonally).
    grid is rectangular, with its width and height not exceeding 100
    The grid is completely surrounded by water
    There is only one island (or nothing).
    The island doesn’t have “lakes” (water inside that
    isn’t connected to the water surrounding the island).
    """
    visit = set()

    def depth_first_search(i, j):
        # Base cases to handle boundary conditions and water cells
        if i >= len(grid) or j >= len(grid[0]):
            return 1
        elif i < 0 or j < 0 or grid[i][j] == 0:
            return 1

        # Check if cell has already been visited
        elif (i, j) in visit:
            return 0

        visit.add((i, j))

        # move right
        perim = depth_first_search(i, j + 1)
        # move up add to perim 1
        perim += depth_first_search(i + 1, j)
        # move left add to perim 1
        perim += depth_first_search(i, j - 1)
        # move down add 1
        perim += depth_first_search(i - 1, j)
        return perim

    # Iterate through the grid to find the first land cell
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                return depth_first_search(i, j)
