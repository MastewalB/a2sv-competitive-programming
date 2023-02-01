class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        answer = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                _sum = 0
                for r in range(max(0, i - k), min(m, i + k + 1)):
                    for c in range(max(0, j - k), min(n, j + k + 1)):
                        _sum += mat[r][c]
                answer[i][j] = _sum 
        
        return answer
                                    