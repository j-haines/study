"""
Write a function that, given:

    - an amount of money
    - a list of coin denominations

computes the number of ways to make amount of money with coins of the available
denominations.
"""

import functools


def coin(amount, denominations):
    ways_of_getting_n = [0] * (amount + 1)
    ways_of_getting_n[0] = 1

    for coin in denominations:
        for higher_amount in range(coin, amount + 1):
            remainder = higher_amount - coin
            ways_of_getting_n[higher_amount] += ways_of_getting_n[remainder]
    return ways_of_getting_n[amount]


if __name__ == '__main__':
    amount = 4
    denominations = [1, 2, 3]
    assert coin(amount, denominations) == 4
    print('[+] Test #1 passed')
