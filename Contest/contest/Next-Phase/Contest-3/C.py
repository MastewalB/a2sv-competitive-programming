from collections import defaultdict
import heapq


def buildGraph(edges):
    graph = defaultdict(list)
    for src, dst, weight in edges:
        graph[src].append([dst, weight])
        graph[dst].append([src, weight])
    return graph


def shortest(edges, n):
    path = [float("inf")] * (n + 1)
    indexFrom = [0] * (n + 1)
    heap = [(0, 1)]  # weight, node
    graph = buildGraph(edges)

    while heap:

        old_weight, node = heapq.heappop(heap)
        for neighbor, weight in graph[node]:
            new_weight = weight + old_weight
            if new_weight < path[neighbor]:
                heapq.heappush(heap, (new_weight, neighbor))
                path[neighbor] = new_weight
                indexFrom[neighbor] = node

    if not indexFrom[n]:
        return -1

    output = []
    i = n
    while i != 1:
        output.append(i)
        i = indexFrom[i]
    output.append(1)
    output.reverse()
    return output


n, m = list(map(int, input().split()))
edges = []
for _ in range(m):
    edges.append(list(map(int, input().split())))
res = shortest(edges, n)
if res != -1:
    print(*res)
else:
    print(res)
