def removePrefix(nums):
    numSet = set()
    ans = 0
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] in numSet:
            ans = i + 1
            break
        numSet.add(nums[i])
    return ans


t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    print(removePrefix(nums))
