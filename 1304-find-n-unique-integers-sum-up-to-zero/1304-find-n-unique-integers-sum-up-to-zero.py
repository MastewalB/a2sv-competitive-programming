class Solution:
    def sumZero(self, n: int) -> List[int]:
        nums = []
        if n % 2 != 0:
            nums.append(0)
        
        for i in range(1, (n // 2) + 1):
            nums.extend([-i, i])
        
        return nums