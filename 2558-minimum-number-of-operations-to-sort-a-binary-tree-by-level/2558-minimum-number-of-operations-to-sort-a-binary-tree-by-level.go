/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func minimumOperations(root *TreeNode) int {
    arr, res := treeToArr(root), 0
    for _, v := range arr {
        res += minSwapToSortArr(v)
    }
    return res
}

func treeToArr(root *TreeNode) [][]int {
    var dfs func(*TreeNode, int)
    arr := [][]int{}

    dfs = func(root *TreeNode, level int) {
        if root == nil { return }
        if len(arr) > level {
            arr[level] = append(arr[level], root.Val)
        } else {
            arr = append(arr, []int{ root.Val })
        }
        dfs(root.Left, level + 1)
        dfs(root.Right, level + 1)
    }
    dfs(root, 0)
    return arr
}

func minSwapToSortArr(arr []int) int {
    clone := append(make([]int, 0, len(arr)), arr...)
    correctPos, swap := make(map[int]int), 0

    sort.Ints(clone)
    for k, v := range clone { correctPos[v] = k }

    i := 0
    for i < len(arr) {
        corr := correctPos[arr[i]]
        if corr != i {
            arr[corr], arr[i] = arr[i], arr[corr]
            swap++
        } else {
            i++
        }
    }
    return swap
}