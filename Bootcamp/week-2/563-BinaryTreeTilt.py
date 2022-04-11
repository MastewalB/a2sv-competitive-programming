# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def calcTilt(root):
            nonlocal tilt
            if root == None:
                return 0
            left = calcTilt(root.left)
            right = calcTilt(root.right)
            tilt += abs(left - right)
            return root.val + left + right

        tilt = 0
        calcTilt(root)
        return tilt
