from collections import defaultdict, deque


def findEarliestAncestor(pairs, a):
    graph = defaultdict(list)

    for parent, child in pairs:
        graph[child].append(parent)

    queue = deque([a])
    ancestor = -1

    while queue:
        ancestor = -1
        size = len(queue)
        for _ in range(size):
            node = queue.popleft()
            ancestor = node
            for parent in graph[node]:
                queue.append(parent)

    return -1 if ancestor == a else ancestor


pairs1 = [
    (2, 3), (3, 15), (3, 6), (5, 6), (5, 7),
    (4, 5), (4, 8), (4, 9), (9, 11), (14, 4),
]

pairs1 = [
    (2, 3), (3, 15), (3, 6), (5, 6), (5, 7),
    (4, 5), (4, 8), (4, 9), (9, 11), (14, 2), (1, 9)
]
print(findEarliestAncestor(pairs1, 8))
print(findEarliestAncestor(pairs1, 7))
print(findEarliestAncestor(pairs1, 6))
print(findEarliestAncestor(pairs1, 15))
print(findEarliestAncestor(pairs1, 14))
print(findEarliestAncestor(pairs1, 11))
