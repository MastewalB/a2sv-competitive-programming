func maxChunksToSorted(arr []int) int {
    chunk, arrCopy := 0, make([]int, 0)

    for k, v := range arr {
        arrCopy = append(arrCopy, v)
        if isValid(arrCopy, k) { chunk++ }
    }
    return chunk
}

func isValid(arr []int, start int) bool {
    sort.Ints(arr)
    for i := start; i < len(arr); i++ {
        if arr[i] != i { return false }
    }
    return true
}