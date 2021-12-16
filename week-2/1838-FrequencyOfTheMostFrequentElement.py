from datetime import datetime


def max_frequency(nums, k):

    nums.sort()
    maximum_frequency = 0
    begin = 0
    end = 0
    total_sum = 0

    while end < len(nums):
        total_sum += nums[end]
        if total_sum + k < nums[end] * ((end - begin) + 1):
            total_sum -= nums[begin]
            begin += 1
        maximum_frequency = max((end - begin) + 1, maximum_frequency)
        end += 1

    return maximum_frequency


nums = [1, 2, 4, 5]
nums = [3, 4, 7, 8]
nums = [1, 4, 8, 8, 13]
nums = [1, 3, 3, 4]

k = 5
b = datetime.now()
print(max_frequency(nums, k))
a = datetime.now()
print(a - b)
