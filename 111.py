# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def dfs(curr, output, node):
            if node:
                if node.left == node.right == None:
                    output.append(curr)
                else:
                    if node.left!=None:
                        dfs(curr+1, output, node.left)
                    if node.right!=None:
                        dfs(curr+1, output, node.right)
        if root == None: return 0
        else:
            output = []
            dfs(1, output, root)
        return min(output)