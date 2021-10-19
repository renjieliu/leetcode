# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        def dfs(output, node, p):
            if node.val > p.val:
                if output == []:
                    output.append(node)
                elif node.val < output[0].val:
                    output[0] = node
            if node.left:
                dfs(output, node.left, p)
            if node.right:
                dfs(output, node.right, p)

        output = []
        dfs(output, root, p)
        return output[0] if output else None


