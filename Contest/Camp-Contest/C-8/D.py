from collections import defaultdict, deque


def jzzhu(graph, trainRoutes, n):
    distance = [float("inf")] * (n + 1)
    distance[1] = 0
    # visited = set([1])
    queue = deque([(1, 0)])

    while queue:
        city, dist = queue.popleft()
        for neigh, neighDist in graph[city]:
            if neighDist + dist < distance[neigh]:
                distance[neigh] = neighDist + dist
                queue.append((neigh, distance[neigh]))

    print(distance)
    removable = 0
    for i in range(1, n + 1):
        if i in trainRoutes and distance[i] <= trainRoutes[i]:
            removable += 1

    return removable


def main():
    n, m, k = list(map(int, input().split()))
    graph = defaultdict(list)
    trainRoutes = defaultdict()
    for _ in range(m):
        u, v, x = list(map(int, input().split()))
        graph[u].append((v, x))
        graph[v].append((u, x))
    for _ in range(k):
        city, cost = list(map(int, input().split()))
        trainRoutes[city] = cost

    print(jzzhu(graph, trainRoutes, n))


main()
