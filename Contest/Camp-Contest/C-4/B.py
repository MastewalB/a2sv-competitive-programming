import sys
import threading

sys.setrecursionlimit(100000)


def minCost(cost, friends, n, m):
    parent = [i for i in range(n + 1)]
    total = 0
    visited = set()

    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return parent[u]

    def union(u, v):
        u, v = find(u), find(v)
        u, v = sorted([u, v], key=lambda x: cost[x])
        parent[v] = u

    for u, v in friends:
        union(u, v)

    for i in range(1, n + 1):
        find(i)

    for i in range(1, n + 1):
        if i == parent[i]:
            total += cost[i]

    return total


n, m = list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))

friends = []
for _ in range(m):
    friends.append(list(map(int, input().split())))
print(minCost(cost, friends, n, m))


# threading.stack_size(1 << 27)
# main_thread = threading.Thread(target=main)
# main_thread.start()
# main_thread.join()
