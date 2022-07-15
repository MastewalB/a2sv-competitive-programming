class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def extend(sub, s, d):
            nonlocal count

            while s >= 0 and d < len(sub):
                if sub[s] != sub[d]:
                    break
                count += 1
                s -= 1
                d += 1
            return

        for i in range(len(s)):
            extend(s, i, i)
            if i + 1 < len(s) and s[i] == s[i + 1]:
                extend(s, i, i + 1)

        return count
