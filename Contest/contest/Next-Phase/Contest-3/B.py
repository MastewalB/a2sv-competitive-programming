def minOps(a, n):
    i = 0
    while i < n and a[i] == 0:
        i += 1
    output = 0
    while i < n - 1:
        if a[i] == 0:
            output += 1
        output += a[i]
        i += 1

    return output


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(minOps(a, n))
