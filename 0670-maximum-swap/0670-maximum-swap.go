func maximumSwap(num int) int {
    numArr := toArr(num)
    indices := make(map[int][]int)

    for k, v := range numArr {
        if len(indices[v]) > 1 { indices[v][1] = k }
        indices[v] = append(indices[v], k)
    }

    for i := 9; i >= 1; i-- {
        if numIndex, ok := indices[i]; ok {
            lastIndex := numIndex[len(numIndex) - 1]
            minInd := lastIndex

            for j := 0; j < i; j++ {
                if targetInd, tOk := indices[j]; tOk {
                    minInd = min(minInd, targetInd[0])
                }
            }
            if minInd != lastIndex {
                numArr[minInd], numArr[lastIndex] = numArr[lastIndex], numArr[minInd]
                break
            }
        }
    }
    return toNum(numArr)
}

func toArr(num int) []int {
    res := make([]int, 0)
    for num > 0 {
        res = append(res, num % 10)
        num /= 10
    }
    slices.Reverse(res)
    return res
}

func toNum(arr []int) int {
    N := 0
    for _, v := range arr { N = N * 10 + v }
    return N
}