#!/usr/bin/python3
"""
Determining the fewest number of coins needed to
meet a given amount total.
"""


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

    # Creating a dp table
    dp = [float('inf')] * (total + 1)
    # Base case coin
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
