def sameSign(a, b):
    return (a > 0 and b > 0) or (a < 0 and b < 0)


def maxSum(nums, n):


t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    print(maxSum(nums, n))
