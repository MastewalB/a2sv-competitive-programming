def equal(A, B):
    i = j = 0
    N, M = len(A), len(B)
    last, total = 0, 0
    for i in range(M):
        count = 0
        while j < N and A[j] <= B[i]:
            if A[j] == B[i]:
                count += 1
            j += 1
        if i > 0 and B[i] == B[i - 1]:
            count = last
        last = count
        total += count

    return total


n, m = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(equal(A, B))
