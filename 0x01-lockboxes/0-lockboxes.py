#!/usr/bin/python3
""" method that determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """method that determines if all the boxes can be opened."""
    x = len(boxes)
    open_boxes = set([0])
    closed_boxes = set(boxes[0]).difference(set([0]))
    while len(closed_boxes) > 0:
        currIndex = closed_boxes.pop()
        if not currIndex or currIndex >= x or currIndex < 0:
            continue
        if currIndex not in open_boxes:
            closed_boxes = closed_boxes.union(boxes[currIndex])
            open_boxes.add(currIndex)
    return x == len(open_boxes)
