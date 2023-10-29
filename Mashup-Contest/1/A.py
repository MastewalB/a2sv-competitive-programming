def changetoMin(hr, m):
    return (hr * 60) + m


def changetoHr(m):
    return f"{(m // 60) % 24} {(m % 60)}"


t = int(input())
for _ in range(t):
    n, h, m = list(map(int, input().split()))
    sleeping_time = changetoMin(h, m)
    minimum, maximum = float("inf"), float("inf")
    for _ in range(n):
        hr, m = list(map(int, input().split()))
        time = changetoMin(hr, m)
        if time >= sleeping_time:
            minimum = min(minimum, time)
        elif time < sleeping_time:
            maximum = min(maximum, time)

    if minimum < float("inf"):
        print(changetoHr((minimum - sleeping_time)))
    elif maximum < float("inf"):
        print(changetoHr((1440 - sleeping_time) + maximum))
