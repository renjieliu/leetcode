# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: 'Optional[TreeNode]') -> int: # O( N | 1 )
        def dfs(output, node, prev, chain):
            output[0] = max(output[0], chain + (node.val == prev+1) ) #check if current value is prev + 1, if it is add to the chain
            if node.left:
                dfs(output, node.left, node.val, 1 + (chain if node.val == prev+1 else 0))
            if node.right:
                dfs(output, node.right, node.val, 1 + (chain if node.val == prev+1 else 0))
        output = [1]
        dfs(output, root, float('inf'), 0)
        return output[0]
        


# previous solution

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def longestConsecutive(self, root: TreeNode) -> int:
#         def dfs(node, output, path):
#             if node.left == node.right == None:
#                 return
#             else:
#                 if node.left:
#                     if node.left.val == path[-1] + 1:
#                         output[0] = max(len(path) + 1, output[0])
#                         dfs(node.left, output, path + [node.left.val])
#                     else:
#                         dfs(node.left, output, [node.left.val])
#                 if node.right:
#                     if node.right.val == path[-1] + 1:
#                         output[0] = max(len(path) + 1, output[0])
#                         dfs(node.right, output, path + [node.right.val])
#                     else:
#                         dfs(node.right, output, [node.right.val])

#         if root == None:
#             return 0
#         else:
#             output = [1]
#             dfs(root, output, [root.val])
#             return output[0]

