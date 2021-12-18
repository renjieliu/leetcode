# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: 'Optional[TreeNode]', low: int, high: int) -> int:
        def helper(output, node, low, high):
            if node:
                if node.val > high: #exclude the invalid node
                    helper(output, node.left, low, high)
                elif node.val < low: #exclude the invalid node
                    helper(output, node.right, low, high)
                else:
                    output[0] += node.val
                    helper(output, node.left, low, high)
                    helper(output, node.right, low, high)
        output = [0]
        helper(output, root, low, high)
        return output[0]


# previous approach 
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
#         def flat(output, node, low, high):
#             output[0] += node.val if low <= node.val <= high else 0
#             if node.val <= low:
#                 if node.right:
#                     flat(output, node.right, low, high)
#             elif node.val >= high:
#                 if node.left:
#                     flat(output, node.left, low, high)
#             elif low <= node.val <= high:
#                 if node.left: flat(output, node.left, low, high)
#                 if node.right: flat(output, node.right, low, high)

#         output = [0]
#         flat(output, root, low, high)
#         return output[0]


# previous approach
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# class Solution:
#     def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
#         def dfs(output, node):
#             if node == None: return None
#             if L<=node.val<=R:
#                 output.append(node.val)
#                 if node.left!= None:
#                     dfs(output, node.left)
#                 if node.right!=None:
#                     dfs(output, node.right)
#             elif node.val>R and node.left!=None:
#                 dfs(output, node.left)
#             elif node.val<L and node.right!=None:
#                 dfs(output, node.right)
#
#         output = [0]
#         dfs(output, root)
#         return sum(output)