class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        for num in nums:
            l ^= num
        return l
            