def even_odd(A, queries):
    even = 0
    odd = 0
    _sum = 0
    for n in A:
        even += int((n % 2) == 0)
        odd += int((n % 2) != 0)
        _sum += n

    for op, val in queries:
        _sum += even * val if op == 0 else odd * val
        if op == 0:
            if val % 2 != 0:
                odd += even
                even = 0
        elif op == 1:
            if val % 2 != 0:
                even += odd
                odd = 0
        print(_sum)

    return


t = int(input())
for _ in range(t):
    n, q = list(map(int, input().split()))
    A = list(map(int, input().split()))
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().split())))
    even_odd(A, queries)
