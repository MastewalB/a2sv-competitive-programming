def minSkips(n, bosses):
    dp = [[float("inf"), float("inf")] for _ in range(n + 1)]
    dp[0][1] = 0

    for i in range(n + 1):
        for fighter in range(2):
            for fight in range(1, min(n - i, 2) + 1):
                hard = bosses[i]

                hard += bosses[i + 1] if fight > 1 else 0

                if fighter:
                    dp[i + fight][1 -
                                  fighter] = min(dp[i + fight][1 - fighter], dp[i][fighter] + hard)
                else:
                    dp[i + fight][1 -
                                  fighter] = min(dp[i + fight][1 - fighter], dp[i][fighter])

    return min(dp[n][0], dp[n][1])

    return


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        bosses = list(map(int, input().split()))
        print(minSkips(n, bosses))


if __name__ == '__main__':
    main()
