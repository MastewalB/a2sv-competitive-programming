class Solution:
    def firstSetBit(self, N):
        for i in range(31, -1, -1):
            if ((1 << i) & N) != 0:
                return i
        
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        
        firstXor = xor
        firstSet = self.firstSetBit(xor)
        for num in nums:
            if ((1 << firstSet) & num) != 0:
                xor ^= num
        
        return [xor, xor ^ firstXor]