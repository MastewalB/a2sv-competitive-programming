def fall(grid, n, m):

    def down(i, j):
        while i + 1 < n and grid[i + 1][j] not in ["*", "o"]:
            grid[i][j] = "."
            grid[i + 1][j] = "*"
            i += 1

    for i in range(n - 1, -1, -1):
        for j in range(m):
            if grid[i][j] == "*":
                down(i, j)

    return grid


t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    grid = []
    for _ in range(n):
        grid.append(list(input()))
    res = fall(grid, n, m)
    for r in res:
        print(''.join(r))
