# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: 'Optional[TreeNode]') -> None: # O( N | 1 )
        """
        Do not return anything, modify root in-place instead.
        """
        def connect(node, sub): # move the sub as the right most leaf of node
            while node and node.right:
                node = node.right
            if node:
                node.right = sub
        
        def helper(node):
            if node:
                helper(node.left)
                helper(node.right)
                connect(node.left, node.right) # move the right tree to the end of left tree, and move back, for the pre-order traversal
                node.right = node.left if node.left else node.right # if left tree exists, move the left tree to right
                node.left = None #void the left tree
        
        helper(root)
        
        
        


# previous solution

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def flatten(self, root: 'Optional[TreeNode]') -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
#         def connect(node, sub): # move the sub as the right most leaf of node
#             while node and node.right:
#                 node = node.right
#             if node:
#                 node.right = sub
        
#         def helper(node):
#             if node:
#                 helper(node.left)
#                 helper(node.right)
#                 connect(node.left, node.right) # move the right tree to the end of left tree, and move back, for the pre-order traversal
#                 node.right = node.left if node.left else node.right # if left tree exists, move the left tree to right
#                 node.left = None #void the left tree
        
#         helper(root)



# previous solution

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def flatten(self, root: TreeNode) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
#         def concat(node, sub): # plug the sub to the end of the node
#             while node.right:
#                 node = node.right
#             node.right = sub

#         def helper(node): #the O(1) extra space
#             if node.left and node.right == None : # move the left to the right
#                 node.right = node.left
#                 node.left = None
#                 helper(node.right)
#             elif node.right and node.left == None: # keep on the right
#                 helper(node.right)
#             elif node.left and node.right: # clean left and clean right
#                 helper(node.left)
#                 helper(node.right)
#                 concat(node.left, node.right) #concat the right to the left
#                 node.right = node.left #make the left as right
#                 node.left = None # remove left
#         if root:
#             helper(root)







# previous approach
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# class Solution:
#     def flatten(self, root: TreeNode) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
#         def helper(arr, node):
#             arr.append(node.val)
#             if node.left:
#                 helper(arr, node.left)
#             if node.right:
#                 helper(arr, node.right)
#         def form(arr, node):
#             if arr:
#                 node.left = None
#                 node.right = TreeNode(arr.pop(0))
#                 form(arr, node.right)
#
#         if root == None:
#             return None
#
#         arr = []
#         helper(arr, root)
#         arr.pop(0)
#         form(arr, root)

# previous approach
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# class Solution:
#     def flatten(self, root: TreeNode) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
#
#         def flat(node, output):
#             if node.left == node.right == None:
#                 output.append(node.val)
#             else:
#                 output.append(node.val)
#                 if node.left:
#                     flat(node.left, output)
#                 if node.right:
#                     flat(node.right, output)
#
#         if root:
#             output = []
#             flat(root, output)
#             root.val = output[0]
#             root.left = None
#             node = root
#             output.pop(0)
#             while output:
#                 node.right = TreeNode(output.pop(0))
#                 node = node.right
#
#
