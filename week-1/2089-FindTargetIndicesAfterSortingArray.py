def target_indices(nums, target):
    count_arr = [0] * 100
    answer = []
    for i in range(len(nums)):
        count_arr[nums[i]] += 1
    if count_arr[target] == 0:
        return answer
    for k in range(1, len(count_arr)):
        count_arr[k] += count_arr[k - 1]

    if target == 0:
        return [index for index in range(count_arr[target] - 1)]

    for j in range(count_arr[target - 1], count_arr[target]):
        answer.append(j)

    return answer


nums = [1, 2, 5, 2, 3]
print(target_indices(nums, 2))
