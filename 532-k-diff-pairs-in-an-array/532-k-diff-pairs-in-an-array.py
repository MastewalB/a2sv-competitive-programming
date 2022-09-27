class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        sol = set()
        numsSet = set()
        
        for i in range(len(nums)):
            if nums[i] in numsSet and k != 0:
                continue
            a, b, c = nums[i], nums[i] + k, nums[i] - k
            if b in numsSet and (a, b) not in sol and (b, a) not in sol:
                sol.add((a, b))
            if c in numsSet and (a, c) not in sol and (c, a) not in sol:
                sol.add((a, c))
            numsSet.add(a)
        return len(sol)