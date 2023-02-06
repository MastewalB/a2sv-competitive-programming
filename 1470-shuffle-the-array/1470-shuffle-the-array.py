class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        
        half = nums[n:]
        for i in range(n - 1, -1, -1):
            nums[2 * i] = nums[i]
        
        for i in range(0, 2 * n, 2):
            nums[i + 1] = half[i // 2]

        return nums
        """
        2 5 1 3 4 7
        
        
        
        1 2 3 4 | 4 3 2 1
        
        1 4 3 4 | 2 3 2 1
        
        1 4 2 4 | 3 3 2 1
        
        1 4 2 3 | 4 3 2 1
        
        
        
        
        """