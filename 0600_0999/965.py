# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        def dfs(node, val):
            if node.val != val:
                return False
            else:
                if node.left != None and dfs(node.left, val) == False:
                    return False
                if node.right != None and dfs(node.right, val) == False:
                    return False
            return True

        return dfs(root, root.val)