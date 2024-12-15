func myAtoi(s string) int {
    IMAX, N, i, sign, res := pow(2, 31) - 1, len(s), 0, 1, 0

    for ; i < N && s[i] == ' '; i++ {}

    if i < N && (s[i] == '-' || s[i] == '+') {
       if s[i] == '-' { sign = -1 }
       i++
    }

    for i < N && isNumeric(s[i]) {
        val := res * 10 + int(s[i] - '0')
        if val > IMAX {
            res = IMAX
            if sign == -1 { res++ }
            break
        } 
        res = val
        i++
    }
    return sign * res
}

func isNumeric(c byte) bool {
    return c >= '0' && c <= '9'
}

func pow(x, n int) int {
    if n == 0 { return 1 }
    if n == 1 { return x }
    y := pow(x, n / 2)
    if n % 2 == 0 { return y * y }
    return x * y * y
}