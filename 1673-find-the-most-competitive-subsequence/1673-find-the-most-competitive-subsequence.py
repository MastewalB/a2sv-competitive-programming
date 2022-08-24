class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        ans = []
        N = len(nums)
        
        for i in range(len(nums)):
            
            while stack and stack[-1] > nums[i] and len(stack) + N - i > k:
                stack.pop()
            if len(stack) < k:
                stack.append(nums[i])
        
        return stack