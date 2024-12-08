import "sort"

func maxCount(banned []int, n int, maxSum int) int {
    nums, sum, j := 0, 0, 0
    N := len(banned) 
    sort.Ints(banned)

    for i := 1; i <= n; i++ {
        for j < N && banned[j] < i {
            j++
        }
        A, C := j < N, i + sum <= maxSum
        if (A && banned[j] != i && C) || (!A && C) {
            sum += i
            nums++
        }
    }
    return nums
}