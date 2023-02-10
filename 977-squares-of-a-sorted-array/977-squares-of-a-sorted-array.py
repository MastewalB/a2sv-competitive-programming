class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        count, left, right = 1, 0, len(nums) - 1
        output = [0] * len(nums)
        
        while left <= right:
            if nums[left] ** 2 >= nums[right] ** 2:
                output[len(nums) - count] = nums[left] ** 2
                left += 1
            else:
                output[len(nums) - count] = nums[right] ** 2
                right -= 1
            count += 1
        return output