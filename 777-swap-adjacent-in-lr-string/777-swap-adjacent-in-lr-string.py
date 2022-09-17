class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        N = len(start)
        start_left = []
        start_right = []
        end_left = []
        end_right = []
        
        
        if start.replace("X", "") != end.replace("X", ""):
            return False
        
        for i in range(N):
            if end[i] == 'R':
                end_right.append(i)
            elif end[i] == 'L':
                end_left.append(i)
            if start[i] == 'L':
                start_left.append(i)
            elif start[i] == 'R':
                start_right.append(i)
        
        for i in range(max(len(start_right), len(start_left))):
            if i < len(start_right) and start_right[i] > end_right[i]:
                return False
            if i < len(start_left) and start_left[i] < end_left[i]:
                return False
        
        return True