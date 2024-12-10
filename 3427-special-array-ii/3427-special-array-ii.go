func isArraySpecial(nums []int, queries [][]int) []bool {
    deviant, n, q := []int{}, len(nums), len(queries)
    res := make([]bool, q)

    for i := 0; i < n - 1; i++ {
        if nums[i] % 2 == nums[i + 1] % 2 {
            deviant = append(deviant, i)
        }
    }

    for k, v := range queries {
        low, high, flag := v[0], v[1], true
        l, r := 0, len(deviant) - 1
        for l <= r {
            mid := (l + r) / 2
            if deviant[mid] < low {
                l = mid + 1
            } else {
                if deviant[mid] >= high {
                    r = mid - 1
                } else {
                    flag = false
                    break
                }
            }
        }
        res[k] = flag
    }
    return res
}