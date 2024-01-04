#!/usr/bin/python3
"""unicode transformation format"""


from typing import List


def validUTF8(data: List[int]) -> bool:
    """takes a list of integers (representing bytes) and
    checks if they form a valid UTF-8 sequence."""

    def check(num):
        """function determines the number of leading bits in a byte
        (interpreted as an integer) that indicate
        the start of a character in a UTF-8 sequence."""

        mask = 1 << (8 - 1)
        i = 0

        while num & mask:
            mask >>= 1
            i += 1
        return i
    i = 0
    while i < len(data):
        j = check(data[i])
        k = i + j - (j != 0)
        i += 1
        if j == 1 or j > 4 or k >= len(data):
            return False
        while i < len(data) and i <= k:
            current = check(data[i])
            if current != 1:
                return False
            i += 1
    return True
