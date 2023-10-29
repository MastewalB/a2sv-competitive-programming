from heapq import *
from collections import defaultdict


def solve(arr, k, n):
    remainders = defaultdict(int)
    for num in arr:
        diff = k - (num % k) if num > k else k - num
        if diff % k:
            remainders[diff] += 1

    x = 0
    for c, v in remainders.items():
        x = max(x, ((v - 1) * k + c) + 1)
    return x


def min_moves(arr, k, n):
    heap = []
    for num in arr:
        diff = k - (num % k) if num > k else k - num
        if diff % k:
            heappush(heap, diff)

    x = 0
    while heap:
        i = 1
        while heap[0] < x:
            rem = heappop(heap) + (i * k)
            heappush(heap, rem)
            i += 1
        x = heappop(heap) + 1

    return x


t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    print(solve(arr, k, n))
