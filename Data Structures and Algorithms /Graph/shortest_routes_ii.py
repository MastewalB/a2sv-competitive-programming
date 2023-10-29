from collections import defaultdict


def shortest(graph, queries, n,  q):
    res = [-1] * q

    distance = [[float("inf") for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        distance[i][i] = 0
        for j, w in graph[i]:
            distance[i][j] = min(distance[i][j], w)

    for k in range(n + 1):
        for i in range(n + 1):
            for j in range(n + 1):
                prev = distance[i][j]
                distance[i][j] = min(
                    distance[i][j], distance[i][k] + distance[k][j])
                if distance[i][j] != prev:
                    changed = True

    for i in range(q):
        src, dst = queries[i]
        res[i] = distance[src][dst]
        if res[i] == float("inf"):
            res[i] = -1
    return res


n, m, q = list(map(int, input().split()))
graph = defaultdict(list)
queries = []
for _ in range(m):
    a, b, c = list(map(int, input().split()))
    graph[a].append((b, c))
    graph[b].append((a, c))
for _ in range(q):
    queries.append(list(map(int, input().split())))
for x in shortest(graph, queries, n, q):
    print(x)
