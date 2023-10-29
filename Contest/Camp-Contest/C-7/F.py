

def can(m, s):
    return 0 <= s <= 9 * m


def maxDigit(m, s):
    res = []

    for i in range(m):
        for d in range(9, -1, -1):
            if (i > 0 or d > 0 or (m == 1 and d == 0)) and can(m - i - 1, s - d):
                res.append(str(d))
                s -= d
                break
    if len(res) != m:
        return -1
    return ''.join(res)


def minDigit(m, s):
    res = []

    for i in range(m):
        for d in range(10):
            if (i > 0 or d > 0 or (m == 1 and d == 0)) and can(m - i - 1, s - d):
                res.append(str(d))
                s -= d
                break
    if len(res) != m:
        return -1
    return ''.join(res)


def givenLengthAndSum(m, s):
    return [minDigit(m, s), maxDigit(m, s)]


def main():
    m, s = list(map(int, input().split()))
    print(*givenLengthAndSum(m, s))


main()
