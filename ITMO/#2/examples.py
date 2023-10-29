# segment with good sum

def good_sum(A, s):
    # returns longest subarray with sum less than or equal to s

    N = len(A)
    L = 0
    S = 0
    longest = 0
    for i in range(N):
        S += A[i]
        while L <= i and S > s:
            S -= A[L]
            L += 1
        longest = max(longest, i - L + 1)
    return longest


def less_sum(A, s):
    N = len(A)
    L = 0
    S = 0
    smallest = float("inf")
    for i in range(N):
        S += A[i]
        while L <= i and S > s:
            smallest = min(smallest, i - L + 1)
            S -= A[L]
            L += 1

    if smallest == float("inf"):
        return -1
    return smallest


def number_of_segments(A, s):
    x = 0
    N = len(A)
    L = 0
    res = 0
    for i in range(N):
        x += A[i]
        while x > s:
            x -= A[L]
            L += 1
        res += i - L + 1

    return res


A = [1, 0, 10]
s = 10
print(number_of_segments(A, s))
