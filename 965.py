# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        def dfs(node, output):
            if node:
                output.append(node.val)
                if node.left == node.right == None:
                        return
                else:
                    if node.left != None:
                        dfs(node.left, output)
                    if node.right != None:
                        dfs(node.right, output)
        output = []
        dfs(root,output)
        return True if len(set(output))==1 else False