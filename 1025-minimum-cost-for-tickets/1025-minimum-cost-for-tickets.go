func mincostTickets(days []int, costs []int) int {
    var R func(int) int
    year, cache := make([]int, 366), make(map[int]int)

    for _, v := range days { year[v] = 1 }
    R = func(i int) int {
        if val, ok := cache[i]; ok { return val }
        if i > 365 { return 0 }
        if year[i] == 0 { return R(i + 1) }
        ans := min(R(i + 1) + costs[0], R(i + 7) + costs[1], R(i + 30) + costs[2])
        cache[i] = ans
        return ans
    }

    return R(1)
}