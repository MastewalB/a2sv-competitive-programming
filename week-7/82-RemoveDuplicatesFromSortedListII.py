class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode()
        dummy.next = head
        slow, fast = dummy, head

        while slow and slow.next:
            count = 0
            while fast and fast.val == slow.next.val:
                count += 1
                fast = fast.next
            if count > 1:
                slow.next = fast
                continue
            slow = slow.next
            slow.next = fast
        return dummy.next
