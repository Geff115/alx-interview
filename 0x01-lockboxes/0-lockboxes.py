#!/usr/bin/python3
"""
This script implements a graph traversal for the
lockboxes, where each box is a node and each key
is an edge to another node.
"""

from collections import deque


def canUnlockAll(boxes):
    """
    ARGS:
        - boxes is a list of lists
        Each box is numbered sequentially from 0
        to n - 1.

    RETURN: boolean.
    """
    # Calculating the number of boxes since boxes is a list of lists
    number_of_boxes = len(boxes)

    # Initializing a set to keep track of unlocked boxes
    unlocked_boxes = set()
    # Initializing a queue to manage the boxes to check
    queue = deque()

    # Adding the first box (index 0) to the set of unlocked boxes
    unlocked_boxes.add(0)

    for key in boxes[0]:
        queue.append(key)  # Adding keys from the first box to the queue

    # Processing the queue to unlock boxes and add new keys
    while len(queue) > 0:
        popped_key = queue.popleft()

        if popped_key not in unlocked_boxes \
           and 0 <= popped_key < number_of_boxes:
            unlocked_boxes.add(popped_key)

            for new_key in boxes[popped_key]:
                # Edge case: Ensuring the key is within range of box indices
                if 0 <= new_key < number_of_boxes \
                   and new_key not in unlocked_boxes:
                    queue.append(new_key)

    if len(unlocked_boxes) == number_of_boxes:
        return True
    else:
        return False
