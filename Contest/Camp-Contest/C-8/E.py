import sys
import threading
from collections import defaultdict
input = sys.stdin.readline


class Solution:
    def inBound(self, x, y, N, M):
        return 0 <= x < N and 0 <= y < M

    def largestIsland(self, grid, N, M):
        parent = defaultdict()
        rank = defaultdict(int)
        visited = set()

        def maxNeighbor(i, j, N, M):
            total = 0
            seen = set()
            dx, dy = 0, 1
            for _ in range(4):
                x, y = i + dx, j + dy
                if self.inBound(x, y, N, M) and grid[x][y] == "." and parent[(x, y)] not in seen:
                    total += rank[parent[(x, y)]]
                    seen.add(parent[(x, y)])
                dx, dy = dy, -dx
            return total

        def dfs(i, j, p, N, M):
            dx, dy = 0, 1
            parent[(i, j)] = p
            rank[p] += 1

            for _ in range(4):
                x, y = i + dx, j + dy
                if self.inBound(x, y, N, M) and (x, y) not in visited and grid[x][y] == ".":
                    visited.add((x, y))
                    dfs(x, y, p, N, M)
                dx, dy = dy, -dx

        for i in range(N):
            for j in range(M):
                if (i, j) not in visited and grid[i][j] == ".":
                    visited.add((i, j))
                    dfs(i, j, (i, j), N, M)

        for i in range(N):
            for j in range(M):
                if grid[i][j] == "*":
                    grid[i][j] = str((maxNeighbor(i, j, N, M) + 1) % 10)

        for i in range(N):
            print(''.join(grid[i]))


def main():
    # sys.setrecursionlimit(100000)
    n, m = list(map(int, input().split()))
    grid = []
    for _ in range(n):
        grid.append(list(input()))

    solution = Solution()
    solution.largestIsland(grid, n, m)


threading.stack_size(1 << 27)
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
