def smallerNumbersThanCurrent(nums):
    count = [0] * 101
    for i in range(len(nums)):
        count[nums[i]] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in range(len(nums)):
        if nums[i] == 0:
            nums[i] = 0
        else:
            nums[i] = count[nums[i] - 1]

    return nums


nums = [37, 64, 63, 2, 41, 78, 51, 36, 2, 20, 25, 41, 72, 100, 17, 43,
        54, 27, 34, 86, 12, 48, 70, 44, 87, 68, 62, 98, 68, 30, 8, 92, 5, 10]

smallerNumbersThanCurrent(nums)
print(nums)
