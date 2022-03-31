# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        total = 0

        def path(root, total):
            if not root:
                return
            if root and root.left == None and root.right == None:
                return root.val + total == targetSum
            total += root.val
            return path(root.left, total) or path(root.right, total)

        return path(root, total)
