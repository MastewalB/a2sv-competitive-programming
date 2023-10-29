from collections import defaultdict


def replaceWithPrevious(string, k):

    replaceDict = defaultdict(str)
    prev = 'a'
    replaceDict[prev] = prev
    for i in range(len(string)):
        c = string[i]
        if c not in replaceDict:
            if k > 0:
                diff = 0
                if ord(c) - ord(prev) <= k:
                    diff = ord(c) - ord(prev)
                    n_c = replaceDict[prev]
                else:
                    diff = k
                    n_c = chr(ord(c) - diff)
                k -= diff
                prev = c

                while diff > 0:
                    replaceDict[c] = n_c
                    c = chr(ord(c) - 1)
                    diff -= 1
                string[i] = n_c

        else:
            string[i] = replaceDict[c]

    print("".join(string))


t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    string = list(input())
    replaceWithPrevious(string, k)
