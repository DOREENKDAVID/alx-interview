#!/usr/bin/python3


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
    if total_coins[total] != float('inf'):
        return total_coins[total]
    else:
        return -1
