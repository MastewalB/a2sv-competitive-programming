class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        min_removed = len(s)
        A = set()
        
        def rip(index, count, possible, r):
            nonlocal min_removed
            
            if r > min_removed or count < 0:
                return 
            
            if index == len(s):
                if count == 0:
                    min_removed = min(min_removed, r)
                    A.add(possible)
                return
                        
            if s[index] in ["(", ")"]:
                rip(index + 1, count + 1 if s[index] == "(" else count - 1, possible + s[index], r)
                rip(index + 1, count, possible, r + 1)
            else:
                rip(index + 1, count, possible + s[index], r)
        
        rip(0, 0, "", 0)
        return A