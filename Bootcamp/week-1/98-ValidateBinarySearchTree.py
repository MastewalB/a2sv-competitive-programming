# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        lower, upper = -float("inf"), float("inf")
        return self.validator(root, lower, upper)

    def validator(self, node, lower, upper):
        if not node:
            return True
        if not lower < node.val < upper:
            return False

        left = self.validator(node.left, lower, node.val)
        right = self.validator(node.right, node.val, upper)

        return left and right
