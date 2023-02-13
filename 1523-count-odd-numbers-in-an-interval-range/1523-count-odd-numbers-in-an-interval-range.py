class Solution:
    def countOdds(self, low: int, high: int) -> int:
        N = high - low
        if low % 2 != 0:
            return (N // 2) + 1
        return math.ceil(N / 2)