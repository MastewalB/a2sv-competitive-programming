class Solution:
    def pairsLessThanK(self, nums, k):
        totalCount = 0
        i = 0
        currPairs = 0
        
        for j in range(1, len(nums)):
            while nums[j] - nums[i] > k:
                currPairs -= (j - (i + 1))
                i += 1
            repeated = currPairs
            currPairs += (j - i)
    
            totalCount += currPairs - repeated
        
        return totalCount
            
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        # print(nums)
        N = len(nums)
        left, right = 0, nums[N - 1] - nums[0]
        prev = None
        
        while left < right:
            mid = (left + right) >> 1
            
            pairCount = self.pairsLessThanK(nums, mid)
            if pairCount >= k:
                right = mid
            else:
                left = mid + 1
        
        return left
                