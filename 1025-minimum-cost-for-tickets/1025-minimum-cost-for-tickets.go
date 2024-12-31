func mincostTickets(days []int, costs []int) int {
    var dp func(int) int
    year, cache := make([]int, days[len(days) - 1] + 1), make(map[int]int)

    for _, v := range days { year[v] = 1 }
    dp = func(i int) int {
        if i >= len(year) { return 0 }
        if year[i] == 0 { return dp(i + 1) }

        if _, ok := cache[i]; !ok {
            cache[i] = min(dp(i + 1) + costs[0], dp(i + 7) + costs[1], dp(i + 30) + costs[2])
        }
        return cache[i]
    }

    return dp(1)
}