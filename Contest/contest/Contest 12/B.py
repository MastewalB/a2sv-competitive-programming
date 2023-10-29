import math


def findK(n):
    p = int(math.log2(n))
    return pow(2, p) - 1


t = int(input())
for _ in range(t):
    n = int(input())
    print(findK(n))
