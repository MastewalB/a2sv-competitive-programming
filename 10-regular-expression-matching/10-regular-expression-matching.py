class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        @lru_cache(None)
        def dp(i, j):
            if j == len(p):
                return i == len(s)
            
            if j + 1 < len(p) and p[j + 1] == '*':
                answer = dp(i, j + 2)
                if i < len(s) and (s[i] == p[j] or p[j] == '.'):
                    answer |= dp(i + 1, j)
                return answer
            
            if i < len(s) and (s[i] == p[j] or p[j] == '.'):
                return dp(i + 1, j + 1)
            
            return False
        
        
        return dp(0, 0)
