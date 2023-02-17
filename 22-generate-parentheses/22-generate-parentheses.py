class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def isValidParenthesis(s):
            cntOpen = 0
            for c in s:
                if c == '(':
                    cntOpen += 1
                else:
                    if cntOpen == 0: return False
                    cntOpen -= 1
            return cntOpen == 0
        
        def backtrack(i, path):
            if i == 2 * n:
                if isValidParenthesis(path):
                    ans.append(path)
                return
            
            backtrack(i+1, path + "(")  
            backtrack(i+1, path + ")") 
            
        backtrack(0, "")
        return ans