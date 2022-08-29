# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return 
        stack = [root]
        inOrder = []
        
        while stack:
            
            node = stack[-1]
            while node.left:
                stack.append(node.left)
                node = node.left
            
            node = stack.pop()
            inOrder.append(node.val)
            while stack and node.right == None:
                node = stack.pop()
                inOrder.append(node.val)
            
            if node.right:
                stack.append(node.right)
        
        return inOrder