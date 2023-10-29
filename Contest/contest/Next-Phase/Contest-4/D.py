from collections import defaultdict


def isValid(n, graph, bfs):
    if len(bfs) != n:
        return "NO"
    if n > 0 and bfs[0] != 1:
        return "NO"
    i = 0
    j = 1
    while i < len(bfs):

        dest = j + len(graph[bfs[i]])
        while j < len(bfs) and j <= dest - 1:
            if bfs[j] not in graph[bfs[i]]:
                return "NO"
            graph[bfs[j]].remove(bfs[i])
            j += 1
        i += 1

    return "Yes"


def buildGraph():
    graph = defaultdict(set)
    n = int(input())
    for _ in range(n - 1):
        a, b = list(map(int, input().split()))
        graph[a].add(b)
        graph[b].add(a)

    return n, graph


n, graph = buildGraph()
bfs = list(map(int, input().split()))
print(isValid(n, graph, bfs))
