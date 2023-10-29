def number_of_big_segments(A, s):
    x = 0
    r = 0
    res = 0
    N = len(A)

    for L in range(N):

        while r < N and x < s:
            x += A[r]
            r += 1
        if x >= s:
            res += N - r + 1
        x -= A[L]

    return res


n, s = list(map(int, input().split()))
A = list(map(int, input().split()))
print(number_of_big_segments(A, s))
