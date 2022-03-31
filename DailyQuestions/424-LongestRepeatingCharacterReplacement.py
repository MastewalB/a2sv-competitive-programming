class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_frequency = i = 0
        sub_array_freq = defaultdict(int)

        for j in range(len(s)):
            sub_array_freq[s[j]] += 1
            max_frequency = max(max_frequency, sub_array_freq[s[j]])

            if j - i + 1 > max_frequency + k:
                sub_array_freq[s[i]] -= 1
                i += 1
        return len(s) - i
