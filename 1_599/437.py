# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: 'Optional[TreeNode]', targetSum: int) -> int:
        if root == None:
            return 0             
        def dfs(output, pathSum, lkp, targetSum,  node):
            accu = pathSum+node.val
          
            if accu-targetSum in lkp: # if the diff was seen, the targetSum is sum of the nodes in between
                output[0] += lkp[accu-targetSum]
            
            if accu not in lkp:
                lkp[accu] = 0 
            lkp[accu] += 1
            
            if node.left:
                dfs(output, accu, lkp, targetSum, node.left)
            if node.right:
                dfs(output, accu, lkp, targetSum, node.right)
                
            lkp[accu] -= 1 
            if lkp[accu]  == 0:
                del lkp[accu] 
        
        output = [0]
        dfs(output, 0, {0:1}, targetSum, root) 
        return output[0]
   


# previous approach 
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def pathSum(self, root: TreeNode, sum: int) -> int:
#         hmp = {0: 1}
#         output = [0]

#         def dfs(node, curr, target, hmp, output):
#             if node:
#                 curr += node.val
#                 if curr - target in hmp:
#                     output[0] += hmp[curr - target]
#                 if curr not in hmp:
#                     hmp[curr] = 0
#                 hmp[curr] += 1  # the value up to current node
#                 if node.left:
#                     dfs(node.left, curr, target, hmp, output)
#                 if node.right:
#                     dfs(node.right, curr, target, hmp, output)
#                 hmp[curr] -= 1  # leave current node
#                 if hmp[curr] == 0:
#                     del hmp[curr]

#         if root == None: return 0
#         dfs(root, 0, sum, hmp, output)
#         return output[0]

# previous approach
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def pathSum(self, root: TreeNode, sum: int) -> int:
#         hmp = {0: 1}
#         output = [0]
#
#         def dfs(node, curr, target, hmp, output):
#             if node:
#                 curr += node.val
#                 if curr - target in hmp:
#                     output[0] += hmp[curr - target]
#                 if curr not in hmp:
#                     hmp[curr] = 0
#                 hmp[curr] += 1
#                 if node.left:
#                     dfs(node.left, curr, target, hmp, output)
#                 if node.right:
#                     dfs(node.right, curr, target, hmp, output)
#                 hmp[curr] -= 1
#
#         if root == None: return 0
#         dfs(root, 0, sum, hmp, output)
#         return output[0]
#
#
