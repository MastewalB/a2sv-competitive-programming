class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        
        def checkSubsequence(removed):
            sPtr = pPtr = 0
            while sPtr < len(s):
                if sPtr not in removed and p[pPtr] == s[sPtr]:
                    pPtr += 1
                if pPtr == len(p):
                    return True 
                sPtr += 1
            
            return True if pPtr >= len(p) else False
        
        
        left, right = 0, len(removable) - 1
        ans = 0
        
        while left <= right:
            mid = (left + right) >> 1
            
            if checkSubsequence(set(removable[:mid + 1])):
                ans = mid + 1
                left = mid + 1
            else:
                right = mid - 1
        
        return ans