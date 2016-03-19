"""
Suppose we could access yesterday's stock prices as a list, where:

The indices are the time in minutes past trade opening time, which was 9:30am local time.
The values are the price in dollars of Apple stock at that time.
So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.

Write an efficient function that takes stock_prices_yesterday and returns the best profit I could have made from 1 purchase and 1 sale of 1 Apple stock yesterday.

For example:

    stock_prices_yesterday = [10, 7, 5, 8, 11, 9]

    get_max_profit(stock_prices_yesterday)
    # returns 6 (buying for $5 and selling for $11)

No "shorting"—you must buy before you sell. You may not buy and sell in the same time step (at least 1 minute must pass).
"""


def get_max_profit(prices):
    curr_buy = prices[0]
    curr_sell = prices[1]

    sidx = 2
    bidx = sidx - 1
    while sidx < len(prices):
        if curr_sell < prices[sidx]:
            curr_sell = prices[sidx]

        while bidx < sidx:
            if curr_buy > prices[bidx]:
                curr_buy = prices[bidx]
            bidx = bidx + 1
        sidx = sidx + 1
    return curr_sell - curr_buy


def get_max_profit_On(prices):
    if len(prices) < 2:
        raise IndexError('Getting profit requires at least 2 prices')

    min_price = prices[0]
    max_profit = prices[1] - prices[0]

    for index, price in enumerate(prices):
        if index == 0:
            continue

        potential_profit = price - min_price
        
        max_profit = max(max_profit, potential_profit)

        min_price = min(min_price, price)
    return max_profit


if __name__ == '__main__':
    stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
    assert get_max_profit(stock_prices_yesterday) == 6

    assert get_max_profit_On(stock_prices_yesterday) == 6

    print('[+] Tests passed')
