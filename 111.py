# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def flat(output, node, lvl):
            if node.left == node.right == None:  # reach the leaf and compare
                output[0] = min(output[0], lvl)
            else:
                if node.left:
                    flat(output, node.left, lvl + 1)
                if node.right:
                    flat(output, node.right, lvl + 1)

        if root == None: return 0
        output = [float('inf')]
        flat(output, root, 1)
        return output[0]



# previous approach
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# class Solution:
#     def minDepth(self, root: TreeNode) -> int:
#         def dfs(curr, output, node):
#             if node:
#                 if node.left == node.right == None:
#                     output.append(curr)
#                 else:
#                     if node.left!=None:
#                         dfs(curr+1, output, node.left)
#                     if node.right!=None:
#                         dfs(curr+1, output, node.right)
#         if root == None: return 0
#         else:
#             output = []
#             dfs(1, output, root)
#         return min(output)