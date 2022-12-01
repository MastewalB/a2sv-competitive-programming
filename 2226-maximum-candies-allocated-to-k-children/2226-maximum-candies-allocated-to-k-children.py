class Solution:
    def canAllocate(self, candies, k):
        N = 0
        for candy in candies:
            N += (candy // k)
        return N

    def maximumCandies(self, candies: List[int], k: int) -> int:
        left = 0
        right = sum(candies)
        
        while left < right:
            mid = ceil((left + right) / 2)
            if self.canAllocate(candies, mid) >= k:
                left = mid 
            else:
                right = mid - 1
        
        return left