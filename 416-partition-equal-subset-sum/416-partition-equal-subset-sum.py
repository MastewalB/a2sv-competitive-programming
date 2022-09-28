class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        @lru_cache(None)
        def dp(index, total):
            if index >= len(nums):
                return False
            if total == 0:
                return True
            
            return dp(index + 1, total - nums[index]) or dp(index + 1, total)
        
        return dp(0, total / 2)