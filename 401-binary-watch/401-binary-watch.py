class Solution:
    def backtrack(self, turnedOn, hour, minute, watch, startIndex):
        if turnedOn == 0:
            return ["%d:%02d" % (hour, minute)]

        answer = []
        for i in range(startIndex, len(watch)):
            if i < 4 and hour + watch[i] < 12:
                answer.extend(self.backtrack(turnedOn - 1, hour + watch[i], minute, watch, i + 1))
            if i >= 4 and minute + watch[i] < 60:
                answer.extend(self.backtrack(turnedOn - 1, hour, minute + watch[i], watch, i + 1))
        return answer
        
        
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        watch = [1, 2, 4, 8, 1, 2, 4, 8, 16, 32]
        return self.backtrack(turnedOn, 0, 0, watch, 0)