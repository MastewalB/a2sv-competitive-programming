class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        _sum = 0
        count = defaultdict(int)
        N = len(nums)
        ans = 0
        
        j = 0
        curr_sum = 0
        for i in range(N):
            count[nums[i]] += 1
            curr_sum += nums[i]
            while j < i and (count[nums[i]] > 1 or i - j > k - 1):
                count[nums[j]] -= 1
                curr_sum -= nums[j]
                j += 1
            
            if i - j == k - 1:
                ans = max(ans, curr_sum)
        
        return ans