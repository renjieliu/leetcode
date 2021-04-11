# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        hmp = defaultdict(int)

        def dfs(hmp, layer, node):
            hmp[layer] += node.val
            if node.left:
                dfs(hmp, layer + 1, node.left)
            if node.right:
                dfs(hmp, layer + 1, node.right)

        dfs(hmp, 0, root)
        return hmp[max(hmp.keys())]

# previous approach
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# class Solution:
#     def deepestLeavesSum(self, root: TreeNode) -> int:
#         def findBottom(node, currLevel, bottom):
#             if node:
#                 if node.left == node.right == None:
#                     bottom.append(currLevel)
#                     return 1
#                 else:
#                     if node != None:
#                         findBottom(node.left, currLevel + 1, bottom)
#                         findBottom(node.right, currLevel + 1, bottom)
#
#         def findDeepest(node, output, currLevel, bottomLevel):
#             if node != None:
#                 if currLevel == bottomLevel and node.left == node.right == None:
#                     output.append(node.val)
#                     return
#                 else:
#                     findDeepest(node.left, output, currLevel + 1, bottomLevel)
#                     findDeepest(node.right, output, currLevel + 1, bottomLevel)
#
#         bottom = []
#         findBottom(root, 0, bottom)
#         bottomLevel = max(bottom)
#         output = []
#         findDeepest(root, output, 0, bottomLevel)
#         return sum(output)
#
#
