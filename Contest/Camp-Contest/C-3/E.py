import sys
import threading


def polycarpus(graph, n, m, k):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set()

    def inBound(x, y):
        return 0 <= x < n and 0 <= y < m
    C = n * m
    start = None

    for i in range(n):
        for j in range(m):
            if graph[i][j] == '#':
                C -= 1
            if not start and graph[i][j] == '.':
                start = (i, j)

    visited.add(start)
    count = 0

    def dfs(p, lim):
        nonlocal count
        px, py = p
        count += 1
        if count > lim:
            graph[px][py] = 'X'

        for x, y in directions:
            nx, ny = px + x, py + y
            if (nx, ny) not in visited and inBound(nx, ny) and graph[nx][ny] == '.':
                visited.add((nx, ny))
                dfs((nx, ny), lim)

    if k > 0:
        dfs(start, C - k)
    for i in range(n):
        for j in range(m):
            print(graph[i][j], end="")
        print()


def main():
    n, m, k = list(map(int, input().split()))
    maze = []
    for _ in range(n):
        maze.append(list(input()))

    polycarpus(maze, n, m, k)


threading.stack_size(1 << 27)
# sys.setrecursionlimit(1000)
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
