# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: 'Optional[TreeNode]') -> bool: #O( N | 1 )
        if root.left and root.right: #if current node has children, check the children 
            return (self.evaluateTree(root.left) and self.evaluateTree(root.right)) if root.val == 3 else (self.evaluateTree(root.left) or self.evaluateTree(root.right))
        return root.val==1 # return current is True
    


        
