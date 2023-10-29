from collections import Counter


def equalize(n, array):
    count = Counter(array)
    freq = sorted(count.values(), reverse=True)
    output = 0
    for i in range(len(freq)):
        output = max(output, freq[i] * (i + 1))
    return n - output


t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int, input().split(" ")))
    print(equalize(n, array))
