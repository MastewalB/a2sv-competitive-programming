class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = [[] for _ in range(numRows)]
        move = "F"
        curr = 0
        
        i = 0
        while i < len(s):
            ans[curr].append(s[i])
            
            if numRows > 1:
                curr += 1 if move == "F" else -1
            
            if curr == 0:
                move = "F"
            if curr == numRows - 1:
                move = "R"
            
            i += 1
        
        A = ""
        for s in ans:
            A += ''.join(s) 
        return A
            
        
"""
P A H N   A P L S I I G  Y I R
"""