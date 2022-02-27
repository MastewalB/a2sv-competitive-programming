class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        for i in range(len(self.nums) - k):
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        if len(self.nums) <= self.k or val > self.nums[0]:
            heappush(self.nums, val)
        for i in range(len(self.nums) - self.k):
            heappop(self.nums)
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
