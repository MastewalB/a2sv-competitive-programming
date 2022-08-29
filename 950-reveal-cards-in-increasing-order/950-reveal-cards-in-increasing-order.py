class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        queue = deque()
        
        while deck:
            if queue:
                queue.appendleft(queue.pop()) 
            queue.appendleft(deck.pop())
        
        return queue