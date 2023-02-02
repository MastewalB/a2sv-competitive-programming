class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count = Counter(tasks)
        rounds = 0
        
        for k, v in count.items():
            if v < 2:
                return -1
            y = (v - 2) // 3
            v -= 3 * y
            if v == 3 or v == 2:
                rounds += 1 + y
            if v == 4:
                rounds += 2 + y
        
        return rounds