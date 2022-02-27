class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        valid_min = max(nums)
        left, right = 1, valid_min

        while left <= right:
            mid = left + (right - left) // 2

            local_sum = 0
            for i in nums:
                local_sum += math.ceil(i / mid)
            if local_sum <= threshold:
                valid_min = min(mid, valid_min)
                right = mid - 1
            else:
                left = mid + 1
        return valid_min
