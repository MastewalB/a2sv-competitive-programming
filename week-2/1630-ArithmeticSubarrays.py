def check_arithmetic_subarrays(nums, l, r):
    answer = []
    total_sum = []
    total_sum.append(nums[0])
    for i in range(1, len(nums)):
        total_sum.append(total_sum[i - 1] + nums[i])

    for i in range(len(l)):
        slc = nums[l[i]:r[i] + 1]
        slc.sort()
        interval = abs(slc[1] - slc[0])
        print(slc, interval)

        for j in range(1, len(slc)):
            if abs(slc[j] - slc[j - 1]) != interval:
                answer.append(False)
                break
            if j == len(slc) - 1:
                answer.append(True)
    return answer


nums = [-3, -6, -8, -4, -2, -8, -6, 0, 0, 0, 0]
l = [5, 4, 3, 2, 4, 7, 6, 1, 7]
r = [6, 5, 6, 3, 7, 10, 7, 4, 10]

ans = check_arithmetic_subarrays(nums, l, r)
print(ans)
