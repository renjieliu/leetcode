# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: 'Optional[TreeNode]', targetSum: int) -> 'List[List[int]]': # O( N | N )
        def dfs(output, curr, total, node,target): # flat and check each node and path, and see if the path sum up to target
            if node.left == node.right == None:
                if total + node.val == target:
                    output.append(curr + [node.val])
            if node.left:
                dfs(output, curr + [node.val], total + node.val, node.left, target)
            if node.right:
                dfs(output, curr + [node.val], total + node.val, node.right, target)
        
        if root == None:
            return []
        output = []
        dfs(output, [], 0, root, targetSum)
        return output
    


# previous solution

# # Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def pathSum(self, root: TreeNode, targetSum: int) -> 'List[List[int]]':
#         def dfs(output, node, curr, total, target):
#             if node.left == node.right == None:
#                 if total == target:
#                     output.append(curr)
#             else:
#                 if node.left:
#                     dfs(output, node.left, curr+[node.left.val], total+node.left.val, target)
#                 if node.right:
#                     dfs(output, node.right, curr+[node.right.val], total+node.right.val, target)

#         if root == None:
#             return []
#         output = []
#         dfs(output, root, [root.val], root.val, targetSum)
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
#     def pathSum(self, root: TreeNode, sum: int) -> 'List[List[int]]':
#         def flat(output, curr, path, node, target):
#             if node.left == node.right == None:
#                 if node.val+curr == target:
#                     output.append(path + [node.val])
#             else:
#                 if node.left:
#                     flat(output, curr+node.val, path + [node.val], node.left, target)
#                 if node.right:
#                     flat(output, curr+node.val, path + [node.val], node.right, target)
#         if root == None: return []
#         else:
#             output = []
#             flat(output, 0, [], root, sum)
#             return output