# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: 'TreeNode') -> int: # O( N | N )
        output = [0]
        covered = {None} #initiate the covered as None. 
        def helper(output, node, parent, covered): #bottom up, to place the camera at the parent level
            if node:
                helper(output, node.left, node, covered)
                helper(output, node.right, node, covered)
                if ( (parent == None and node not in covered) or node.left not in covered or node.right not in covered):
                    output[0] += 1
                    covered.add(node)
                    covered.add(parent)
                    covered.add(node.left)
                    covered.add(node.right)
                    # covered.update({node, parent, node.left, node.right})

        helper(output, root, None, covered)
        return output[0]
    

    
    

# previous solution

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def minCameraCover(self, root: TreeNode) -> int: #bottom up, to place the camera at the parent level
#         output = [0]
#         covered = {None}
#         def dfs(node, parent = None):
#             if node:
#                 dfs(node.left, node)
#                 dfs(node.right, node)
#                 if ( (parent is None and node not in covered) or
#                         node.left not in covered or node.right not in covered):
#                     output[0] += 1
#                     covered.add(node)
#                     covered.add(parent)
#                     covered.add(node.left)
#                     covered.add(node.right)
#                     # covered.update({node, parent, node.left, node.right})

#         dfs(root)
#         return output[0]

# previous approach
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def minCameraCover(self, root: TreeNode) -> int:
#         def solve(node):
#             # 0: Strict ST; All nodes below this are covered, but not this one
#             # 1: Normal ST; All nodes below and incl this are covered - no camera
#             # 2: Placed camera; All nodes below this are covered, plus camera here
#
#             if not node: return [0, 0, float('inf')]
#             L = solve(node.left)
#             R = solve(node.right)
#
#             dp0 = L[1] + R[1]
#             dp1 = min(L[2] + min(R[1:]), R[2] + min(L[1:]))
#             dp2 = 1 + min(L) + min(R)
#
#             return [dp0, dp1, dp2]
#
#         return min(solve(root)[1:])
#
