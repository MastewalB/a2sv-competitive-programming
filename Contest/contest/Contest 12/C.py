# import sys
# sys.setrecursionlimit(2000)


def minCost(cost, pairs):
    price_rank = [None] * (len(cost) + 1)

    def find(x):
        while price_rank[x] != x:
            price_rank[x] = price_rank[price_rank[x]]
            x = price_rank[x]
        return x

    def union(x, y):
        x, y = find(x), find(y)
        if x != y:
            x, y = sorted([x, y], key=lambda x: cost[price_rank[x] - 1])
            price_rank[y] = x

    for i in range(len(price_rank)):
        price_rank[i] = i
    for i, j in pairs:
        union(i, j)
    for i in range(1, len(price_rank)):
        price_rank[i] = find(price_rank[i])

    total = 0
    price_rank = set(price_rank)
    price_rank.remove(0)
    # print(price_rank)
    for p in price_rank:
        total += cost[p - 1]
    return total


characters, pair = list(map(int, input().split()))
cost = list(map(int, input().split()))
pairs = []
for _ in range(pair):
    pairs.append(list(map(int, input().split())))
print(minCost(cost, pairs))
