class Solution:
    def largestPalindromic(self, num: str) -> str:
        
        res = []
        count = Counter(num)
        
        for i in '9876543210':
            res += count[i] // 2 * i
        
        res = ''.join(res).lstrip('0')
        middle = max(count[i] % 2 * i for i in count)
        
        return res + middle + res[::-1] or "0"