class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = (10 ** 9) + 7 
        
        powers = []
        while n > 0:
            power = 2 ** (math.floor(math.log2(n)))
            n -= power
            powers.append(power)
        
        powers.append(1)
        powers.reverse()
        for i in range(2, len(powers)):
            powers[i] *= powers[i - 1]
        
        answer = []
        for left, right in queries:
            product = powers[right + 1] // powers[left]
            answer.append(product % MOD)
        
        return answer