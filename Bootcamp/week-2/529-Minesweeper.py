class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        visited = set()
        count = self.isValid(click[0], click[1], board)
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = "X"
        elif count > 0:
            board[click[0]][click[1]] = str(count)
        else:
            self.dfs(board, click[0], click[1], visited)
        return board

    def isValid(self, i, j, board):
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1],
                      [1, 1], [-1, -1], [1, -1], [-1, 1]]
        count = 0
        for x, y in directions:
            if self.isBounded(x + i, y + j, board) and board[x + i][y + j] == "M":
                count += 1
        return count

    def isBounded(self, i, j, board):
        return 0 <= i < len(board) and 0 <= j < len(board[0])

    def dfs(self, board, i, j, visited):
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1],
                      [1, 1], [-1, -1], [1, -1], [-1, 1]]
        visited.add((i, j))
        board[i][j] = "B"
        for x, y in directions:
            if self.isBounded(x + i, y + j, board) and (x + i, y + j) not in visited and board[x + i][y + j] != "1":
                count = self.isValid(x + i, y + j, board)
                if count == 0:
                    self.dfs(board, x + i, y + j, visited)
                else:
                    board[x + i][y + j] = str(count)
