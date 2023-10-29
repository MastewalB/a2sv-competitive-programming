from collections import defaultdict


def split(dominoes):
    dom = defaultdict(set)
    for a, b in dominoes:
        if a == b:
            return "NO"
        dom[a].add(b)
        dom[b].add(a)
    set1 = set()
    set2 = set()

    for a, b in dominoes:
        set1.add(a)
        set1.add(b)
        dom[a].remove(b)
        dom[b].remove(a)

        if dom[a][0] in set2 or dom[b][0] in set2:
            return "NO"
        set2.add(dom[a][0])
        set2.add(dom[b][0])
    return "Yes"


t = int(input())

for _ in range(t):
    dominoes = []
    n = int(input())
    for _ in range(n):
        dominoes.append(list(map(int, input().split())))
    print(split(dominoes))
