func waysToSplitArray(nums []int) int {
    var (
        ways int
        N int = len(nums)
        prefix []int = make([]int, N)
    )

    prefix[0] = nums[0]
    for k, v := range nums{
        if k > 0 { prefix[k] = v + prefix[k - 1] }
    }

    for i := 0; i < N - 1; i++ {
        if prefix[i] >= prefix[N - 1] - prefix[i] { ways++ }
    }

    return ways
}