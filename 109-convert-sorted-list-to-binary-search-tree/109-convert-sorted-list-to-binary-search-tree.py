# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
sys.setrecursionlimit(10000)
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        dummy = ListNode()
        dummy.next = head 
        slow, fast = dummy, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        rootNode = slow.next
        root = TreeNode(rootNode.val)
        slow.next = None
        if root and slow != dummy:
            root.left = self.sortedListToBST(head)
            root.right = self.sortedListToBST(rootNode.next)
        
        return root