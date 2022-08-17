# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        pathSum = float("-inf")
        
        def maxPath(root):
            nonlocal pathSum
            if not root:
                return 0
            
            left = max(maxPath(root.left), 0)
            right = max(maxPath(root.right), 0)
            
            three = root.val + left + right
            pathSum = max(pathSum, three)
            
            return root.val + max(left, right)
        
        maxPath(root)
        
        return pathSum