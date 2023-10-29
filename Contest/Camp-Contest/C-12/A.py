def maxOr(A, B):
    _maxOr = float("-inf")
    if len(A) == 1:
        return A[0] + B[0]
    for i in range(len(A)):
        curr_a = A[i]
        curr_b = B[i]
        for j in range(i + 1, len(A)):
            curr_a |= A[j]
            curr_b |= B[j]
            _maxOr = max(_maxOr, curr_a + curr_b)
    return _maxOr


n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


print(maxOr(A, B))
