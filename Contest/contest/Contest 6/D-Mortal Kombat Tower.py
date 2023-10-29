import sys
from functools import lru_cache


def minSkips(n, bosses):

    dp = [[float("inf"), float("inf")] for _ in range(n + 1)]
    dp[0][1] = 0  # before the start of the game

    for i in range(n + 1):
        for who in range(2):  # 0 for us 1 for friend
            for fight in range(1, min(n - i, 2) + 1):
                hard = bosses[i]
                if fight > 1:
                    hard += bosses[i + 1]
                if who == 1:
                    dp[i + fight][1 -
                                  who] = min(dp[i + fight][1 - who], dp[i][who] + hard)
                else:
                    dp[i + fight][1 -
                                  who] = min(dp[i + fight][1 - who], dp[i][who])

    return min(dp[n][0], dp[n][1])


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        bosses = list(map(int, input().split()))
        print(minSkips(n, bosses))


if __name__ == '__main__':
    main()
