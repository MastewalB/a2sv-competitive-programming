from collections import defaultdict, deque


def bipartite(graph, edges):
    queue = deque()
    parts = [set(), set()]
    visited = set()

    for i in edges:
        if i not in visited:
            queue.append(i)
            color = 0
            while queue:
                size = len(queue)
                for _ in range(size):
                    u = queue.popleft()
                    for v in graph[u]:
                        if v in parts[color]:
                            return -1
                        parts[1 - color].add(v)

                        if v not in visited:
                            visited.add(v)
                            queue.append(v)
                color = 1 - color

    return parts


n, m = list(map(int, input().split()))
graph = defaultdict(list)
edges = set()
for _ in range(m):
    a, b = list(map(int, input().split()))
    edges.add(a)
    graph[a].append(b)
    graph[b].append(a)
res = bipartite(graph, edges)
if res == -1:
    print(-1)
else:
    for p in res:
        print(len(p))
        print(*list(p))
