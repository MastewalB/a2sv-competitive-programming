class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        # up # right # down #left
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        m, n = len(board), len(board[0])

        def dfs(row, col):
            visited.add((row, col))
            for x, y in directions:
                new_row, new_col = row + x, col + y
                if 0 <= new_row < m and 0 <= new_col < n and board[new_row][new_col] == "O" and (new_row, new_col) not in visited:
                    dfs(new_row, new_col)

        current = [0, 0]
        while current[1] < n - 1:
            if board[current[0]][current[1]] == "O":
                dfs(current[0], current[1])
            current[1] += directions[1][1]
        while current[0] < m - 1:
            if board[current[0]][current[1]] == "O":
                dfs(current[0], current[1])
            current[0] += directions[2][0]
        while current[1] > 0:
            if board[current[0]][current[1]] == "O":
                dfs(current[0], current[1])
            current[1] += directions[3][1]
        while current[0] > 0:
            if board[current[0]][current[1]] == "O":
                dfs(current[0], current[1])
            current[0] += directions[0][0]

        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if (i, j) not in visited:
                    if board[i][j] == "O":
                        board[i][j] = "X"
