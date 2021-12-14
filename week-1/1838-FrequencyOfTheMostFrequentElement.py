def max_frequency(nums, k):
    nums.sort()
    maximum_frequency = 0

    for i in range(len(nums), -1, -1):
        j = i - 1
        b = k
        while b > 0 and j >= 0:
            if nums[j] == nums[i]:
                j -= 1
