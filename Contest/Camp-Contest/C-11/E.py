from collections import defaultdict
n = int(input())
v = input()
t = input()

parent = [i for i in range(26)]
rank = [1 for _ in range(26)]


def find(a):
    while parent[a] != a:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return parent[a]


def union(a, b):
    a, b = find(a), find(b)
    a, b = sorted([a, b], key=lambda x: rank[x])
    parent[a] = b
    rank[b] += rank[a]


answer = []
for i in range(len(v)):
    a, b = ord(v[i]) - ord('a'), ord(t[i]) - ord('a')
    if find(a) != find(b):
        union(a, b)
        answer.append((a, b))


print(len(answer))
for a, b in answer:
    a, b = chr(97 + a), chr(97 + b)
    print(a, b)
