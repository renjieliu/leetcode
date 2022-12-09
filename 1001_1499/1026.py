# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: 'Optional[TreeNode]') -> int: #O( N | 1 )
        def flat(output, curr, node, mx, mi): # greedy, get the mx and mi on the path, and compare the difference
            if node:
                if node.left == node.right == None:
                    output[0] = max( max(mx, node.val) - min(mi, node.val), output[0]) 
                else:
                    flat(output, curr + [node.val], node.left, max(mx, node.val), min(mi, node.val))
                    flat(output, curr + [node.val], node.right, max(mx, node.val), min(mi, node.val))
        
        output = [-float('inf')]
        flat(output, [], root, -float('inf'), float('inf') )
        return output[0]
    


    
    

# previous solution

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def maxAncestorDiff(self, root: 'Optional[TreeNode]') -> int:
#         def helper(output, node):
#             if node.left == node.right == None:
#                 return [node.val, node.val] #[min, max]
            
#             minn = float('inf')
#             maxx = -float('inf')
#             if node.left:
#                 A = helper(output, node.left)
#                 minn = min(minn, A[0])
#                 maxx = max(maxx, A[1])
#             if node.right:
#                 A = helper(output, node.right)
#                 minn = min(minn, A[0])
#                 maxx = max(maxx, A[1])
            
#             output[0] = max(output[0], abs(node.val - minn), abs(node.val-maxx)) # calc the result
            
#             return [min(minn, node.val), max(maxx, node.val)] # return [min of current tree, max of current tree]
    
#         output = [-float('inf')]
        
#         helper(output, root)
#         return output[0]
    
    
    

# previous approach
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def maxAncestorDiff(self, root: TreeNode) -> int:
#         def flat(output, node, maxx, minn):
#             if node.left == node.right == None:
#                 output[0] = max(output[0], max(maxx, node.val) - min(minn, node.val))
#             else:
#                 if node.left:
#                     flat(output, node.left, max(maxx, node.val), min(minn, node.val))
#                 if node.right:
#                     flat(output, node.right, max(maxx, node.val), min(minn, node.val))

#         output = [-float('inf')]
#         flat(output, root, root.val, root.val)
#         return output[0]
