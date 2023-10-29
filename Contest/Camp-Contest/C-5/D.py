from collections import defaultdict, deque


def trim(graph, n, k):
    queue = deque()
    qSet = set()
    for i in range(1, n + 1):
        qSet.add(i)
        if len(graph[i]) <= 1:
            queue.append(i)

    while queue:
        if k == 0:
            break
        for i in range(len(queue)):
            node = queue.popleft()
            qSet.remove(node)
            if len(graph[node]) > 0:
                ngh = graph[node].pop()
                graph[ngh].remove(node)
                if len(graph[ngh]) == 1:
                    queue.append(ngh)
        k -= 1

    # count = 0
    # for i in range(1, n + 1):
    #     if len(graph[i]) > 0:
    #         count += 1
    return len(qSet)


t = int(input())
for _ in range(t):
    input()
    graph = defaultdict(set)
    n, k = list(map(int, input().split()))
    for _ in range(n - 1):
        a, b = list(map(int, input().split()))
        graph[a].add(b)
        graph[b].add(a)
    print(trim(graph, n, k))
