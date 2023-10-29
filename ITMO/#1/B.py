def smaller(A, B):
    i = j = 0
    N, M = len(A), len(B)
    C = []
    for i in range(M):
        while j < N and A[j] < B[i]:
            j += 1
        C.append(j)
    return C


n, m = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(*smaller(A, B))
