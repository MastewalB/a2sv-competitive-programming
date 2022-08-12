# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        treeDict = defaultdict(TreeNode)
        children = set()
        
        
        for parent, child, side in descriptions:
            
            treeDict[parent].val = parent
            treeDict[child].val = child
            
            if side == 1:
                treeDict[parent].left = treeDict[child]
            else:
                treeDict[parent].right = treeDict[child]
            
            children.add(child)
        
        
        for parent, child, side in descriptions:
            if parent not in children:
                return treeDict[parent]