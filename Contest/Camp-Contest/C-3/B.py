from collections import defaultdict, deque


def transform(s, t):
    queue = deque([s])
    parent = defaultdict(int)
    visited = set([s])

    while queue:
        size = len(queue)
        for _ in range(size):
            node = queue.popleft()
            if node == t:
                path = []
                while node in parent:
                    path.append(node)
                    node = parent[node]
                path.append(node)
                path.reverse()
                return path
            else:
                for c in [node * 2, node * 10 + 1]:
                    if c not in visited and c <= t:
                        queue.append(c)
                        visited.add(c)
                        parent[c] = node
    return


s, d = list(map(int, input().split()))
res = transform(s, d)
if res:
    print("YES")
    print(len(res))
    print(*res)
else:
    print("NO")
