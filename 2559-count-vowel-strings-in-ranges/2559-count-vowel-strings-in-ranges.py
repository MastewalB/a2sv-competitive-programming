class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        N = len(words)
        count = [0 for _ in range(N)]
        vowels = ['a', 'e', 'i', 'o', 'u']
        
        for i in range(N):
            count[i] += int(words[i][0] in vowels and words[i][-1] in vowels)
            if i > 0:
                count[i] += count[i - 1]
        count.append(0)
        ans = []
        for l, r in queries:
            l = l - 1 if l > 0 else -1
            ans.append(count[r] - count[l])
        
        return ans