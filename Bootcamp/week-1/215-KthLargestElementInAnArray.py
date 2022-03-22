class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums_neg = [-i for i in nums]
        heapq.heapify(nums_neg)
        for _ in range(k - 1):
            heapq.heappop(nums_neg)
        return -(nums_neg[0])
