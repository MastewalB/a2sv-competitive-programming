class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return
        print(len(s))
        i = 0
        patterns = defaultdict(int)
        output = []

        for j in range(9, len(s)):
            patterns[s[i:j + 1]] += 1
            if patterns[s[i:j + 1]] == 2:
                output.append(s[i:j + 1])
            i += 1
        return output
