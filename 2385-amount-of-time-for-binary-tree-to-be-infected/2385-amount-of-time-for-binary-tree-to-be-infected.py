# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        parent = {}
        
        def dfs(node):
            nonlocal start
            if not node:
                return 
            if node.val == start:
                start = node
            if node.left:
                parent[node.left.val] = node
            if node.right:
                parent[node.right.val] = node 
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        visited = set()
        queue = collections.deque([start])
        level = 0
        
        while queue:
            
            size = len(queue)
            
            for _ in range(size):
                node = queue.popleft()
                visited.add(node)
                if node.left and node.left not in visited:
                    queue.append(node.left)
                if node.right and node.right not in visited:
                    queue.append(node.right)
                if node.val in parent and parent[node.val] not in visited:
                    queue.append(parent[node.val])
            
            level += 1
        
        return level - 1