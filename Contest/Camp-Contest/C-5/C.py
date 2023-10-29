from collections import defaultdict


def minWindow(flat):
    pokemons = set(flat)
    N = len(pokemons)
    _maxLen = float("inf")

    window, j = defaultdict(int), 0
    found = 0
    for i in range(len(flat)):
        p = flat[i]
        window[p] += 1
        if window[p] == 1:
            found += 1

        while j <= i and found == N:
            _maxLen = min(_maxLen, i - j + 1)
            window[flat[j]] -= 1
            if window[flat[j]] == 0:
                found -= 1
            j += 1
    return _maxLen


n = int(input())
flats = input()
print(minWindow(flats))
