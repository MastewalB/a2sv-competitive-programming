def remove(nums):
    numsSet = set()
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] in numsSet:
            return len(nums) - len(numsSet)

        numsSet.add(nums[i])
    return 0


t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    print(remove(nums))
