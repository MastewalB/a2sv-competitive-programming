class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for i in range(len(s)):
            c = s[i]
            if count[c] == 1:
                return i
        return -1