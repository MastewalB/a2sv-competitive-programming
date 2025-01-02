func largestMerge(A string, B string) string {
    var sb strings.Builder
    i, j, N, M := 0, 0, len(A), len(B)
    for i < N && j < M {
        if A[i] > B[j] {
            sb.WriteString(string(A[i]))
            i++
        } else if A[i] < B[j] {
            sb.WriteString(string(B[j]))
            j++
        } else {
            ii, jj := i, j
            for ii < N && jj < M && A[ii] == B[jj] {
                ii++
                jj++
            }
            if jj == M || (ii < N && A[ii] > B[jj]){
                sb.WriteString(string(A[i]))
                i++
            } else {
                sb.WriteString(string(B[j]))
                j++
            }
        }
    }
    for i < N || j < M {
        if i < N {
            sb.WriteString(string(A[i]))
            i++
        }
        if j < M {
            sb.WriteString(string(B[j]))
            j++                        
        }
    }
    return sb.String()
}