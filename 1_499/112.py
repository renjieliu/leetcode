# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def dfs(node, paths, curr):
            if node:
                if node.left == node.right== None:
                    paths.append(curr+node.val)
                else:
                    if node.left != None:
                        x = curr + node.val
                        dfs(node.left, paths, x)
                    if node.right!=None:
                        y = curr + node.val
                        dfs(node.right, paths, y)
        paths = []
        dfs(root, paths, 0)
        return True if sum in paths else False
