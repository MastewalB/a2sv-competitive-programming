# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        longestLen = float("-inf")
        
        def longest(root):
            nonlocal longestLen            

            equalLeft = 0
            equalRight = 0
            if root.left:
                leftLen = longest(root.left)
                if root.left.val == root.val:
                    equalLeft += leftLen + 1
                
            if root.right:
                rightLen = longest(root.right)
                if root.right.val == root.val:
                    equalRight += rightLen + 1
            
            longestLen = max(longestLen, equalLeft + equalRight)
            return max(equalLeft, equalRight)
        
        longest(root)
        return longestLen