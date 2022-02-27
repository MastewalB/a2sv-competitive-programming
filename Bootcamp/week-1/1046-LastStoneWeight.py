import heapq


class Solution(object):
    def lastStoneWeight(self, stones):
        stone_heap = []
        for stone in stones:
            heapq.heappush(stone_heap, -stone)

        while len(stone_heap) > 1:
            stone_1 = heapq.heappop(stone_heap)
            stone_2 = heapq.heappop(stone_heap)

            if stone_1 != stone_2:
                heapq.heappush(stone_heap, (stone_1 - stone_2))

        return -stone_heap[0] if stone_heap else 0
