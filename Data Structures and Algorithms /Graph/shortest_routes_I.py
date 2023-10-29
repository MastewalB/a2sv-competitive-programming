from collections import defaultdict
import heapq


def shortest(graph, n):
    heap = [(1, 0)]  # Syrjälä = 1
    dist = [float("inf")] * (n + 1)
    dist[1] = 0

    while heap:
        dst, length = heapq.heappop(heap)
        length = -length
        if length <= dist[dst]:
            for neigh, old_len in graph[dst]:
                new_len = old_len + length
                if new_len < dist[neigh]:
                    dist[neigh] = new_len
                    heapq.heappush(heap, (neigh, -new_len))

    return dist[1:]


n, m = list(map(int, input().split()))
graph = defaultdict(list)
for _ in range(m):
    a, b, c = list(map(int, input().split()))
    graph[a].append((b, c))
print(*shortest(graph, n))
