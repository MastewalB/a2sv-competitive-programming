class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        count = float("inf")

        left = 0
        for right in range(len(nums)):
            total += nums[right]

            while left <= right and total >= target:
                count = min(count, right - left + 1)
                total -= nums[left]
                left += 1

        return count if count < float("inf") else 0
