# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: 'TreeNode', u: 'TreeNode') -> 'Optional[TreeNode]':
        def helper(output, level, node, v, found):
            if node.val == v:
                found[0] = level # found the u node
            else:
                if found[0] == level: # pre-order traversal, if curr is on the same level, curr node is the closest on the right
                    output[0] = node
                    found[0] = -1 #reset found, and it will so the output will not be update again
                if node.left:
                    helper(output, level+1, node.left, v, found)
                if node.right:
                    helper(output, level+1, node.right, v, found)

        output = [None]
        helper(output, 0, root, u.val, [-1])
        return output[0]
        




# previous approach


# # Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
#         def helper(target, targetLayer, hmp, node, layer):  # to find the layer, and all the node in that layer
#             if layer not in hmp:
#                 hmp[layer] = []
#             hmp[layer].append(node.val)
#             if node.val == target:
#                 targetLayer[0] = layer
#             if node.left:
#                 helper(target, targetLayer, hmp, node.left, layer + 1)
#             if node.right:
#                 helper(target, targetLayer, hmp, node.right, layer + 1)

#         target = u.val
#         targetLayer = [None]
#         hmp = {}
#         helper(target, targetLayer, hmp, root, 0)

#         arr = hmp[targetLayer[0]]
#         ans = None
#         for i in range(len(arr)):  # find the value of the node (ans) to be returned
#             if arr[i] == target:
#                 if i == len(arr) - 1:
#                     return ans
#                 else:
#                     ans = arr[i + 1]
#                     break
#         output = []

#         def flat(output, node, ans):  # find the node and return
#             if node.val == ans:
#                 output.append(node)
#             else:
#                 if node.left: flat(output, node.left, ans)
#                 if node.right: flat(output, node.right, ans)

#         flat(output, root, ans)
#         return output[0]



# previous approach

# # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution(object):
#     def findNearestRightNode(self, root, u):
#         """
#         :type root: TreeNode
#         :type u: TreeNode
#         :rtype: TreeNode
#         """
#         hmp = {}  # to store all the level, and index
#         target_Level_idx = [-1, -1]
#
#         def flat(node, hmp, lvl, idx, v, target_Level):
#             if node.val == v:
#                 target_Level_idx[0] = lvl
#                 target_Level_idx[1] = idx
#             if lvl not in hmp:
#                 hmp[lvl] = []
#             hmp[lvl].append([idx, node])
#             if node.left == node.right == None:
#                 return None
#             else:
#                 if node.left:
#                     flat(node.left, hmp, lvl + 1, idx * 2 + 1, v, target_Level_idx)
#                 if node.right:
#                     flat(node.right, hmp, lvl + 1, idx * 2 + 2, v, target_Level_idx)
#
#         flat(root, hmp, 0, 0, u.val, target_Level_idx)
#         if target_Level_idx[0] == -1:
#             return None
#         else:
#             arr = hmp[target_Level_idx[0]]
#             arr.sort(key=lambda x: x[0])
#             for a in arr:  # on the same level, find the first one on the right of the node
#                 if a[0] > target_Level_idx[1]:
#                     return a[1]
#             return None
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
