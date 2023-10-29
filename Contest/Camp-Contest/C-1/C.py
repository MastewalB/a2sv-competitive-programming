def makeOne(nums, N):
    zeroes, neg, pos = 0, 0, 0
    cost = 0
    for i in range(N):
        if nums[i] > 0:
            cost += nums[i] - 1
            pos += 1
        elif nums[i] < 0:
            cost += abs(nums[i] + 1)
            neg += 1
        else:
            cost += 1
            zeroes += 1

    if neg % 2 != 0 and zeroes == 0:
        cost += 2

    return cost


n = int(input())
nums = list(map(int, input().split()))
print(makeOne(nums, n))
