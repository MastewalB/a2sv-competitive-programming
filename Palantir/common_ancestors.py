from collections import defaultdict, deque


def hasCommonAncestor(pairs, a, b):
    queue = deque([a, b])
    graph = defaultdict(list)
    visited = set([a, b])

    for parent, child in pairs:
        graph[child].append(parent)

    while queue:
        size = len(queue)
        node = queue.popleft()
        for par in graph[node]:
            if par in visited and par not in (a, b):
                return True
            visited.add(par)
            queue.append(par)

    return False


pairs = [
    (2, 3), (3, 15), (3, 6), (5, 6), (5, 7),
    (4, 5), (4, 8), (4, 9), (9, 11), (14, 4), (1, 20)
]
# print(hasCommonAncestor(pairs, 3, 8))
# print(hasCommonAncestor(pairs, 5, 8))
# print(hasCommonAncestor(pairs, 6, 8))
# print(hasCommonAncestor(pairs, 6, 9))
# print(hasCommonAncestor(pairs, 1, 3))
# print(hasCommonAncestor(pairs, 3, 1))
# print(hasCommonAncestor(pairs, 7, 11))
# print(hasCommonAncestor(pairs, 6, 5))
# print(hasCommonAncestor(pairs, 5, 6))
print(hasCommonAncestor(pairs, 3, 6))
# print(hasCommonAncestor(pairs, 14, 4))
