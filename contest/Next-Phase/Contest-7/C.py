from collections import defaultdict


def balanced(s):
    numSet = defaultdict(int)
    numSet[0] = -1
    total = 0
    longest = 0
    for i in range(len(s)):
        if s[i] == "1":
            total += 1
        else:
            total -= 1
        if total in numSet:
            longest = max(longest, i - numSet[total])
        else:
            numSet[total] = i
    return longest


n = int(input())
s = input()
print(balanced(s))
