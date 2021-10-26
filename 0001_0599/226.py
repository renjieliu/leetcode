# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: 'Optional[TreeNode]') -> 'Optional[TreeNode]':
        def invert(node):
            if node:
                node.left, node.right = node.right, node.left
                invert(node.left)
                invert(node.right)
        invert(root) 
        return root


# previous approach
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def invertTree(self, root: TreeNode) -> TreeNode:
#         def helper(node):
#             if node.left == node.right == None:
#                 return None
#             else:
#                 t = node.left
#                 node.left = node.right
#                 node.right = t
#                 if node.left:
#                     helper(node.left)
#                 if node.right:
#                     helper(node.right)
#         if root == None : return None
#         else:
#             helper(root)
#             return root



# Previous Solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# class Solution:
#     def invertTree(self, root: TreeNode) -> TreeNode:
#         def invert(node):
#             if node:
#                 if node.left or node.right:
#                     t = node.left
#                     node.left = node.right
#                     node.right = t
#                     invert(node.left)
#                     invert(node.right)
#
#         invert(root)
#         return root
#
