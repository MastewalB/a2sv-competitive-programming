from collections import deque


def largestRectangleArea(heights):
    stack = []
    max_area = 0

    return max_area


def largest_rectangle_area(heights):

    heights.append(0)
    stack = [-1]
    answer = 0
    for i in range(len(heights)):
        while heights[i] < heights[stack[-1]]:
            height = heights[stack.pop()]
            width = i - stack[-1] - 1
            answer = max(answer, height * width)
        stack.append(i)
    heights.pop()
    return answer


heights = [1, 5, 6, 3, 3, 3]
heights = [2, 1, 5, 6, 2, 3]
print(largestRectangleArea(heights))
