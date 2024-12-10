func isArraySpecial(nums []int, queries [][]int) []bool {
    n, q := len(nums), len(queries)
    prefixSum := make([]int, n)
    res := slices.Repeat([]bool{true}, q)

    prefixSum[0] = 0
    for i := 1; i < n; i++ {
        if nums[i] % 2 == nums[i - 1] % 2 {
            prefixSum[i] = prefixSum[i - 1] + 1
        } else {
            prefixSum[i] = prefixSum[i - 1]
        }
    }

    for i := 0; i < q; i++ {
        l, r := queries[i][1], queries[i][0]
        if prefixSum[l] - prefixSum[r] > 0 {
            res[i] = false
        }
    }
    return res
}