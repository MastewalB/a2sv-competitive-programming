from collections import OrderedDict
import heapq

od = dict()
highest = ""
heap = []

n = int(input())
for _ in range(n):
    info = input().split(" ")
    name, score = info[0], int(info[1])

    found = False
    for i in range(len(heap)):
        if heap[i][1] == name:
            found = True
            heap[i][0] += -score
            heapq.heapify(heap)
    if not found:
        heapq.heappush(heap, [-score, name])
print(heapq.heappop(heap)[1])
