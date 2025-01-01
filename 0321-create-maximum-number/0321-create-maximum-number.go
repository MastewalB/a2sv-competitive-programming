func maxNumber(nums1 []int, nums2 []int, k int) []int {
    res, M, N := make([]int, k), len(nums1), len(nums2)

    for i := 0; i <= k && i <= M; i++ {
        if k - i > N { continue }
        A := selectK(nums1, i)
        B := selectK(nums2, k - i)
        res = greater(res, merge(A, B), k)
    }   
    return res
}

func selectK(arr []int, k int) []int {
    stack := make([]int, 0)

    for i, v := range arr {
        for len(stack) > 0 && stack[len(stack) - 1] < v && len(arr) - i >= k - (len(stack) - 1) { stack = stack[:len(stack) - 1] }
        stack = append(stack, v)
    }
    return stack[:min(k, len(stack))]
}

func merge(A []int, B []int) []int {
    i, j, M, N, ans := 0, 0, len(A), len(B), make([]int, 0)

    for i < M && j < N {
        if A[i] > B[j] {
            ans = append(ans, A[i])
            i++
        } else if A[i] < B[j] {
            ans = append(ans, B[j])
            j++
        } else {
            I, J := i, j
            for I < M && J < N && A[I] == B[J] {
                J++
                I++
            }
            if J == N || (I < M && A[I] > B[J]) {
                ans = append(ans, A[i])
                i++
            } else {
                ans = append(ans, B[j])
                j++
            }
        }
    }
    for i < M || j < N {
        if i < M {
            ans = append(ans, A[i])
            i++
        }
        if j < N {
            ans = append(ans, B[j])
            j++                        
        }
    }
    return ans
}

func greater(A []int, B []int, K int) []int {
    for i := 0; i < K; i++ {
        if A[i] > B[i] {
            return A
        } else if A[i] < B[i] { return B }
    }
    return B
}