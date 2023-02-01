class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_op = float("inf")
        whites = 0
        j = 0

        for i in range(len(blocks)):
            whites += int(blocks[i] == 'W')
            if i >= k - 1:
                min_op = min(min_op, whites)
                whites -= int(blocks[j] == 'W')
                j += 1
        
        return min_op