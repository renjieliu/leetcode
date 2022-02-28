# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: 'Optional[TreeNode]') -> int:
        def helper(output, hmp, layer, node, idx): #find the distance of each node with the leftmost node on that level
            if node:
                helper(output, hmp, layer+1, node.left, idx*2+1)
                helper(output, hmp, layer+1, node.right, idx*2+2)
                if layer not in hmp:
                    hmp[layer] = []
                hmp[layer].append(idx)
                output[0] = max(output[0], idx - hmp[layer][0] + 1) #how many nodes are before current node on the same layer
        
        output = [0]
        helper(output, {}, 0, root, 0)
        return output[0]
    

    

# previous approach 

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def widthOfBinaryTree(self, root: TreeNode) -> int:
#         def flat(node, idx, level, hmp):
#             if node.left == node.right == None:
#                 if level not in hmp:
#                     hmp[level] = []
#                 hmp[level].append(idx)
#             else:
#                 if level not in hmp:
#                     hmp[level] = []
#                 hmp[level].append(idx)
#                 if node.left: flat(node.left, 2*idx+1, level +1 , hmp )
#                 if node.right: flat(node.right, 2*idx+2, level +1 , hmp )
#         if root == None:
#             return 0
#         else:
#             hmp ={}
#             flat(root, 0, 0, hmp)
#             output = -float('inf')
#             for k, v in hmp.items():
#                 output = max(output,v[-1] - v[0] +1)
#             return output



