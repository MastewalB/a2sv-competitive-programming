class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candles = []
        output = []
        
        def findNearest(index, direction):
            best, pos = None, None
            left, right = 0, len(candles) - 1
            
            while left <= right:
                mid = left + right >> 1  
                if candles[mid] == index:
                    return candles[mid], mid
                elif candles[mid] < index:
                    if direction == -1:
                        best, pos = candles[mid], mid
                    left = mid + 1
                else:
                    if direction == 1:
                        best, pos = candles[mid], mid
                    right = mid - 1
            return best, pos
        
        for i in range(len(s)):
            if s[i] == "|":
                candles.append(i)
        
        for l, r in queries:
            l, lIndex = findNearest(l, 1)
            r, rIndex = findNearest(r, -1)
            output.append((r - l) - (rIndex - lIndex)) if (l != None and r != None and l < r) else output.append(0)
        
        return output