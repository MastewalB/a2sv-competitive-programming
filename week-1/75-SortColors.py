def sort_colors(nums):
    count_arr = [0] * 301
    for i in range(len(nums)):
        count_arr[nums[i]] += 1
    cursor = 0
    for k in range(len(count_arr)):
        for i in range(count_arr[k]):

            nums[i + cursor] = k
        cursor += count_arr[k]
