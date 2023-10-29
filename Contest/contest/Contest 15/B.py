import math


def team(a, b):
    return min(min(a, b), (a + b) // 4)


def is_valid(a, b, teams):
    return a + b >= 4 * teams


def teamBS(a, b):
    low, high = 0, min(a, b)
    best = 0
    while low <= high:
        mid = (low + high) >> 1
        if is_valid(a, b, mid):
            best = mid
            low = mid + 1
        else:
            high = mid - 1

    return best


t = int(input())
for _ in range(t):
    a, b = list(map(int, input().split()))
    print(teamBS(a, b))
