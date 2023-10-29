from collections import deque


def getNeighbours(canyon, x, y, k):
    def inBound(x, y): return 0 <= x < 2 and y > 0
    result = []
    directions = [(0, 1), (0, -1), (1, k), (-1, k)]
    for px, py in directions:
        nx, ny = px + x, py + y
        if inBound(nx, ny):
            result.append((nx, ny))
    return result


def canJump(canyon, n, k):
    queue = deque([(0, 0)])
    visited = set()
    level = -1

    while queue:
        size = len(queue)
        for _ in range(size):
            x, y = queue.popleft()
            if y > n - 1:
                return "YES"
            if (x, y) not in visited and y > level and canyon[x][y] != 'X':
                for nx, ny in getNeighbours(canyon, x, y, k):
                    queue.append((nx, ny))
                visited.add((x, y))

        level += 1

    return "NO"


n, k = list(map(int, input().split()))
canyon = []
for _ in range(2):
    canyon.append(list(input()))
print(canJump(canyon, n, k))
