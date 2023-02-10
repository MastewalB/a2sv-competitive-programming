class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        N = len(grid)
        queue = deque()
        directions = [[1, 0],[0, 1],[-1, 0],[0, -1]]
        in_bound = lambda r, c: 0 <= r < N and 0 <= c < N
        visited = set()

        def neighbours(px, py):
            all_neigh = []
            for dx, dy in directions:
                nx, ny = px + dx, py + dy
                if in_bound(nx, ny) and (nx, ny) not in visited and grid[nx][ny] == 0:
                    all_neigh.append((nx, ny))
                    visited.add((nx, ny))
            return all_neigh
        
        water = 0
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    visited.add((i, j))
                else:
                    water += 1
        if water == 0:
            return -1
        
        level = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                r, c = queue.popleft()
                for x, y in neighbours(r, c):
                    queue.append((x, y))
            level += 1
        
        return level - 1
