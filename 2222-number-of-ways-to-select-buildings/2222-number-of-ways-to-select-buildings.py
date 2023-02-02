class Solution:
    def numberOfWays(self, s: str) -> int:
        O = Z = OZ = ZO = OZO = ZOZ = 0
        
        for digit in s:
            if digit == '1':
                O += 1
                ZO += Z
                ZOZ += OZ
            else:
                Z += 1
                OZ += O
                OZO += ZO
        
        return OZO + ZOZ