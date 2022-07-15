class Solution:
    def longestCommonSubstring(self, s, t):
        if not s:
            return ""

        longest = [[0 for i in range(len(s))] for j in range(len(s))]
        max_len = 0
        max_end = 0

        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    if i == 0 or j == 0:
                        longest[i][j] = 1
                    else:
                        longest[i][j] = longest[i - 1][j - 1] + 1
                if longest[i][j] > max_len:
                    max_len = longest[i][j]
                    max_end = i

        return s[max_end - max_len + 1: max_end + 1]


s = "babaad"
t = "cabaa"

sol = Solution()
output = sol.longestCommonSubstring(s, t)
print(output)
