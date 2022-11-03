class Solution:
    def trap(self, height: List[int]) -> int:
        max_height = 0
        stack = []  # monotonic strictly decreasing stack
        water = 0

        for i in range(1, len(height)):
            if height[i] >= height[max_height]:
                width = i - (max_height + 1)
                water = water + height[max_height] * width if width > 0 else water + 0
                
                for j in range(i - 1, max_height, -1):
                    water -= height[j]
                max_height = i
        
        if max_height < len(height) - 1:
            max_temp = len(height) - 1
            
            for i in range(max_temp, max_height - 1, -1):
                if height[i] >= height[max_temp]:
                   
                    width = max_temp - (i + 1)
                    water = water + height[max_temp] * width if width > 0 else water + 0
                    for j in range(i + 1, max_temp):
                        water -= height[j]
                    max_temp = i
        return water