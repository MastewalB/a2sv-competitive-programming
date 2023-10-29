import math


def min_op(n):
    A = []
    for _ in range(n):
        A.extend(["B", "A", "N"])
    ops = []
    start = (n * 3) // 2
    if n % 2 == 0:
        start += 3
    else:
        start += 3 - (start % 3)

    j = 2
    print(math.ceil(((n * 3) + 1 - start) / 3))
    for i in range(start, (n * 3) + 1, 3):
        print(j, i)
        j += 3
    return


t = int(input())
for _ in range(t):
    n = int(input())
    min_op(n)
