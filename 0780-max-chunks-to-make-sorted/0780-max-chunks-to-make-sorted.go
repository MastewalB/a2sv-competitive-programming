func maxChunksToSorted(arr []int) int {
    chunk, _max := 0, arr[0]

    for k, v := range arr {
        _max = max(v, _max)
        if _max == k { chunk++ }
    }
    return chunk
}