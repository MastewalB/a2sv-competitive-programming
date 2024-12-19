func removeComments(source []string) []string {
    var (
        lineStr strings.Builder
        block bool
        n int = len(source)
        curr int = 0
    )

    for i := 0; i < n; i++ {
        line := source[i]
        m := len(line)

        for j := 0; j < m; {
            if j < m - 1 && line[j:j + 2] == "//" && !block {
                break
            } else if j < m - 1 && line[j:j + 2] == "/*" && !block {
                block = true
                j += 2
            } else if j < m - 1 && line[j:j + 2] == "*/" && block {
                block = false
                j += 2
            } else {
                if !block {
                    lineStr.WriteString(string(line[j]))
                }
                j++
            }
        }
        if !block && lineStr.Len() > 0 {
            source[curr] = lineStr.String()
            curr++
            lineStr.Reset()
        }
    }

    return source[:curr]
}