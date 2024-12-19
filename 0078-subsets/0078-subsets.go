func subsets(nums []int) [][]int {
    var res [][]int = [][]int{{}}

    for _, v := range nums {
        l := len(res)
        for i := 0; i < l; i++ {
            res = append(res, append([]int{v}, res[i]...))
        }
    }
    return res
}