def is_valley(A):
    count = 0
    i = 1

    A = [float("inf")] + A + [float("inf")]
    while i < len(A):
        j = i
        while j < len(A) - 1 and A[j] == A[j + 1]:
            j += 1
        if A[i] < A[i - 1] and A[j] < A[j + 1]:
            count += 1

        i = j + 1
    return "YES" if count == 1 else "NO"


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(is_valley(a))
