class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket_2 = curMax = total_max = 0
        basket_1_id = basket_2_id = -1
        
        for i in fruits:
            if i == basket_1_id or i == basket_2_id:
                curMax += 1
                total_max = max(curMax, total_max)
                
                if i == basket_1_id:
                    basket_2 = 0
                    basket_1_id, basket_2_id = basket_2_id, basket_1_id
                basket_2 += 1
            else:
                curMax = basket_2 + 1
                basket_2 = 1
                total_max = max(curMax, total_max)
                
                basket_1_id = basket_2_id
                basket_2_id = i
        return total_max