def max_operations(nums, k):
    count = dict()
    operations = 0

    for i in nums:
        if count.get(k - i):
            if count[k - i] == 1:
                del count[k - i]
            else:
                count[k - i] -= 1
            operations += 1
        else:
            if count.get(i):
                count[i] += 1
            else:
                count[i] = 1

    return operations


nums = [3, 1, 3, 4, 3]
k = 6
ans = max_operations(nums, k)
print(ans)
