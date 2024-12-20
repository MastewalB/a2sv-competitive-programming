func wordBreak(s string, wordDict []string) []string {
	var (
		dp        func(int) ([]string, bool)
		dict      = map[string]bool{}
        cache     = map[int]Cache{}
	)

    for _,v := range wordDict { dict[v] = true }

    dp = func(start int) ([]string, bool) {
        if cache[start].canEnd { return cache[start].answers, cache[start].canEnd }
        if start == len(s) { return []string{}, true }

        ends, ans := false, []string{}
        for i := start; i < len(s); i++ {
            if _, ok := dict[s[start:i + 1]]; ok {
                if nxtRes, nxtEnds := dp(i + 1); nxtEnds {
                    if len(nxtRes) == 0 { ans = append(ans, s[start:i + 1]) }
                    for _, v := range nxtRes {
                        ans = append(ans, s[start:i + 1] + " " + v)
                    }
                    ends = nxtEnds
                }
            }
        }
        cache[start] = Cache{
            answers: ans,
            canEnd: ends,
        }
        return ans, ends 
    }
    res, _ := dp(0)
    return res
}

type Cache struct {
    answers []string
    canEnd bool
}