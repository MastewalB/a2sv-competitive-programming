from functools import lru_cache


def maxCoins(n, k, b, c):
    _max = 1001
    a = [float("inf")] * (_max + 1)
    a[1] = 0

    for i in range(1, _max):
        for j in range(1, i + 1):
            R = i + (i // j)
            if R < _max:
                a[R] = min(a[R], a[i] + 1)

    _sum = 0
    for num in b:
        _sum += a[num]
    k = min(k, _sum)

    A = []
    for i in range(n):
        A.append(a[b[i]])

    @lru_cache(None)
    def dp(index, k):
        nonlocal n
        if index >= n or k == 0:
            return 0

        P = (c[index] + dp(index + 1, k - A[index])) if A[index] <= k else 0
        NP = dp(index + 1, k)

        return max(P, NP)

    return dp(0, k)


def main():
    t = int(input())
    for _ in range(t):
        n, k = list(map(int, input().split()))
        b = list(map(int, input().split()))
        c = list(map(int, input().split()))
        print(maxCoins(n, k, b, c))


main()

# 9
# 2 7
# 4 23
# 100 39
# 13 13
# 71 7 47 16 56 70 57 87 56 12 46 39 24
# 43 83 51 27 100 35 58 63 56 87 71 54 56
# 4 3
# 65 83 54 25
# 96 47 2 28
# 1 6
# 72
# 74
# 7 12
# 11 57 71 26 31 99 58
# 62 66 82 31 94 18 74
# 3 16
# 62 85 15
# 35 23 35
# 5 19
# 89 57 9 80 13
# 72 25 54 95 91
# 22 91
# 52 45 12 86 97 52 35 54 86 86 42 11 67 5 100 72 37 50 38 57 6 63
# 39 7 8 28 94 52 98 72 6 29 45 25 5 14 16 83 86 53 61 65 97 8
# 6 16
# 66 83 11 45 81 48
# 2 49 78 19 29 54
# 2 6
# 86 67
# 52 100
# 13 46
