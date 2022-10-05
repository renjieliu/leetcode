# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: 'Optional[TreeNode]', targetSum: int) -> bool: # O( N | 1 )
        def helper(node, curr, target): #check all the paths, and see if the path sum == target
            if node:
                if node.left == node.right == None:
                    return curr + node.val == target  
                else:
                    return helper(node.left, curr+node.val, target) or helper(node.right, curr+node.val, target)
        return root and helper(root, 0, targetSum)
    



# previous solution

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def hasPathSum(self, root: TreeNode, sum: int) -> bool:
#         def dfs(node, paths, curr):
#             if node:
#                 if node.left == node.right== None:
#                     paths.append(curr+node.val)
#                 else:
#                     if node.left != None:
#                         x = curr + node.val
#                         dfs(node.left, paths, x)
#                     if node.right!=None:
#                         y = curr + node.val
#                         dfs(node.right, paths, y)
#         paths = []
#         dfs(root, paths, 0)
#         return True if sum in paths else False



