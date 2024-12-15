type Pair struct {
    element string
    count int
}

func countOfAtoms(formula string) string {
    i, N := 0, len(formula)
    stack := make([]Pair, 0)
    var res strings.Builder

    for i < N {
        if formula[i] == '(' {
            stack = append(stack, Pair{ "(", 0})
            i++
        } else if formula[i] == ')' {
            ptr, j := len(stack) - 1, i + 1
            for ; j < N && isNumeric(formula[j]); j++ {}
            num, err := strconv.Atoi(formula[i + 1:min(j, N)])
            if err != nil { num = 1 }
            
            for stack[ptr].element != "(" {
                stack[ptr].count *= num
                ptr--
            }
            stack = append(stack[:ptr], stack[ptr + 1:]...)

            i = j
        } else {
            j := i + 1
            for ; j < N && isLowerAlpha(formula[j]); j++ {}
            k := j
            for ; k < N && isNumeric(formula[k]); k++ {}

            num, err := strconv.Atoi(formula[min(j, N - 1):min(k, N)])
            if err != nil { num = 1 }
            pair := Pair{ formula[i:min(j, N)], num }
            stack = append(stack, pair)
            i = k
        }
    }

    dict, final := map[string]int{}, []string{}
    for _, val := range stack {
        _, ok := dict[val.element]
        if !ok { final = append(final, val.element) }
        dict[val.element] += val.count
    }

    sort.Strings(final)
    for i := 0; i < len(final); i++ { 
        res.WriteString(final[i])
        if dict[final[i]] > 1 { res.WriteString(strconv.Itoa(dict[final[i]])) }
    }
    return res.String()
}

func isLowerAlpha(c byte) bool {
    return c >= 'a' && c <= 'z'
}

func isNumeric(c byte) bool {
    return c >= '0' && c <= '9'
}