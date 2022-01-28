def removeDuplicates(nums):
    if len(nums) < 2:
        return len(nums)
    slow = 0
    fast = 0
    while fast < len(nums):
        if nums[slow] == nums[fast]:
            while fast < len(nums) and nums[fast] == nums[slow]:
                fast += 1
            if fast >= len(nums):
                return slow + 1
            nums[slow + 1], nums[fast] = nums[fast], nums[slow + 1]
            slow += 1
            fast += 1
        else:
            if fast - slow > 1:
                nums[slow + 1], nums[fast] = nums[fast], nums[slow + 1]
            slow += 1
            fast += 1
    return slow + 1


nums = [0, 1, 2, 3, 4]
removeDuplicates(nums)
