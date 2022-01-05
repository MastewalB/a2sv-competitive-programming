class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1 / x

        y = self.myPow(x, n // 2)
        if n % 2 == 0:
            return y * y
        return x * y * y

# 60min
