func maxScoreSightseeingPair(values []int) int {
    _max, res := values[0], 0

    for i, v := range values {
        if i > 0 {
            res = max(res, _max + v - i)
            _max = max(_max, v + i)
        }
    }
    return res
}