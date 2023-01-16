class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        
        matrix = [[0 for _ in range(n + 1)] for _ in range(n) ]
        
        for tr, tc, br, bc in queries:
            for i in range(tr, br + 1):
                matrix[i][tc] += 1
                matrix[i][bc + 1] -= 1
        
        for i in range(n):
            for j in range(1, n + 1):
                matrix[i][j] += matrix[i][j - 1]
        
        return [[matrix[j][i] for i in range(n)] for j in range(n)]