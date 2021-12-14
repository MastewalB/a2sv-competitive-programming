from datetime import datetime


def max_frequency(nums, k):

    nums.sort()
    maximum_frequency = 0
    nums_copy = nums[:]
    begin = 0
    for i in range(1, len(nums)):
        local_frequency = 1
        j = begin
        while j < i:
            if nums_copy[j] == nums_copy[i]:
                local_frequency += 1
                j += 1
                continue
            if nums_copy[i] - nums_copy[j] <= k:
                k -= nums_copy[i] - nums_copy[j]
                nums_copy[j] += nums_copy[i] - nums_copy[j]
                local_frequency += 1
            else:
                k += nums_copy[begin] - nums[begin]
                begin += 1

            j += 1
        if local_frequency > maximum_frequency:
            maximum_frequency = local_frequency

    return maximum_frequency


nums = [1, 2, 4, 5]
nums = [3, 4, 7, 8]
nums = [1, 4, 8, 8, 13]

k = 5
b = datetime.now()
print(max_frequency(nums, k))
a = datetime.now()
print(a - b)
