def min_pair_sum(nums):
    nums.sort()
    left = 0
    right = len(nums) - 1
    maximum_pair_sum = 0

    while left < right:
        maximum_pair_sum = max(maximum_pair_sum, nums[left] + nums[right])
        left += 1
        right -= 1
    return maximum_pair_sum


nums = [3, 5, 4, 2, 4, 6]
ans = min_pair_sum(nums)
print(ans)
