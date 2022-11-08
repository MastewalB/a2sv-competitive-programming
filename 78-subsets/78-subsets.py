class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        S = [[]]
        for num in nums:
            size = len(S)
            for i in range(size):
                S.append(S[i] + [num])
        return S