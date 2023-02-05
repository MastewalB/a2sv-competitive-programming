class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count = Counter(p)
        
        l = 0
        output = []
        for r, c in enumerate(s):
            count[c] -= 1
            while count[c] < 0:
                count[s[l]] += 1
                l += 1
            if r - l + 1 == len(p):
                output.append(l)
        
        return output