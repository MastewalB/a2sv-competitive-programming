class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        # up # right # down #left
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def dfs(row, col):
            visited.add((row, col))
            area = 1
            for x,  y in directions:
                new_row, new_col = row + x, col + y
                if (0 <= new_row < m
                    and 0 <= new_col < n
                    and grid[new_row][new_col] == 1
                        and (new_row, new_col) not in visited):
                    area += dfs(new_row, new_col)
            return area

        max_area = 0
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and grid[i][j] == 1:
                    area = dfs(i, j)
                    max_area = max(max_area, area)
        return max_area
