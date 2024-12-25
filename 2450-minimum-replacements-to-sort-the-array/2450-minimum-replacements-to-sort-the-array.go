func minimumReplacement(nums []int) int64 {
    if len(nums) < 2 { return 0 }
    var (
        n int = len(nums)
        i int = n - 2
        nxt int = nums[n - 1]
        res int64 = 0
    )

    for ; i >= 0; i-- {
        if nums[i] > nxt {
            steps := (nums[i] - 1) / nxt
            nxt = nums[i] / (steps + 1)
            res += int64(steps)
        } else {
            nxt = nums[i]
        }
    }
    return res
}