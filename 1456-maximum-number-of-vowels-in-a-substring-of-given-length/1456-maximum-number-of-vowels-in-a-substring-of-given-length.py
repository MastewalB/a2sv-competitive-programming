class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxCount = float("-inf")
        count = 0
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        left = 0


        for i in range(len(s)):

            if i - left == k:
                count -= (s[left] in vowels)
                left += 1
            count += (s[i] in vowels)
            maxCount = max(maxCount, count)

        return maxCount
