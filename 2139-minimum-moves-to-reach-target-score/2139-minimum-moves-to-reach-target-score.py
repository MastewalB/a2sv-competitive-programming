class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        op = 0
        
        while target > 1:
            
            if maxDoubles > 0:
                if target % 2 == 0:
                    target //= 2
                    maxDoubles -= 1
                else:
                    target -= 1
                op += 1
            else:
                op += target - 1
                break
        
        return op