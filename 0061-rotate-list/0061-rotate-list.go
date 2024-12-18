/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func rotateRight(head *ListNode, k int) *ListNode {
    if head == nil { return head }

    var tail *ListNode = head
    N := 1
    for tail.Next != nil {
        N++
        tail = tail.Next
    }
    newPos := (0 + k) % N
    if newPos > 0 {
        var tempHead *ListNode = head
        for i := 0; i < N - newPos - 1; i++ { tempHead = tempHead.Next }

        tail.Next = head
        head = tempHead.Next
        tempHead.Next = nil        

    }
    return head
}