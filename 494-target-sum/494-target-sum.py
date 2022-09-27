class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @lru_cache(None)
        def dp(index, total):
            if index >= len(nums):
                return 1 if total == target else 0

            return dp(index + 1, total + nums[index]) + dp(index + 1, total - nums[index])
        
        return dp(0, 0)