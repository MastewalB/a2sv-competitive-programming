
def num(n):
    if n < 10:
        return n
    digits = []
    _sum = 0

    i = 9
    while i > 0:
        if _sum + i <= n:
            _sum += i
            digits.append(str(i))
            if _sum == n:
                break
        i -= 1

    digits.reverse()

    return int(''.join(digits))


t = int(input())
for _ in range(t):
    n = int(input())
    print(num(n))
