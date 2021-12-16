def number_of_identical_pairs(nums):
    count_list = [0] * 101
    total_good_pairs = 0

    for i in range(len(nums)):
        count_list[nums[i]] += 1

    for i in range(len(count_list)):
        if count_list[i] != 0:
            summation = ((count_list[i] - 1)*(count_list[i])) // 2
            total_good_pairs += summation
    return total_good_pairs


nums = [1, 2, 3, 3, 3, 3, 4, 4, 1, 1, 1]
nums = [5, 5, 1, 77, 96, 96, 89, 80, 12, 23, 1, 6, 3, 66, 39, 88, 48, 38, 44, 32, 44, 36, 60, 87, 53, 77, 72, 49, 13, 39, 60, 60, 71, 68, 80, 75, 79, 38, 4, 14, 59,
        75, 6, 91, 87, 95, 25, 55, 83, 18, 26, 59, 53, 100, 42, 96, 76, 22, 21, 4, 22, 46, 34, 39, 98, 82, 54, 73, 52, 33, 47, 73, 54, 23, 82, 98, 13, 51, 52, 1, 96, 69, 76]
print(number_of_identical_pairs(nums))


# Possible Improvement with memoization
