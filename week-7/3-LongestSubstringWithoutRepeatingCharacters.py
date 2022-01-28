class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        chars = dict()
        result = 0

        ch = 0
        for i in range(len(s)):
            if chars.get(s[i]):
                while ch < i and s[ch] != s[i]:
                    del chars[s[ch]]
                    ch += 1
                while ch < i and s[ch] == s[i]:
                    del chars[s[ch]]
                    ch += 1

            chars[s[i]] = s[i]
            print(s[ch:i+1])
            result = max(result, (i - ch) + 1)
        return result
