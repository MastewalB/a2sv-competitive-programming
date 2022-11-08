class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        S = []
        for seq in range(1 << len(nums)):
            sub = []
            for i in range(len(nums)):
                if seq & (1 << i):
                    sub.append(nums[i])
            S.append(sub)
        return S