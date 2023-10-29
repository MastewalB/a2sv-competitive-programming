def atm(queue, s, N):
    start, end = 0, -1

    total = s
    begin = 0
    for i in range(N):
        total += queue[i]
        while total < 0:
            total -= queue[begin]
            begin += 1

        if i - begin > end - start:
            start, end = begin, i

    return (start + 1, end + 1) if end >= 0 else -1


t = int(input())
for _ in range(t):
    n, s = list(map(int, input().split()))
    queue = list(map(int, input().split()))
    res = atm(queue, s, n)
    print(res) if res == -1 else print(*res)
