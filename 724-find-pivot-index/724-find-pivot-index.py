class Solution:    
    def pivotIndex(self, nums: List[int]) -> int:
        left = [0]
        right = [0] * (len(nums) + 1)
        
        for i in range(len(nums)):
            left.append(nums[i] + left[i])
        for i in range(len(nums) - 1, -1, -1):
            right[i] = nums[i] + right[i + 1]
        for i in range(len(nums)):
            if left[i] == right[i+1]:
                return i
        return -1