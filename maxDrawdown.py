# Given a series of oscillating price data within a time interval as example
import matplotlib
prs = [1, 2, 3, 4, 5, 19, 16, 14, 22, 10, 8, 4, 5, 9, 12, 7, 4, 1]

def maxDrawdown(prices: list) -> int:
    peak = -1 # assuming the lowest possilbe price of a stock is 0
    dd = 0    # drawdown
    mdd = 0   # maximum drawdown
    for i in range(len(prs)):
        if prs[i] > peak:
            peak = prs[i]
        dd = peak - prs[i]
        if dd > mdd:
            mdd = dd
    return mdd


res = maxDrawdown(prs)
print(res)

matplotlib.s

