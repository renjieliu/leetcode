# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        def dfs(node, output):
            if node.left == node.right == None:
                output.append(node.val)
            else:
                output.append(node.val)
                dfs(node.left, output)
                dfs(node.right, output)

        output = []
        if root == None:
            return -1
        dfs(root, output)
        output = sorted(list(set(output)))
        return -1 if len(output) < 2 else output[1]
