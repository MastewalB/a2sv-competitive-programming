# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        
        def check(u, v):
            
            if (u or v) and not (u and v):
                return False
            
            if not (u and v):
                return True
            
            if u.val != v.val:
                return False
            
            return check(u.left, v.right) and check(u.right, v.left)
        
        
        
        return check(root.left, root.right)