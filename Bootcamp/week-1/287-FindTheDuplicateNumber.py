class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = 1
        right = len(nums)

        while left <= right:
            mid = left + (right - left) // 2
            below = self.findNumbersBelowN(mid, nums)

            if below >= mid:
                right = mid - 1
            else:
                left = mid + 1
        return right

    def findNumbersBelowN(self, n, nums):
        count = 0
        for i in range(len(nums)):
            if nums[i] < n:
                count += 1
        return count
