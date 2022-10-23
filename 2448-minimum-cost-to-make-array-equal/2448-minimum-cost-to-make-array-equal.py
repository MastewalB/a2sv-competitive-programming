class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        
        for i in range(len(nums)):
            nums[i] = [cost[i], nums[i]]
        
        nums.sort(key = lambda x: x[1])
        
        total_spread = sum(cost)
        median = total_spread // 2
        prefix = 0
        target = None
        
        for cost, num in nums:
            prefix += cost
            if prefix >= median:
                target = num
                break

        return sum(c * abs(num - target) for c, num in nums)
