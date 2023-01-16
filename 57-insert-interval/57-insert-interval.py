class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        updated = []
        
        start, end = newInterval
        
        for s, e in intervals:
            if e >= start and s <= end:
                start, end = min(start, s), max(end, e)
            else:
                updated.append(min([start, end], [s, e]))
                start, end = max([start, end], [s, e])
        
        updated.append([start, end])
        return updated