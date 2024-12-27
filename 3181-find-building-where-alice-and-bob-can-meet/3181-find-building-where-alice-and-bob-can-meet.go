func leftmostBuildingQueries(heights []int, queries [][]int) []int {
    var (
        qLen int = len(queries)
        hLen int = len(heights)
        stack []int = make([]int, 0)
        res []int = make([]int, qLen)
        queryMap = make(map[int][][]int)
    )

    for i, v := range queries {
        a, b := v[0], v[1]
        if a > b { b, a = a, b }
        if heights[a] < heights[b] || a == b {
            res[i] = b
        } else {
            queryMap[b] = append(queryMap[b], []int{ a, i }) // queryMap[LargestIndex] = [[SmallerIndex, QueryIndex]....]
        }
    }

    for i := hLen - 1; i >= 0; i-- {
        for _, v := range queryMap[i] {
            h, index := v[0], v[1]
            res[index] = bSearch(heights, stack, heights[h])
        }

        for len(stack) > 0 && heights[i] >= heights[stack[len(stack) - 1]] { stack = stack[:len(stack) - 1] }
        stack = append(stack, i) 
    }
    return res
}

func bSearch(heights, arr []int, val int) int {
    index, l, r := -1, 0, len(arr) - 1

    for l <= r {
        mid := (l + r) / 2
        if heights[arr[mid]] <= val {
            r = mid - 1
        } else if heights[arr[mid]] > val {
            index = arr[mid]
            l = mid + 1
        }
    }
    return index
}