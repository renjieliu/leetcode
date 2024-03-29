# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: 'TreeNode') -> int: #O( N | 1 )
        def dfs(output, node, mx): #go through all the nodes, and record the max in current path
            if node:
                output[0] += (node.val >= mx) #add to the output if node.val is >= pathMax
                dfs(output, node.left, max(node.val, mx))
                dfs(output, node.right, max(node.val, mx))
        output = [0]
        dfs(output, root, -float('inf'))
        return output[0]
    
    


# previous solution

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def goodNodes(self, root: TreeNode) -> int:
#         def dfs(output, currMax, node):
#             if node.left == node.right == None:
#                 if node.val >= currMax:
#                     output[0] += 1
#             else:
#                 output[0] += 1 if node.val >= currMax else 0
#                 if node.left:
#                     dfs(output, max(currMax, node.val), node.left)
#                 if node.right:
#                     dfs(output, max(currMax, node.val), node.right)

#             # print(node.val, output)

#         if root == None:
#             return 0
#         else:
#             output = [0]
#             dfs(output, root.val, root)
#             return output[0]






# previous approach
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def goodNodes(self, root: TreeNode) -> int:
#         def dfs(node, currMax, output):
#             if node.left == node.right == None:
#                 if node.val >= currMax:
#                     output[-1] +=1
#             else:
#                 if node.val >= currMax:
#                     output[-1] +=1
#                 if node.left:
#                     dfs(node.left, max(currMax, node.val), output)
#                 if node.right:
#                     dfs(node.right, max(currMax, node.val), output)
#         if root == None:
#             return 0
#         output = [0]
#         dfs(root, root.val, output)
#         return output[0]




