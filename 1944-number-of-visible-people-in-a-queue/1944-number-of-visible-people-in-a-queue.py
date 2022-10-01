class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        canSee = [0] * len(heights)

        for i in range(len(heights)):
            while stack and heights[stack[-1]] < heights[i]:
                canSee[stack.pop()] += 1
            if stack:
                canSee[stack[-1]] += 1
            stack.append(i)
        
        return canSee