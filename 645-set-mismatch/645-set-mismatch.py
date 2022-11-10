class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        return [sum(nums) - sum(set(nums)), list(set(list(range(1, len(nums) + 1))) - set(nums))[0]]