func getLargestOutlier(nums []int) int {
    set := map[int]int{}
    total, outlier := 0, math.MinInt32

    for _, v := range nums {
        set[v]++
        total += v
    }

    for k, _ := range set {
        tempSum := total - k
        diff := tempSum - k
        if count, ok := set[diff]; ok == true && (diff != k || count > 1) {
            outlier = max(diff, outlier)
        }
    }

    return outlier
}