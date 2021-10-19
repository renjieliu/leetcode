# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> 'List[List[int]]':
        def helper(hmp, level, node):
            if level not in hmp:
                hmp[level] = []
            hmp[level].append(node.val)
            if node.left:
                helper(hmp, level+1, node.left)
            if node.right:
                helper(hmp, level+1, node.right)
        if root == None:
            return []
        hmp = {}
        helper(hmp, 0, root)
        output = []
        for k in sorted(list(hmp.keys())):
            output.append(hmp[k])
        return output

# previous approach
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# class Solution:
#     def levelOrder(self, root: TreeNode) -> 'List[List[int]]':
#         def dfs(flat, node, level):  # flat :[number_left, number_right,level]
#             if node:
#                 if node.left == node.right == None:  # if leaf, then do nothing, as it has been added to the flat.
#                     return None
#                 elif node.left != None and node.right != None:  # add both, and go left, and go right
#                     flat.append([level, node.left.val])
#                     flat.append([level, node.right.val])
#                     dfs(flat, node.left, level + 1)
#                     dfs(flat, node.right, level + 1)
#                 elif node.left != None and node.right == None:  # add left only
#                     flat.append([level, node.left.val])
#                     dfs(flat, node.left, level + 1)
#                 elif node.right != None and node.left == None:  # add right only
#                     flat.append([level, node.right.val])
#                     dfs(flat, node.right, level + 1)
#
#         if root == None:
#             return []
#         else:
#             flat = [[0, root.val]]  # the root level,
#             dfs(flat, root, 1)
#             output = []
#             check = [0] * len(flat)
#             i = 0
#             while i < len(flat):
#                 if check[i] == 0:
#                     temp = [flat[i][1]]
#                     check[i] = 1
#                     for j in range(len(flat)):
#                         if check[j] == 0 and flat[j][0] == flat[i][0]:  # it's on the same level as the curr one.
#                             temp.append(flat[j][1])
#                             check[j] = 1
#                     output.append(temp)
#                 i += 1
#         return output
#
