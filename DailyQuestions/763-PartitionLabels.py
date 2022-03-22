class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}
        output = []
        for i in range(len(s) - 1, -1, -1):
            if not last_index.get(s[i]):
                last_index[s[i]] = i
        current = s[0]
        output.append(last_index[s[0]] + 1)
        for i in range(len(s)):
            if i > last_index[current]:
                output.append((last_index[s[i]] - last_index[current]))
                current = s[i]
            if last_index[s[i]] > last_index[current]:
                output[-1] += last_index[s[i]] - last_index[current]
                current = s[i]
        return output