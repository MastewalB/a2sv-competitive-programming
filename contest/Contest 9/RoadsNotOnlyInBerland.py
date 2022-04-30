def berlandRoads(graph, cities):
    parent = [None] * (cities + 1)
    rank = [0] * (cities + 1)
    cycles = set()

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        x, y = find(x), find(y)
        if x != y:
            x, y = sorted([x, y], key=lambda x: rank[x])
            parent[x] = y
            rank[y] += rank[x]

    for i in range(len(parent)):
        parent[i] = i
    for i, j in graph:

        if find(i) == find(j):
            cycles.add((i, j))
        else:
            union(i, j)
    for i in range(1, len(parent)):
        parent[i] = find(parent[i])

    parents = set(parent[1:])
    print(len(cycles))
    for i, j in cycles:
        for par in parents:
            if find(i) != find(par):
                parent[par] = find(i)
                parents.remove(par)
                print(i, j, i, par)
                break


def main():
    graph = []
    cities = int(input())
    for _ in range(cities - 1):
        road = list(map(int, input().split()))
        graph.append(road)
    berlandRoads(graph, cities)


if __name__ == "__main__":
    main()
