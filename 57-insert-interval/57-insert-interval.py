class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        updated = []
        start, end = newInterval
        
        i = 0
        while i < len(intervals):
            s, e = intervals[i]
            
            if e >= start and s <= end:
                start, end = min(start, s), max(end, e)
            else:
                updated.append(min([start, end], [s, e]))
                start, end = max([start, end], [s, e])
            i += 1
        
        updated.append([start, end])
        return updated