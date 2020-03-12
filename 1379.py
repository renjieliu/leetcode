# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(node, target, output):
            if node.val == target.val:
                output.append(node)
            elif node.left == node.right == None:
                return
            else:
                if node.left != None:
                    dfs(node.left, target, output)
                if node.right != None:
                    dfs(node.right, target, output)

        output = []
        dfs(cloned, target, output)
        return output[0] if len(output) > 0 else []
