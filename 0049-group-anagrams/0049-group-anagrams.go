func groupAnagrams(strs []string) [][]string {
    anagrams, res := make(map[string][]string), [][]string{}

    for _, str := range strs {
        key := sortString(str)
        anagrams[key] = append(anagrams[key], str)
    }
    for _, v := range anagrams {
        res = append(res, v)
    }
    return res
}

func sortString(str string) string {
    runes := []rune(str)
    sort.Slice(runes, func(i, j int) bool {
		return runes[i] < runes[j]
	})
    return string(runes)
}