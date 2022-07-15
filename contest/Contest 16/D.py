from collections import defaultdict
import heapq


def wander(graph, n):
    output = []
    heap = [1]
    visited = set([1])

    while heap:
        node = heapq.heappop(heap)
        output.append(node)

        for neigh in graph[node]:
            if neigh not in visited:
                heapq.heappush(heap, neigh)
                visited.add(neigh)

    print(*output)


n, m = list(map(int, input().split()))
graph = defaultdict(list)
for _ in range(m):
    s, d = list(map(int, input().split()))
    graph[s].append(d)
    graph[d].append(s)


wander(graph, n)
