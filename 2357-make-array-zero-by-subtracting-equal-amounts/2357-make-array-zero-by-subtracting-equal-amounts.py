class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        numsSet = set(nums)
        if 0 in numsSet:
            numsSet.remove(0)
        return len(numsSet)