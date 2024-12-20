func wordBreak(s string, wordDict []string) bool {
	var (
		dp    func(int) bool
		dict  = map[string]bool{}
		cache = map[int]bool{}
	)
    
    for _,v := range wordDict { dict[v] = true }

    dp = func(start int) bool {
        if _, ok := cache[start]; ok { return cache[start] }
        if start == len(s) { return true }

        ends := false
        for i := start; i < len(s); i++ {
            if _, ok := dict[s[start:i + 1]]; ok {
                ends = ends || dp(i + 1) 
            }
        }
        cache[start] = ends
        return ends 
    }
    return dp(0)
}
