from collections import Counter, defaultdict


def minWindow(s):
    requiredDict = Counter(["1", "2", "3"])
    requiredLen = len(requiredDict)

    left = 0
    window = defaultdict(int)
    formed = 0
    output = float("inf")
    begin, end = None, None

    for right in range(len(s)):
        c = s[right]
        window[c] += 1

        if c in requiredDict and window[c] == 1:
            formed += 1

        while left <= right and formed >= requiredLen:
            if right - left + 1 < output:
                output = right - left + 1
                begin = left
                end = right
            window[s[left]] -= 1
            if s[left] in requiredDict and window[s[left]] < 1:
                formed -= 1

            left += 1
    return output if output < float("inf") else 0


t = int(input())
for _ in range(t):
    s = input()
    print(minWindow(s))
