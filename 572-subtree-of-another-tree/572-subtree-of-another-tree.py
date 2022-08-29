# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        @lru_cache(None)
        def dfs(root, sRoot):
            
            if not root and not sRoot:
                return True
            if not root or not sRoot:
                return False
            
            identical = False
            
            if root.val == sRoot.val:
                identical = dfs(root.left, sRoot.left) and dfs(root.right, sRoot.right)
            
            return dfs(root.left, subRoot) or dfs(root.right, subRoot) or identical
                
            
        return dfs(root, subRoot)