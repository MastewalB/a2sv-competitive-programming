def stipend(students, pair, a, b, c):
    parent = [n for n in range(students)]

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        x, y = find(x), find(y)
        if x != y:
            parent[x] = y

    for x, y in pair:
        union(x, y)
    # print(parent)
    
    return "YES"


students, conn, a, b, c = list(map(int, input().split()))
pair = []
for _ in range(conn):
    pair.append(list(map(int, input().split())))
print(stipend(students, pair, a, b, c))
