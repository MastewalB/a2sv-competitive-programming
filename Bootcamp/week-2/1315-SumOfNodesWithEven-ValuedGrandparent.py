# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(root, parent, g_parent):
            if root == None:
                return
            nonlocal total
            if g_parent and g_parent % 2 == 0:
                total += root.val
            dfs(root.left, root.val, parent)
            dfs(root.right, root.val, parent)
            return

        total = 0
        dfs(root, None, None)

        return total
