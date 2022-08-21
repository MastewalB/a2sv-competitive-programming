class Solution:
    def largestPalindromic(self, num: str) -> str:
        queue = deque()
        
        def addQueue(num, count):
            for i in range(count // 2):
                queue.appendleft(num)
                queue.append(num)
            
        
        count = Counter(num)
        heap = []
        oneCountHeap = []
        
        for i in range(10):
            i = str(i)
            if count[i]:
                if count[i] % 2 == 0:
                    heappush(heap, (i, count[i]))
                elif count[i] == 1:
                    heappush(oneCountHeap, -int(i))
                else:
                    heappush(heap, (i, count[i] - 1)) 
                    heappush(oneCountHeap, -int(i))
        
        while heap:
            num, count = heappop(heap)
            addQueue(num, count)
        if queue and queue[0] == '0':
            return str(-heappop(oneCountHeap)) if oneCountHeap else '0'
        res = ''.join(queue)
        N = len(res)
        return res[:N//2] + str(-heappop(oneCountHeap)) + res[N//2:] if oneCountHeap else res