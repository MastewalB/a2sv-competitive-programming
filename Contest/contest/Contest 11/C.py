import math


def bacteria(n):
    h = math.log2(n)
    if math.floor(h) == math.ceil(h):
        print(1)
        return

    print(1 + n - pow(2, math.floor(h)))


t = int(input())
bacteria(t)
