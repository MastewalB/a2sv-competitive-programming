def cheap(word, p):
    prices = []

    total = 0
    for i in range(len(word)):
        prices.append((word[i], i, ord(word[i]) - 96))
        total += prices[-1][2]

    prices.sort(key=lambda x: x[2])

    while total > p:
        total -= prices.pop()[2]

    prices.sort(key=lambda x: x[1])
    res = []
    for a, b, c in prices:
        res += a
    return ''.join(res)


t = int(input())

for _ in range(t):
    w = input()
    p = int(input())
    print(cheap(w, p))
