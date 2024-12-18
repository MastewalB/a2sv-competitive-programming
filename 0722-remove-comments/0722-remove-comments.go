func removeComments(source []string) []string {
    var temp strings.Builder
    
    str := strings.Join(source, "\\n") + "\\n"
    i, n := 0, len(str)

    for i < n {
        if i < n - 1 && str[i:i + 2] == "//" {
            i = find(str, i + 2, "\\n")
        } else if i < n - 1 && str[i:i + 2] == "/*" {
            i = find(str, i + 2, "*/") + 2
        } else {
            temp.WriteString(string(str[i]))
            i++
        }
    }

    split := strings.Split(temp.String(), "\\n")
    res := make([]string, 0)
    for i := 0; i < len(split); i++ {
        if split[i] != "" {
            res = append(res, split[i])
        }
    }
    return res
}

func find(s string, start int, t string) int {
    for i := start; i <= len(s) - len(t); i++ {
        if s[i: i + len(t)] == t { return i }
    }
    return -1
}