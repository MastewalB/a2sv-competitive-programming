class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        operation = True
        s = list(s)
        count = 0
        
        while operation:
            i = 0
            operation = False
            while i < len(s):
                if i < len(s) - 1 and s[i] == '0' and s[i + 1] == '1':
                    s[i], s[i + 1] = s[i + 1], s[i]
                    operation = True
                    i += 2
                else:
                    i += 1
            
            if operation:
                count += 1
        
        return count