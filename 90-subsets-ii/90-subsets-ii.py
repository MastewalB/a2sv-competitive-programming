class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        prev = 0
        S = [[]]
        
        for i in range(len(nums)):
            size = len(S)
            begin = 0
            
            if i > 0 and nums[i] == nums[i - 1]:
                begin = prev
            prev = size
            for j in range(begin, size):
                S.append(S[j] + [nums[i]])
        
        return S