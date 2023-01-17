class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        N = len(s)
        P = [[0 for _ in range(N)] for _ in range(2)]
        
        P[0][-1] = int(s[-1] == '0')
        P[1][0] = int(s[0] == '1')
        
        for i in range(1, N):
            P[1][i] += P[1][i - 1] + int(s[i] == '1')
            P[0][N - i - 1] += P[0][N - i] + int(s[N - i - 1] == '0')
        
        ans = float("inf")
        for i in range(N):
            _sum = P[0][i] + P[1][i]
            ans = min([ans, _sum - int(s[i] == '1')])
        return min(ans, P[1][-1])