#!/usr/bin/python3

import sys
from typing import List, Tuple


def nqueens(n: int) -> List[List[Tuple[int, int]]]:
    """function that returns placement of the queen in a n *n
    board. the queens should not attack each other or
    shouldnt be on same row same colomn or
    share the positive  r + c or negative diagonal r - c
    """
    column = set()
    pos_diag = set()
    neg_diag = set()

    results = []

    def backtrack(row, curr):
        """line search algorithim that will help
        in positioning the queen"""
        if row == n:
            results.append(curr[:])
            return
        for col in range(n):
            if col in column or (row+col) in pos_diag or (row-col) in neg_diag:
                continue
            column.add(col)
            pos_diag.add(row + col)
            neg_diag.add(row - col)
            curr.append([row, col])

            backtrack(row + 1, curr)

            column.remove(col)
            pos_diag.remove(row + col)
            neg_diag.remove(row - col)
            curr.pop()
    backtrack(0, [])
    return results


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = nqueens(N)

    for solution in solutions:
        print(solution)
