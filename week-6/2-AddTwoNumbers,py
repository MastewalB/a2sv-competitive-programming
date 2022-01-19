# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode()
        temp = ListNode()
        answer.next = temp
        carry = 0

        while l1 or l2:
            dig = 0
            if l1 == None:
                dig = l2.val + carry
                carry, l2 = 0, l2.next
            elif l2 == None:
                dig = l1.val + carry
                carry = 0
                l1 = l1.next
            else:
                dig = l1.val + l2.val + carry
                carry = 0
                l1, l2 = l1.next, l2.next

            if dig > 9:
                carry = 1
            temp.val = dig % 10
            if l1 or l2:
                temp.next = ListNode()
                temp = temp.next

        if carry == 1:
            temp.next = ListNode(carry)

        return answer.next
