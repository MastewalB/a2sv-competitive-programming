from collections import deque


def shortest_subarray(nums, k):
    queue = deque()
    answer = float('inf')

    prefix_sum = [0] * (len(nums) + 1)

    for i in range(len(nums)):
        if nums[i] >= k:
            return 1
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]

    for i in range(len(prefix_sum)):
        while queue and prefix_sum[i] <= prefix_sum[queue[-1]]:
            queue.pop()

        queue.append(i)

        while queue and (prefix_sum[i] - prefix_sum[queue[0]] >= k):
            answer = min(answer, i - queue.popleft())

    if answer == float('inf'):
        return -1
    return answer


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
