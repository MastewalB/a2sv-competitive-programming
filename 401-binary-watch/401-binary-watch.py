class Solution:
    def countBit(self, N):
        count = 0
        for i in range(32):
            count += ((1 << i) & N) != 0
        return count
    
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        answer = []
        
        for h in range(12):
            for m in range(60):
                if self.countBit(h) + self.countBit(m) == turnedOn:
                    answer.append("%d:%02d" % (h, m))
        
        return answer