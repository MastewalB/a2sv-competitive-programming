def gcd(a, b):
    while y:
        x, y = y, x % y
    return x


def cGcd(l, r):
    if l == r:
        return l
    return 1


l, r = list(map(int, input().split()))
print(cGcd(l, r))
