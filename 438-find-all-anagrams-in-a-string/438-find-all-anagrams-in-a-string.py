class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = Counter(p)
        l = found = 0
        
        window_count = defaultdict(int)
        output = []
        
        for r in range(len(s)):
            letter = s[r]
            window_count[letter] += 1
            
            if letter in p_count and window_count[letter] == p_count[letter]:
                found += 1
            if r - l + 1 == len(p) and found == len(p_count.keys()):
                output.append(l)
            
            if r - l + 1 >= len(p):
                if s[l] in p_count and window_count[s[l]] == p_count[s[l]]:
                    found -= 1
                window_count[s[l]] -= 1
                l += 1
        
        return output