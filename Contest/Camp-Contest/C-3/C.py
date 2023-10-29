from collections import defaultdict


def topology(graph, n):
    top = ["bus topology", "ring topology",
           "star topology", "unknown topology"]

    edge = set()
    count = defaultdict(int)
    for i in range(1, n + 1):
        edge.add(len(graph[i]))
        count[len(graph[i])] += 1

    if len(edge) == 2 and count[1] == 2 and count[2] == n - 2:
        return top[0]
    if len(edge) == 1 and 2 in count:
        return top[1]
    if len(edge) == 2 and count[1] == n - 1 and count[n - 1] == 1:
        return top[2]

    return top[3]


n, m = list(map(int, input().split()))
graph = defaultdict(list)
for _ in range(m):
    s, d = list(map(int, input().split()))
    graph[s].append(d)
    graph[d].append(s)
print(topology(graph, n))
