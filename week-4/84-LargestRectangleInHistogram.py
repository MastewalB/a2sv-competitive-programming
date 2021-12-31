from collections import deque


def largestRectangleArea(heights):
    stack = []
    max_area = 0
    for i in range(len(heights)):
        # print(stack)
        if stack and heights[stack[-1]] > heights[i]:
            queue = deque()
            area = 0
            while stack and heights[stack[-1]] > heights[i]:
                queue.append(stack.pop())
            while queue:
                # print(queue)
                if queue[-1] != 0:
                    area = heights[queue[-1]] * len(queue)
                    max_area = max(area, max_area)
                queue.pop()
        stack.append(i)
    print(stack)
    while stack:
        reminant = stack.pop()
        while stack and heights[stack[-1]] == heights[reminant]:
            stack.pop()
        if heights[reminant] != 0:
            area = heights[reminant] * (len(heights) - stack[-1]
                                        ) if stack else heights[reminant] * len(heights)
            max_area = max(area, max_area)
            if stack:
                reminant = stack.pop()
            else:
                break

    return max_area


heights = [2, 1, 5, 6, 2, 3]
print(largestRectangleArea(heights))
