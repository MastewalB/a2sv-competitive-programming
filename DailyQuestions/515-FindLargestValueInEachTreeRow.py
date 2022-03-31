# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return
        queue = deque()
        queue.append(root)
        output = []

        while queue:
            max_node = float("-inf")
            for _ in range(len(queue)):
                node = queue.popleft()
                max_node = max(max_node, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            output.append(max_node)

        return output
