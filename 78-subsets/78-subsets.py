class Solution:
    def __init__(self):
        self.subset = []
    def generate(self, nums, index, S):
        if index == len(nums):
            self.subset.append(S[::])
        else:
            self.generate(nums, index + 1, S)
            S.append(nums[index])
            self.generate(nums, index + 1, S)
            S.pop()
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.generate(nums, 0, [])
        return self.subset