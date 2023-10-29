def merge(A, B):
    i = j = 0
    N, M = len(A), len(B)
    C = []

    while len(C) < N + M:
        if j == M or (i < N and A[i] < B[j]):
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    return C


n, m = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(*merge(A, B))
