
def isGood(num, k):
    nums = set(range(k + 1))

    for n in num:
        if int(n) in nums:
            nums.remove(int(n))
    return True if not nums else False


count = 0
n, k = list(map(int, input().split()))
for _ in range(n):
    if isGood(input(), k):
        count += 1

print(count)
