def largest_number(nums):
    def compare(a, b):
        num_1 = a + b
        num_2 = b + a
        return int(num_1) > int(num_2)

    for i in range(len(nums)):
        nums[i] = str(nums[i])

    for i in range(len(nums)):
        maximum = i
        for j in range(i + 1, len(nums)):
            if compare(nums[j], nums[maximum]):
                maximum = j
        nums[i], nums[maximum] = nums[maximum], nums[i]

    if nums[0] == "0":
        return "0"
    return "".join(nums)
