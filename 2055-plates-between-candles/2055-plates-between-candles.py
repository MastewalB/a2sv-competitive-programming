class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candles = []
        plateSum = [0] * len(s) 
        output = []
        
        def findNearest(index, direction):
            best = None
            left, right = 0, len(candles) - 1
            
            while left <= right:
                mid = left + right >> 1  
                if candles[mid] == index:
                    return candles[mid]
                elif candles[mid] < index:
                    if direction == -1:
                        best = candles[mid]
                    left = mid + 1
                else:
                    if direction == 1:
                        best = candles[mid]
                    right = mid - 1
            return best
        
        last = None
        for i in range(len(s)):
            if s[i] == "|":
                candles.append(i)
                if last != None:
                    plateSum[i] += i - last - 1
                    plateSum[i] += plateSum[last]
                last = i 
        
        for l, r in queries:
            l, r = findNearest(l, 1), findNearest(r, -1)
            output.append(plateSum[r] - plateSum[l]) if (l != None and r != None and l < r) else output.append(0)
        
        return output