# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def flat(output, node):
            if node.left == node.right == None:
                output.append(node.val)
            else:
                output.append(node.val)
                if node.left:
                    flat(output, node.left)
                if node.right:
                    flat(output, node.right)

        output = []
        if root == None: return 0
        flat(output, root)
        return len(output)

