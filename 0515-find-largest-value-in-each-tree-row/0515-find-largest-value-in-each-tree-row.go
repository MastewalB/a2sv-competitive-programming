/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func largestValues(root *TreeNode) []int {
    if root == nil { return nil }
    queue, output := &Queue{}, []int{}
    queue.Push(root)

    for len(*queue) > 0 {
        _max, l := math.MinInt64, len(*queue)
        for i := 0; i < l; i++ {
            qElem, _ := queue.Pop()
            if node, ok := qElem.(*TreeNode); ok {
                _max = max(node.Val, _max)
                if node.Left != nil { queue.Push(node.Left) }
                if node.Right != nil { queue.Push(node.Right) }
            }
        }
        output = append(output, _max)
    }
    return output
}

type Queue []interface{} 

func (q *Queue) Push(x interface{}) {
    *q = append(*q, x)
}

func (q *Queue) Pop() (interface{}, bool) {
    var el interface{}
    l := len(*q)
    if l == 0 { return el, false }
    el, *q = (*q)[0], (*q)[1:]
    return el, true
}