class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        queue = deque([amount])
        visited = set([amount])
        coins.sort()
        level = 0
        
        while queue:

            size = len(queue)
            for _ in range(size):
                coin = queue.popleft()
                if coin == 0:
                    return level
                for c in coins:
                    if c <= coin:
                        newCoin = coin - c
                        if newCoin not in visited:
                            queue.append(newCoin)
                            visited.add(newCoin)
                    else:
                        break

            level += 1
        return -1