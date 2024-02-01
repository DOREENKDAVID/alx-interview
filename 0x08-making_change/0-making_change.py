#!/usr/bin/python3
"""Given a pile of coins of different values,
determine the fewest number of coins needed
to meet a given amount total."""


def makeChange(coins, total):
    """Given a pile of coins of different values,
    determine the fewest number of coins needed
    to meet a given amount total."""
    if total <= 0:
        return 0
    total_coins = [float('inf')] * (total + 1)

    total_coins[0] = 0

    for coin in coins:
        for amount in range(coin, (total + 1)):
            total_coins[amount] = min(total_coins[amount],
                                      total_coins[amount - coin] + 1)
    return total_coins[total] if total_coins[total] != float('inf') else -1
