class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        curr = good = 0
        N = len(nums)
        
        j = 0
        for i in range(len(nums)):
            curr += count[nums[i]]
            count[nums[i]] += 1
            
            while j < i and curr >= k:
                good += N - i
                curr -= count[nums[j]] - 1
                count[nums[j]] -= 1
                j += 1
            
        return good