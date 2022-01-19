# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        temp = head
        head = head.next
        temp.next = None

        while head and head.next:
            temp_2 = head
            head = head.next
            temp_2.next = temp
            temp = temp_2
        head.next = temp
        return head
