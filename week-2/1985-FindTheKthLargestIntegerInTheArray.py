def find_kth_largest_element(nums, k):
    nums.sort(key=int)
    return nums[-k]
