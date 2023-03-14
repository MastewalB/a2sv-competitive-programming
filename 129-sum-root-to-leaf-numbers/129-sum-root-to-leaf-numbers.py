# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, num):
            
            left = right = 0
            num += str(root.val)
            if not root.left and not root.right:
                return int(num)
            
            if root.left:
                left = dfs(root.left, num)
            if root.right:
                right = dfs(root.right, num)
            
            return left + right
    
        return dfs(root, "")