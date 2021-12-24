from collections import deque


def shortest_subarray(nums, k):
    queue = deque()
    shortest_subarray_length = len(nums) + 1
    total = 0

    for i in range(len(nums)):
        if nums[i] >= k:
            return 1

        queue.append(nums[i])
        total += nums[i]

        while queue and queue[0] < 0:
            total -= queue[0]
            queue.popleft()

        if total >= k:
            shortest_subarray_length = min(
                shortest_subarray_length, len(queue))

            j = (i + 1) - len(queue)

            while j < i:
                total -= queue[0]
                queue.popleft()

                if total >= k:
                    shortest_subarray_length = min(
                        shortest_subarray_length, len(queue))

                j += 1

        if total < 0:
            total = 0
            queue.clear()

    if shortest_subarray_length == len(nums) + 1:
        return -1
    return shortest_subarray_length


nums = [-28, 81, -20, 28, -29]
k = 89
nums = [2, -2, 1, -6, 2, 2]
k = 4
nums = [2, -1, 2]
k = 3
nums = [52, 40, 55, -53, -72, 50, -70, 58, 10, 59, -13, 71, -18, -78, -12, 87, -60, -39, -56, -28, 45, -28, -51, 14,
        -7, 71, 74, 69, -99, -34, 53, 16, 65, 7, 58, -33, 59, 43, 12, -34, -17, 72, 37, -100, 25, -63, 46, -61, 100, 36, 63]
k = 303

nums = [75, -32, 50, 32, 97]
k = 129


print("ans - ", shortest_subarray(nums, k))


# print(j, i)
# print(nums[j])
# print("total -", total)
# print("shortest - ", shortest_subarray_length)
