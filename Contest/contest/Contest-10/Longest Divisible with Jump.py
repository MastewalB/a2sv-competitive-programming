def lds(nums, k):

    def dp(index, total, count):
        if index >= len(nums) or total >= k:
            return count
        pick = 0
        not_pick = dp(index + 1, total, count)
        if total + nums[index] <= k:
            pick = dp(index + 1, total + nums[index], count + 1)

        return max(pick, not_pick)


n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))
print(lds(nums, k))
