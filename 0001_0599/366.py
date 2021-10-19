# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findLeaves(self, root: TreeNode) -> 'List[List[int]]':
        def dfs(output, node):
            if node.left == node.right == None:
                if len(output) == 0:
                    output.append([])
                output[0].append(node.val)
                return 0 #this is the 1st to be removed
            else:
                leftLevel = rightLevel = -float('inf')
                if node.left:
                    leftLevel = dfs(output, node.left) + 1 #from left bottom
                if node.right:
                    rightLevel = dfs(output, node.right) + 1 # from right bottom

                realLevel= max(leftLevel, rightLevel)
                if realLevel == len(output): # the new level can only be previous Max + 1
                    output.append([])
                output[realLevel].append(node.val)
                return realLevel

        output = []
        dfs(output, root)
        return output


# previous approach

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# class Solution:
#     def findLeaves(self, root: TreeNode) -> 'List[List[int]]':
#         if root==None: return []
#         def helper(batch, node, root):
#             if node.left == node.right== None:
#                 batch[0].append(node.val)
#                 return 0
#             else:
#                 L = R = -float('inf')
#                 if node.left:
#                     L = helper(batch, node.left, root)+1
#                 if node.right:
#                     R = helper(batch, node.right, root)+1
#                 currBatch = max(L,R) #the batch number for the current node to be removed
#                 if currBatch not in batch:
#                     batch[currBatch] = []
#                 if node!=root:
#                     batch[currBatch].append(node.val)
#                 return currBatch
#         batch = {0:[]}
#         helper(batch, root, root)
#         if len(batch) == 1:
#             return [batch[k] for k in sorted(list(batch.keys())) if batch[k] ]
#         return [batch[k] for k in sorted(list(batch.keys())) if batch[k] ] + [[root.val]] # the final batch is the root, and root is excluded from the helper function
#
#


















