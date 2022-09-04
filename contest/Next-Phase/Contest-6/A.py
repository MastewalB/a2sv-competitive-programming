from collections import deque


def minCoins(n):

    coins = [100, 20, 10, 5, 1]
    output = 0
    while n > 0:
        for c in coins:
            if n >= c:
                output += n // c
                n %= c
    return output


n = int(input())
print(minCoins(n))
