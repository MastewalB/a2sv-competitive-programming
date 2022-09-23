class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        for i in range(len(nums)):
            nums[i] = [nums[i], i]
        
        nums.sort(key=lambda x: x[0])
        for i in range(len(nums)):
            if i > 0:
                if nums[i][0] > nums[i - 1][0]:
                    res[nums[i][1]] = i
                else:
                    res[nums[i][1]] = res[nums[i - 1][1]]
        return res