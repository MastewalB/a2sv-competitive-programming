def digits(n):
    d = []
    while n > 0:
        d.append(n % 10)
        n //= 10
    d.reverse()
    return d


def toInt(lst):
    n = 0
    for i in range(len(lst)):
        n += pow(10, i) * lst[i]
    return n


def increase_by_one(N):
    d = digits(N)
    d.reverse()
    i = 0
    while i < len(d) and d[i] == 0:
        i += 1
    carry = 1
    d[i] = 0
    i += 1
    while True:
        if i >= len(d):
            d.append(1)
            break
        d[i] += carry
        if d[i] > 9:
            d[i] = d[i] % 10
            carry = 1
        else:
            break
        i += 1

    return (sum(d), toInt(d))


def min_move(n, s):
    if n <= s:
        return 0
    original = n
    currSum = sum(digits(n))

    while currSum > s:
        currSum, n = increase_by_one(n)

    return n - original


t = int(input())
for _ in range(t):
    n, s = list(map(int, input().split()))
    print(min_move(n, s))
