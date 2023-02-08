class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        numsSet = set(nums)
        M = -1 * pow(2, 31)
        A = B = C = M
        
        for n in nums:
            if n > A:
                C = B
                B = A
                A = n
            elif n > B and n != A:
                C = B
                B = n
            elif n > C and (n != B and n != A):
                C = n
                
        return C if len(numsSet) >= 3 else A