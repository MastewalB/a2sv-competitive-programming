class Solution:
    def compress(self, chars: List[str]) -> int:
        ans = left = right = 0
        def helper(num):
            if num ==1: return []
            return list(str(num))
            
        while right < len(chars):
            if chars[left] == chars[right]:
                right += 1
                continue
            
            chars[ans] = chars[left]
            ans+=1
            num = helper(right - left)
            for i in num:
                chars[ans] = i
                ans += 1
            
            
            left = right
        
        chars[ans] = chars[left]
        ans+=1
        num = helper(right - left)
        for i in num:
            chars[ans] = i
            ans += 1
        
        return ans