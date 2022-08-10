class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        a = b = float("inf")
        
        for n in nums:
            if n > b:
                return True 
            if n <= a:
                a = n
            elif n <= b:
                b = n
        
        return False