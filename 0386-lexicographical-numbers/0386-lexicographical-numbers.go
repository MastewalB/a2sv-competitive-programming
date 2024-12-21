func lexicalOrder(n int) []int {
    curr := 1
    res := make([]int, 0, n)

    for len(res) < n {
        res = append(res, curr)
        if curr * 10 <= n { 
            curr *= 10
        } else if curr % 10 != 9 && curr + 1 <= n {
            curr += 1
        } else {
            curr /= 10
            for curr % 10 == 9 {
                curr /= 10
            }
            curr += 1
        }
    }

    return res
}