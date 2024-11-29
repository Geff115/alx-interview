#!/usr/bin/python3
"""
Determining the fewest number of coins needed to
meet a given amount total.
"""

from collections import deque


def makeChange(coins, total):
    """
    ARGS:
        - coins: List of integers representing coin denominations
        - total: Target amount to achieve

    RETURN:
        - 0, if total is 0 or less
        - -1, if it's not possible to achieve the total
    """
    if total <= 0:
        return 0

    # Using Breadth-First Search algorithm (BFS)
    queue = deque([(total, 0)])
    visited = set()

    while queue:
        current, steps = queue.popleft()

        if current == 0:
            return steps

        for coin in coins:
            next_amount = current - coin
            if next_amount >= 0 and next_amount not in visited:
                visited.add(next_amount)
                queue.append((next_amount, steps + 1))

    return -1
