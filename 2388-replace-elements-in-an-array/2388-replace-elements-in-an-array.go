func arrayChange(nums []int, operations [][]int) []int {
    dict := make(map[int]int)
    
    for k, v := range nums {
        dict[v] = k
    }
    for _, v := range operations {
        old, new := v[0], v[1]
        dict[new] = dict[old]
        delete(dict, old)
    }
    for k, v := range dict {
        nums[v] = k
    }
    return nums
}