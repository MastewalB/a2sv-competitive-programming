class Solution:
    def minWindow(self, s: str, t: str) -> str:
        requiredDict = Counter(t)
        requiredLen = len(requiredDict)

        left = 0
        window = defaultdict(int)
        formed = 0
        output = float("inf")
        begin, end = None, None

        for right in range(len(s)):
            c = s[right]
            window[c] += 1

            if c in requiredDict and window[c] == requiredDict[c]:
                formed += 1
            while left <= right and formed == requiredLen:

                if right - left + 1 < output:
                    output = right - left + 1
                    begin = left
                    end = right

                window[s[left]] -= 1
                if s[left] in requiredDict and window[s[left]] < requiredDict[s[left]]:
                    formed -= 1

                left += 1
        return s[begin:end + 1] if begin != None and end != None else ""
