# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        total = 0
        paths = []
        path = []

        def findPath(root, path, total):
            if not root:
                return
            path.append(root.val)
            total += root.val
            if root and root.left == None and root.right == None:
                if total == targetSum:
                    paths.append(path[:])

                path.pop()
                total -= root.val
                return
            findPath(root.left, path, total)
            findPath(root.right, path, total)
            path.pop()
            total -= root.val

        findPath(root, path, total)
        return paths
