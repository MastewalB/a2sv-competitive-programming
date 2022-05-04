class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        subs = {}

        subs[s[0]] = s
        for char in t:
            if subs.get(char):
                if len(subs[char]) == 1:
                    return True
                subs[subs[char][1]] = subs[char][1:]
