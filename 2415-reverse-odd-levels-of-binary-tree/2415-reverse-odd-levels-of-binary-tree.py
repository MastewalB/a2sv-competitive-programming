# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        
        level = 0
        level_members = []
        while queue:
            
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if level % 2 != 0:
                    node.val = level_members[size - i - 1]
                if node.left:
                    if level % 2 == 0 and node.left:
                        level_members.append(node.left.val)
                        level_members.append(node.right.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level % 2 != 0:
                level_members = []
            level += 1
        
        return root