func leftmostBuildingQueries(heights []int, queries [][]int) []int {
    var (
        qLen int = len(queries)
        hLen int = len(heights)
        lastProcessed int = hLen
        stack []int = make([]int, 0)
        res []int = make([]int, qLen)
    )

    for _, v := range queries {
        if v[0] > v[1] { v[1], v[0] = v[0], v[1]}
    }
    for i := 0; i < qLen; i++ { queries[i] = append(queries[i], i) }
    sort.Slice(queries, func(x, y int) bool {
        return queries[x][1] > queries[y][1]
    })

    for _, q := range queries {
        x, y, qIndex := q[0], q[1], q[2]
        for i := lastProcessed - 1; i > y; i-- {
            for len(stack) > 0 && heights[i] >= heights[stack[len(stack) - 1]] { stack = stack[:len(stack) - 1] }
            stack = append(stack, i) 
        }
        if x == y || heights[x] < heights[y] {
            res[qIndex] = y
        } else { res[qIndex] = bSearch(heights, stack, heights[x]) }
        lastProcessed = y + 1
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