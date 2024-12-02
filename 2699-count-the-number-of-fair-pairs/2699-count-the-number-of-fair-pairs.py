class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        N = len(nums)
        ans = 0
        nums.sort()

        for i in range(N):
            low = high = -1
            left, right, curr = i + 1, N - 1, nums[i]

            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] + curr < lower:
                    left = mid + 1
                else:
                    low = mid
                    right = mid - 1
            
            left, right = i + 1, N - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] + curr > upper:
                    right = mid - 1
                else:
                    high = mid
                    left = mid + 1
            
            if low >= 0 and high >= 0:
                ans += high - low + 1
        return ans