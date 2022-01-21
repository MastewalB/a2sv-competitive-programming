class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0]
        result = nums[0]
        Max = (-sys.maxsize) - 1
        for i in range(1, k + 1):
            if i < len(nums):
                ret_val = self.maxResult(nums[i:], k)
                if ret_val > Max:
                    Max = ret_val
        result += Max
        return result
