from collections import defaultdict


def small_set(A, k):
    if k == 0:
        return 0
    S = defaultdict(int)
    curr = 0
    L = 0
    res = 0

    for i in range(len(A)):
        S[A[i]] += 1
        if S[A[i]] == 1:
            curr += 1
        while L < i and curr > k:
            S[A[L]] -= 1
            if S[A[L]] == 0:
                curr -= 1
            L += 1
        res += i - L + 1
    return res


n, k = list(map(int, input().split()))
A = list(map(int, input().split()))
print(small_set(A, k))
