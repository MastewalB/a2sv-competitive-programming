
def max_inversions(A):
    N = len(A)
    O = [0] * N
    Z = [0] * N
    ans, f_z, l_o = 0, None, None
    for i in range(N - 1, -1, -1):
        if i < N - 1:
            Z[i] += Z[i + 1]
        if A[i] == 0:
            Z[i] += 1
        else:
            if l_o == None:
                l_o = i
    for i in range(N):
        if i > 0:
            O[i] += O[i - 1]

        if A[i] == 1:
            O[i] += 1
        else:
            if f_z == None:
                f_z = i
            ans += O[i]

    a = b = 0
    if f_z != None:
        a = ans - O[f_z] + Z[f_z] - 1
    if l_o != None:
        b = ans - Z[l_o] + O[l_o] - 1
    return max(ans, a, b)


t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split()))
    print(max_inversions(array))
