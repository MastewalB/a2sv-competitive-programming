"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        result = []
        prev = 1000
        for i in range(1, 1001):
            left = 1
            right = prev
            while left <= right:
                mid = left + (right - left) // 2

                current = customfunction.f(i, mid)
                if current == z:
                    result.append([i, mid])
                    prev = mid - 1
                    break
                elif current > z:
                    right = mid - 1
                else:
                    left = mid + 1

        return result
