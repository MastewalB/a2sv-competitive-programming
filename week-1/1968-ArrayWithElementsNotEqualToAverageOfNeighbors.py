def rearrange_array(nums):
    nums.sort()
    left, right = 0, len(nums) - 1
    result = []
    while left <= right:
        if left == right:
            result.append(nums[left])
            left += 1
            right -= 1
        else:
            result.append(nums[right])
            result.append(nums[left])
            right -= 1
            left += 1

    return result
