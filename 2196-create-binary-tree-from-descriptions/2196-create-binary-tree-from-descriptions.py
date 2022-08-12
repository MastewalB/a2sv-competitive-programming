# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findRoot(self, descriptions):
        nodes = set()
        for parent, child, side in descriptions:
            nodes.add(parent)
        for parent, child, side in descriptions:
            if child in nodes:
                nodes.remove(child)
        return list(nodes)[0]
        
    def buildGraph(self, descriptions):
        nodes = defaultdict(list)
        
        for parent, child, side in descriptions:
            if not nodes[parent]:
                nodes[parent] = [None, None]
            nodes[parent][side] = child 
        
        return nodes
    
        
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        graph = self.buildGraph(descriptions)
        nodeGraph = defaultdict(TreeNode)
        root = self.findRoot(descriptions)
                
        def dfs(node):
            if not node:
                return 
            if node not in nodeGraph:
                            
                root = TreeNode(node)
                if graph[node]:
                    root.left = dfs(graph[node][1])
                    root.right = dfs(graph[node][0])
                nodeGraph[node] = root
            
            return nodeGraph[node]
        
        for parent, child, side in descriptions:
            if parent not in nodeGraph:
                dfs(parent)
            
        
        return nodeGraph[root]