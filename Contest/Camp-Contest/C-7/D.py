from collections import defaultdict


def changeString(s, k):
    max_freq = i = 0
    window_freq = defaultdict(int)

    for j in range(len(s)):
        c = s[j]
        window_freq[c] += 1
        max_freq = max(max_freq, window_freq[c])

        if j - i + 1 > max_freq + k:
            window_freq[s[i]] -= 1
            i += 1

    return len(s) - i


def main():
    n, k = list(map(int, input().split()))
    s = input()
    print(changeString(s, k))


main()
