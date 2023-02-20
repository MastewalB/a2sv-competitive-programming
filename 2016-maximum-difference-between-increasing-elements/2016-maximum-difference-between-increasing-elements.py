class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res = float("-inf")
        _min = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] > _min:
                res = max(res, nums[i] - _min)
            _min = min(_min, nums[i])
                
        return res if res != float("-inf") else -1