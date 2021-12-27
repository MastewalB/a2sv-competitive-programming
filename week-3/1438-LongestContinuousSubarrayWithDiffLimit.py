from collections import deque
import heapq


def longest_subarray(nums, limit):
    queue = deque()
    longest = 0

    queue.append(nums[0])
    heap = list(queue)
    heapq.heapify(heap)
    longest += 1

    i = 1
    j = 0
    max_difference = 0
    while i < len(nums):
        if heap and abs(nums[i] - heap[0]) > limit:
            while queue and queue[0] != heap[0]:
                queue.popleft()
                j += 1
            while queue and queue[0] == heap[0]:
                queue.popleft()
                j += 1
        if heap and abs(nums[i] - (heap[0] + max_difference)) > limit:
            while queue and queue[0] != (heap[0] + max_difference):
                queue.popleft()
                j += 1
            while queue and queue[0] == (heap[0] + max_difference):
                queue.popleft()
                j += 1

        else:
            if heap:
                max_difference = max(max_difference, abs(nums[i] - heap[0]))
            queue.append(nums[i])
            longest = max(longest, len(queue))
            i += 1
        print(queue, max_difference)

        heap = list(queue)
        heapq.heapify(heap)

    return longest


nums = [4, 2, 2, 2, 4, 4, 2, 2]
limit = 0
nums = [10, 1, 2, 4, 7, 2]
limit = 5
nums = [1, 5, 6, 7, 8, 10, 6, 5, 6]
limit = 4


print(longest_subarray(nums, limit))
