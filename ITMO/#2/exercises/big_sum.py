def big_sum(A, s):
    x = 0
    shortest = float("inf")
    L = 0

    for i in range(len(A)):
        x += A[i]
        while L <= i and x >= s:
            shortest = min(shortest, i - L + 1)
            x -= A[L]
            L += 1

    return shortest if shortest != float("inf") else -1


n, s = list(map(int, input().split()))
A = list(map(int, input().split()))
print(big_sum(A, s))
