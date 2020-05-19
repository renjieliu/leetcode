# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, currMax, output):
            if node.left == node.right == None:
                if node.val >= currMax:
                    output[-1] +=1
            else:
                if node.val >= currMax:
                    output[-1] +=1
                if node.left:
                    dfs(node.left, max(currMax, node.val), output)
                if node.right:
                    dfs(node.right, max(currMax, node.val), output)
        if root == None:
            return 0
        output = [0]
        dfs(root, root.val, output)
        return output[0]