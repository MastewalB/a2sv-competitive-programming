class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stack = []
        removal = [0] * len(nums)
        response = 0

        for i in range(len(nums) - 1, -1, -1):
            
            while stack and nums[stack[-1]] < nums[i]:
                removal[i] = max(removal[stack[-1]], removal[i] + 1)
                stack.pop()
            
            stack.append(i)
            response = max(response, removal[i])
            
        return response