class Solution:
    def canChange(self, start: str, target: str) -> bool:
        N = len(start)
        if start.replace("_", "") != target.replace("_", ""):
            return False
        
        i = j = 0
        
        while i < N and j < N:
            while i < N and start[i] == '_':
                i += 1
            while j < N and target[j] == '_':
                j += 1
            
            if i < N and ((start[i] == 'L' and i < j) or (start[i] == 'R' and i > j)):
                return False 
            
            i += 1
            j += 1
        
        return True