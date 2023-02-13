class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if grid[0][0] or grid[m - 1][m - 1]:
            return -1
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1],
                      [1, 1], [-1, -1], [1, -1], [-1, 1]]

        in_bound = lambda row, col: (0 <= row < m and 0 <= col < m and grid[row][col] == 0)
        queue = deque()
        queue.append((0, 0, 1))
    
        
        while queue:
            row, col, cells = queue.popleft()
            if row == m - 1 and col == m - 1:
                return cells
            
            for x, y in directions:
                new_x, new_y = row + x, col + y
                if in_bound(new_x, new_y):
                    grid[new_x][new_y] = 1
                    queue.append((new_x, new_y, cells + 1))        
            
        return -1