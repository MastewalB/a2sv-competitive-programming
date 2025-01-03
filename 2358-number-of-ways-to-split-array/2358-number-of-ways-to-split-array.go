func waysToSplitArray(nums []int) int {
    var (
        ways, curr, sum int
        N int = len(nums)
    )

    for _, v := range nums{
        sum += v
    }

    for i := 0; i < N - 1; i++ {
        curr += nums[i]
        if curr >= sum - curr { ways++ }
    }

    return ways
}