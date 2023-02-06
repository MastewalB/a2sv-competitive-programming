class DetectSquares:

    def __init__(self):
        self.P = Counter()
        
    def add(self, point: List[int]) -> None:
        x, y = point
        self.P[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        R = 0
        for (x2, y2), cnt in self.P.items():
            if abs(x2-x) == abs(y2-y) and abs(x2-x) != 0:
                R += cnt * self.P[(x, y2)] * self.P[(x2, y)]
        return R
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)