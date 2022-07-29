from collections import defaultdict


def trainQueries(stations, queries, n, k):
    graph = defaultdict(list)

    for i in range(len(stations)):
        graph[str(stations[i])].append(i)

    for a, b in queries:
        a, b = str(a), str(b)
        if a not in graph or b not in graph:
            print("NO")
        else:

            if graph[a][0] < graph[b][-1]:
                print("yes")
            else:
                print("NO")


t = int(input())


for _ in range(t):
    input()
    n, k = list(map(int, input().split()))
    stations = list(map(int, input().split()))
    queries = []
    for _ in range(k):
        queries.append(list(map(int, input().split())))

    trainQueries(stations, queries, n, k)
