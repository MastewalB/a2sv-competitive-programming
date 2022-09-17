class Solution:
    def canChange(self, start: str, target: str) -> bool:
        N = len(start)
        start_left = []
        start_right = []
        target_left = []
        target_right = []
        
        
        if start.replace("_", "") != target.replace("_", ""):
            return False
        
        for i in range(N):
            if target[i] == 'R':
                target_right.append(i)
            elif target[i] == 'L':
                target_left.append(i)
            if start[i] == 'L':
                start_left.append(i)
            elif start[i] == 'R':
                start_right.append(i)
        
        for i in range(max(len(start_right), len(start_left))):
            if i < len(start_right) and start_right[i] > target_right[i]:
                return False
            if i < len(start_left) and start_left[i] < target_left[i]:
                return False
        
        return True