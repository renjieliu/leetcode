# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def helper(arr, node):
            arr.append(node.val)
            if node.left:
                helper(arr, node.left)
            if node.right:
                helper(arr, node.right)
        def form(arr, node):
            if arr:
                node.left = None
                node.right = TreeNode(arr.pop(0))
                form(arr, node.right)

        if root == None:
            return None

        arr = []
        helper(arr, root)
        arr.pop(0)
        form(arr, root)

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
