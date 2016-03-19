"""
Write a function that, given:

    - an amount of money
    - a list of coin denominations

computes the number of ways to make amount of money with coins of the available
denominations.
"""

import functools


def memoize(func):
    cache = {}
    @functools.wraps(func)
    def wraps(*args):
        key = str((*args,))
        if key not in cache:
            cache[key] = func(*args)
        return cache[key]
    return wraps


@memoize
def coin(amount, denominations):
    if amount == 0: # Hit the amount spot on
        return 1
    elif amount < 0: # Overshot the amount
        return 0

    if len(denominations) == 0: # No denominations left to check
        return 0

    curr_coin = denominations[0]
    remaining_coins = denominations[1:]

    num_ways = 0
    while amount >= 0:
        num_ways += coin(amount, remaining_coins)
        amount -= curr_coin
    return num_ways


if __name__ == '__main__':
    amount = 4
    denominations = [1, 2, 3]
    assert coin(amount, denominations) == 4
    print('[+] Test #1 passed')
