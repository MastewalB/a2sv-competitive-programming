def number_of_small_segments(A, s):
    res = 0
    x = 0
    L = 0

    for i in range(len(A)):
        x += A[i]
        while x > s:
            x -= A[L]
            L += 1

        res += i - L + 1
    return res


n, s = list(map(int, input().split()))
A = list(map(int, input().split()))
print(number_of_small_segments(A, s))
