class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        total = 0
        m, n = len(grid) - 1, 0
        start = (m, n)
        while m >= 0 and n < len(grid[0]):
            if grid[m][n] < 0:
                total += len(grid[m]) - n
                print(total)
                m -= 1
            else:
                n += 1

        return total
