# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        def dfs(root, sRoot):
                
            if not root and not sRoot:
                return True
            if not root or not sRoot:
                return False
            
            return root.val == sRoot.val and dfs(root.left, sRoot.left) and dfs(root.right, sRoot.right)
        
                    
        
        return dfs(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)