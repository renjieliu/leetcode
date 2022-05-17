# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode: #O(N | N) H is the height of the tree
        def dfs(output, target, node, clone): # dfs,  if current node val is same as the target, get the node from clone
            if node:
                if node.val == target.val:
                    output[0] = clone
                else:
                    dfs(output, target, node.left, clone.left)
                    dfs(output, target, node.right, clone.right)
        output = [None]
        dfs(output, target, original, cloned)
        return output[0]

    


# previous solution

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
#         def dfs(output, node, target, idx):  # find the index of the target node
#             if node.val == target.val:
#                 output[0] = idx
#             else:
#                 if node.left:
#                     dfs(output, node.left, target, 2 * idx + 1)
#                     if output[0] != None:
#                         return
#                 if node.right:
#                     dfs(output, node.right, target, 2 * idx + 2)
#                     if output[0] != None:
#                         return

#         output = [None]
#         dfs(output, original, target, 0)
#         res = []

#         def find(res, node, idx, currIdx):  # find the same location of the node, and add to res
#             if currIdx == idx:
#                 res.append(node)
#             else:
#                 if node.left:
#                     find(res, node.left, idx, 2 * currIdx + 1)
#                     if res: return
#                 if node.right:
#                     find(res, node.right, idx, 2 * currIdx + 2)
#                     if res: return

#         res = []
#         find(res, cloned, output[0], 0)
#         return res[0]






# previous solution

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

# class Solution:
#     def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
#         def dfs(node, target, output):
#             if node.val == target.val:
#                 output.append(node)
#             elif node.left == node.right == None:
#                 return
#             else:
#                 if node.left!=None:
#                     dfs(node.left, target, output)
#                 if node.right!=None:
#                     dfs(node.right, target, output)
#         output = []
#         dfs(cloned, target, output)
#         return output[0] if len(output) > 0 else []
            






