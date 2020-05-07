# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def flat(curr, node, path):
            if node.left == node.right == None:
                path.append(curr + [node.val])
            else:
                if node.left:
                    flat(curr + [node.val], node.left, path)
                if node.right:
                    flat(curr + [node.val], node.right, path)

        path = []
        flat([], root, path)
        x_depth = -1
        x_parent = -1
        y_depth = -1
        y_parent = -1
        for p in path:
            if x in p:
                x_depth = p.index(x)
                if x_depth > 0:
                    x_parent = p[x_depth - 1]
            if y in p:
                y_depth = p.index(y)
                if y_depth > 0:
                    y_parent = p[y_depth - 1]
        return True if x_depth != -1 and y_depth != -1 and x_depth == y_depth and x_parent != y_parent else False











# #OLD SOLUTION
#
#
#
#     # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# class Solution:
#     def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
#         def dfs(node,output, depth, v):
#             if node:
#                 if node.left==node.right ==None:
#                     return 0
#                 elif (node.left!=None and node.left.val == v) or (node.right !=None and node.right.val == v):
#                     output.append([node.val, depth, v]) #parent, level,  value
#                     return 1
#                 else:
#                     dfs(node.left, output, depth+1, v)
#                     dfs(node.right,output, depth+1, v)
#         output = []
#         dfs(root, output, 0, x)
#         dfs(root, output, 0, y)
#         if len(output) !=2:
#             return False
#         return True if output[0][0] != output[1][0] and output[0][1] == output[1][1] else False