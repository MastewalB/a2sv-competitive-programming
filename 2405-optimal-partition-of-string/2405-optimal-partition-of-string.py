class Solution:
    def partitionString(self, s: str) -> int:
        chars = set()
        count = 0
        for c in s:
            if c in chars:
                count += 1
                chars = set()
            chars.add(c)
        
        return count + 1