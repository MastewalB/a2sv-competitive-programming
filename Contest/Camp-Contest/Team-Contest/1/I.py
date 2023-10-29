from collections import defaultdict, deque


def shortestPath(graph, forbidden, n, m, k):
    visited = set((-1, 1))
    queue = deque([(1, -1)])
    previous = {(1, -1): (-1, -1)}

    while queue:
        for _ in range(len(queue)):

            P, G = queue.popleft()
            if P == n:
                path = [P]
                while G != -1:
                    P, G = previous[(P, G)]
                    path.append(P)
                path.reverse()
                return path
            for C in graph[P]:
                if (P, C) not in visited and (G, P, C) not in forbidden:
                    previous[(C, P)] = (P, G)
                    visited.add((P, C))
                    queue.append((C, P))

    return -1


def main():
    n, m, k = list(map(int, input().split()))
    graph = defaultdict(list)
    forbidden = set()
    for _ in range(m):
        a, b = list(map(int, input().split()))
        graph[a].append(b)
        graph[b].append(a)

    for _ in range(k):
        a, b, c = list(map(int, input().split()))
        forbidden.add((a, b, c))

    shortest = shortestPath(graph, forbidden, n, m, k)
    if shortest == -1:
        print(-1)
    else:
        print(len(shortest) - 1)
        print(*shortest)


main()
