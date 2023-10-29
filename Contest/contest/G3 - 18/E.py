from functools import lru_cache


def vacations(A):

    @lru_cache(None)
    def dp(i, prev):
        if i >= len(A):
            return 0

        if A[i] == prev or A[i] == 0:
            return dp(i + 1, 0) + 1

        if A[i] == 3:
            if prev == None or prev == 0:
                return min(dp(i + 1, 1), dp(i + 1, 2))
            if prev == 1:
                return dp(i + 1, 2)
            else:
                return dp(i + 1, 1)

        return dp(i + 1, A[i])

    return dp(0, None)


n = int(input())
a = list(map(int, input().split()))
print(vacations(a))
