class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        inBound = lambda row, col: 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        def dfs(row, col):
            if not inBound(row, col) or grid[row][col] == 0:
                return 1
            
            visited.add((row, col))
            perimeter = 0
            for x, y in directions:
                n_r, n_c = row + x, col + y
                
                if (n_r, n_c) not in visited:
                    perimeter += dfs(n_r, n_c)
            
            return perimeter
        
        start = None
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    start = (i, j)
        
        return dfs(start[0], start[1])