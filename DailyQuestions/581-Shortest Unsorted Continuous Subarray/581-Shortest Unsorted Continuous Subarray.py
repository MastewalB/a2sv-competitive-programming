class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        left, right = 0, len(nums) - 1

        while left < len(nums) - 1 and nums[left] <= nums[left + 1]:
            left += 1
        while right > 0 and nums[right] >= nums[right - 1]:
            right -= 1

        if left > right:
            return 0

        disturbance = nums[left: right + 1]
        minDisturber = min(disturbance)
        maxDisturber = max(disturbance)

        while left > 0 and nums[left - 1] > minDisturber:
            left -= 1
        while right < len(nums) - 1 and nums[right + 1] < maxDisturber:
            right += 1

        return right - left + 1
