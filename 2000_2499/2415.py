# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: 'Optional[TreeNode]') -> 'Optional[TreeNode]': # O( N | N )
        def flat(arr, lvl, node): # preorder traverse the tree.
            if node:
                if lvl == len(arr):
                    arr.append([])
                arr[lvl].append(node.val)
                flat(arr, lvl+1, node.left)
                flat(arr, lvl+1, node.right)
        
        arr = []
        flat(arr, 0, root)
        nodes = []
        for i, a in enumerate(arr): #reverse the odd layer
            if i % 2:
                nodes += a[::-1]
            else:
                nodes += a
        
        def build(nodes, idx): #build a new tree, based on the flattened array
            if idx < len(nodes):
                node = TreeNode(nodes[idx])
                node.left =  build(nodes, idx*2+1)
                node.right = build(nodes, idx*2+2)
                return node
        
        return build(nodes, 0)
            
                
        
        
        
       



