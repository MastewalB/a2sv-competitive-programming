/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func reverseOddLevels(root *TreeNode) *TreeNode {
    if root == nil { return root }

    var dfs func (left *TreeNode, right *TreeNode, level int)

    dfs = func (left *TreeNode, right *TreeNode, level int) {
        if left == nil && right == nil { return }

        if level % 2 != 0 {
            (*left).Val, (*right).Val = (*right).Val, (*left).Val
        }
        dfs(left.Left, right.Right, level + 1)
        dfs(left.Right, right.Left, level + 1)
        return
    }
    dfs(root.Left, root.Right, 1)
    return root
}