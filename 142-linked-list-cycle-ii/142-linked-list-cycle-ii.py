# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        tortoise = hare = head
        while hare and hare.next:
            tortoise = tortoise.next
            hare = hare.next.next
            
            if tortoise == hare:
                break
        else:
            return 
                 
        
        tortoise = head
        while tortoise != hare:
            tortoise = tortoise.next
            hare = hare.next
    
        return tortoise