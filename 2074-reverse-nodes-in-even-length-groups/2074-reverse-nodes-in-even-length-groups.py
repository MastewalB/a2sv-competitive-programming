# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def groupNodes(self, head):
        count = []
        n = 1
        while head:
            k = 0
            while k < n and head:
                head = head.next
                k += 1
            count.append(min(n, k))
            n += 1
        return count
    
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodeGroupCount = self.groupNodes(head)
        i = 0
        prev, dummy = None, head
        
        while i < len(nodeGroupCount):     
            nCount = nodeGroupCount[i]
            step = 0
            
            if nCount % 2 != 0:
                while step < nCount:
                    prev = head
                    head = head.next
                    step += 1
            else:
                last = curr = head
                prev.next = nxt = None
                
                while step < nCount:
                    nxt = curr.next
                    curr.next = prev.next
                    prev.next = curr
                    curr = nxt
                    step += 1
                    
                prev, prev.next = last, nxt
                head = prev.next
            i += 1
        
        return dummy