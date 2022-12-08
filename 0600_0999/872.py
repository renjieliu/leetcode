# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: 'Optional[TreeNode]', root2: 'Optional[TreeNode]') -> bool: # O( N | N )
        def leaf(node): # pre-order traversal find the leaf value sequence
            if node == None:
                return []
            return leaf(node.left) + ([node.val] if node.left == node.right == None else []) + leaf(node.right)  
            
        return leaf(root1) == leaf(root2) # check if they have the same leaf value sequence


    
