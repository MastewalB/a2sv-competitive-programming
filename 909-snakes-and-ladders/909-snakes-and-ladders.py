class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        def get_location(n, curr):
            r, c = divmod(curr - 1, n)
            if r % 2 == 0:
                return n-1-r, c
            else:
                return n-1-r, n-1-c
        queue = deque([(1, 0)])
        visited = set([1])
        n = len(board)

        while queue:
            curr, dist = queue.popleft()
            r, c = get_location(n, curr)
            if board[r][c] != -1:
                curr = board[r][c]
            if curr == pow(n, 2):
                return dist
            for i in range(curr + 1, min(curr + 7, pow(n, 2) + 1)):
                if i not in visited:
                    queue.append((i, dist + 1))
                    visited.add(i)
        return -1