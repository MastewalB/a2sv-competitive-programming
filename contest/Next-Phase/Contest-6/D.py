from collections import Counter
from functools import lru_cache
import sys

sys.setrecursionlimit(10000)


def boredom(array):
    count = Counter(array)
    _max = max(array)
    dp = [0] * (_max + 1)

    dp[_max] = count[_max] * _max
    for i in range(_max - 1, 0, -1):
        if i < _max - 1:
            dp[i] = max((count[i] * i) + dp[i + 2], dp[i + 1])
        else:
            dp[i] = max((count[i] * i), dp[i + 1])

    return dp[1]


n = int(input())
array = list(map(int, input().split()))
print(boredom(array))
