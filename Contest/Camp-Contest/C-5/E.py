
def fox(dots):
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    def inBound(p):
        x, y = p
        return 0 <= x < n and 0 <= y < m
    visited = set()

    def dfs(u, p, path):
        if u in path:
            return True
        path.add(u)
        ux, uy = u
        px, py = p
        c = dots[ux][uy]
        for x, y in directions:
            nx, ny = x + ux, y + uy
            if (nx, ny) != p and inBound((nx, ny)) and (nx, ny) not in visited and dots[nx][ny] == c:
                res = dfs((nx, ny), u, path)
                if res:
                    return res

        path.remove(u)
        visited.add(u)
    for i in range(n):
        for j in range(m):
            if (i, j) not in visited:
                cyc = dfs((i, j), (i, j), set())
                if cyc:
                    return True

    return False


n, m = list(map(int, input().split()))
dots = []
for _ in range(n):
    dots.append(list(input()))
print("Yes") if fox(dots) else print("No")
