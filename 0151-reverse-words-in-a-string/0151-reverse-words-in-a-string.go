func reverseWords(s string) string {
    var res strings.Builder

    split := strings.Split(s, " ")
    for i := len(split) - 1; i >= 0; i-- {
        if len(split[i]) > 0 { res.WriteString(split[i] + " ") }
    }
    return strings.TrimRight(res.String(), " ")
}