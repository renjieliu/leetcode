# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: 'Optional[TreeNode]') -> 'List[int]': # O( N | 1 )
        def helper(output, n, node):
            if node:
                if len(output) == n: # using the length of the output, to determine if current is the one to be recorded.
                    output.append(node.val)
                helper(output, n+1, node.right) #right first
                helper(output, n+1, node.left) 
        output = []
        helper(output, 0, root)
        return output

    


# previous solution

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def rightSideView(self, root: TreeNode) -> 'List[int]':
#         def look(output, order, node):
#             if order == len(output):
#                 output.append(node.val)
#             if node.right:
#                 look(output, order + 1, node.right)
#             if node.left:
#                 look(output, order + 1, node.left)

#         output = []
#         if root == None:
#             return output
#         else:
#             look(output, 0, root)
#             return output

# previous approach
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# class Solution:
#     def rightSideView(self, root: TreeNode) -> 'List[int]':
#         if root == None:return []
#         output= []
#         def look(node, currentLayer, output):
#             if node:
#                 if currentLayer == len(output):
#                     output.append(node.val)
#                 look(node.right, currentLayer+1, output) #look right first
#                 look(node.left, currentLayer+1, output) # if not there, then look on left
#         look(root, 0, output)
#         return output

# previous approach
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# class Solution:
#     def rightSideView(self, root: TreeNode) -> 'List[int]':
#         if root == None:return []
#         output= []
#         def look(node, currentLayer, output):
#             if node:
#                 if currentLayer == len(output):
#                     output.append(node.val)
#                 look(node.right, currentLayer+1, output) #look right first
#                 look(node.left, currentLayer+1, output) # if not there, then look on left
#         look(root, 0, output)
#         return output