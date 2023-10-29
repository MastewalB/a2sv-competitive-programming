from collections import defaultdict


def bellman_ford(graph, n, src):
    distance = [float("inf")] * n
    distance[0] = 0

    for i in range(n + 1):
        for src, dst, weight in graph:
            if distance[src] != float("inf") and distance[src] + weight < distance[dst]:
                distance[dst] = distance[src] + weight


n, m = list(map(int, input().split()))
graph = []
for _ in range(m):
    a, b, w = list(map(int, input().split()))
    graph.append((a, b, w))

bellman_ford(graph, n, 1)
